#!/usr/bin/env python3
"""Verify source integrity, replay comparisons, fixtures and this continuation's links.

Standard library only; no network, no subprocess, no writes. Run without -O
when also using the original Boolean fixture's internal assertions.
"""
import gzip
import hashlib
import importlib.util
import json
from math import gcd
from pathlib import Path
import re
from itertools import combinations
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent


def require(ok, message):
    if not ok:
        raise ValueError(message)


def read_json(path):
    data = gzip.decompress(path.read_bytes()) if path.suffix == '.gz' else path.read_bytes()
    return json.loads(data)


def main():
    release = read_json(ROOT / 'RELEASE_FILES.json')
    for entry in release['new_files']:
        path = (ROOT / entry['path']).resolve()
        require(path.is_relative_to(ROOT), 'Escaped release path')
        data = path.read_bytes()
        require(len(data) == entry['bytes'], 'Changed release size: ' + entry['path'])
        require(hashlib.sha256(data).hexdigest() == entry['sha256'],
                'Changed release hash: ' + entry['path'])
    require(hashlib.sha256((ROOT / release['original_manifest']).read_bytes()).hexdigest()
            == release['original_manifest_sha256'], 'Original manifest hash changed')
    manifest = read_json(ROOT / 'received/ARTIFACT_PROVENANCE.json')
    for entry in manifest['members']:
        path = (ROOT / 'received' / entry['member']).resolve()
        require(path.is_relative_to(ROOT / 'received'), 'Escaped artifact path')
        data = path.read_bytes()
        require(len(data) == entry['bytes'], 'Changed source size: ' + entry['member'])
        require(hashlib.sha256(data).hexdigest() == entry['sha256'],
                'Changed source hash: ' + entry['member'])
    require(len(manifest['members']) == 429, 'Wrong original source count')
    alignment = ROOT / 'received/es_dual_frontier/lineage/aligned_isometry.json'
    require(alignment.read_bytes() == (alignment.parent / 'lineage/aligned_isometry.json').read_bytes(),
            'Compatibility copy changed')
    comparisons = 0
    for package, output in [('es_dual_frontier', 'dual'), ('es_s6_counterfactual', 's6')]:
        for path in sorted((ROOT / 'checks' / output).iterdir()):
            if path.name.endswith(('.json', '.json.gz')):
                original = ROOT / 'received' / package / 'certificates' / path.name
                require(read_json(path) == read_json(original), 'Replay mismatch: ' + path.name)
                comparisons += 1
    require(comparisons == 28, 'Missing received/replay comparison')
    energy = read_json(ROOT / 'checks/energy/mathematical_summary.json')
    require(energy['status'] == 'passed', 'Energy check failed')
    require(energy['scan']['shell_count'] == 9531, 'Wrong scan domain')
    require(energy['scan']['certification_counts'] ==
            {'unpartitioned': 214, 'jacobi': 231, 'quadratic': 240}, 'Wrong energy counts')
    spec = importlib.util.spec_from_file_location('boolean_fixtures', ROOT / 'reconstructed/boolean_exact_checks.py')
    fixtures = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fixtures)
    require(fixtures.short_pairs(61, 4) == [[2,3,1],[3,2,1]], '61 box')
    require(fixtures.short_pairs(73, 4) == [[1,3,1],[3,1,1]], '73 box')
    require(fixtures.short_pairs(193, 4) == [[3,4,1],[4,3,1]], '193 box')
    require(fixtures.short_pairs(2521, 4) == [[1,26,181],[26,1,181]], '2521 box')
    require(fixtures.short_pairs(73, 8) ==
            [[1,7,78937],[4,5,4057],[5,4,4057],[7,1,78937]], 'Phi24 box')
    require(fixtures.first_layer_hits(2521) == [], 'First layer not empty')
    for p, full, minimal in [(13,5,4),(37,12,9),(61,15,11)]:
        fibre = fixtures.permutation_fibres(p)
        require(fibre['full_hits']==full and fibre['minimal_half_hits']==minimal
                and fibre['all_exact_fibres_verified'], 'Permutation fibre mismatch')
    for p,a in [(37,18),(61,22),(3361,847)]:
        shell = fixtures.shell(p,a)
        require(not shell['E'] and not shell['M'], 'Expected empty shell')
    for p,a,u,e in [(193,50,250,0),(2521,636,50562,1),(3361,841,29,0)]:
        row = fixtures.reconstruct(p,a,u,e)
        x,y,z = row['xyz']
        require(min(x,y,z)>0 and 4*x*y*z == p*(x*y+x*z+y*z), 'False fixture witness')
    # Independent integer conjugacy checks retain g and all three coordinates.
    checks = 0
    for g in range(-2,3):
        for x in range(-3,4):
            for y in range(-3,4):
                for z in range(-3,4):
                    def to_t(v):
                        X,Y,Z=v
                        return (-X-Y-Z-2*g,-X-Z+2*g,-Z)
                    t0,t1,t2=to_t((x,y,z))
                    require((t2-t1+2*g,-t0+t1-4*g,-t2)==(x,y,z), 'Affine inverse')
                    require(to_t((6*g+y,-6*g-x-y,z-2*g+x)) == (t2,t0,t1), 'a1 conjugacy')
                    require(to_t((-y,x-6*g,z+3*g+y)) ==
                            (t1-g,t2-g,t0-t1+t2+g), 'a2 conjugacy')
                    require(to_t((x,y+x,z-g)) ==
                            (t0+t1-t2-g,t1+g,t2+g), 'cusp conjugacy')
                    X,Y,W=t2-t1,t0-t1,-t0-t1-t2
                    require((W-2*X+Y)%3 == 0, 'Integral gluing')
                    require(2*(X*X-X*Y+Y*Y)+W*W == 3*(t0*t0+t1*t1+t2*t2), 'Exact norm')
                    checks += 1
    for R in range(1,50,2):
        for g in range(R):
            d=gcd(R,g); D=R//d
            values=[g*v%R for v in range(D)]
            require(len(set(values))==D and set(values)==set(range(0,R,d)), 'Gate image')
            if D>1:
                require(all(((w//d)*pow(g//d,-1,D))%D==v for v,w in enumerate(values)),
                        'Gate inverse')
    # Picard coordinates mean d H - sum m_i E_i. Keep the six blowup marks.
    lines=[]
    for i in range(6):
        v=[0]*7; v[i+1]=-1; lines.append(tuple(v))
    for i,j in combinations(range(6),2):
        v=[1]+[0]*6; v[i+1]=v[j+1]=1; lines.append(tuple(v))
    for i in range(6):
        v=[2]+[1]*6; v[i+1]=0; lines.append(tuple(v))
    def pairing(a,b): return a[0]*b[0]-sum(x*y for x,y in zip(a[1:],b[1:]))
    gamma=(1,1,1,1,0,0,0)
    def turn(v):
        h=pairing(v,gamma)
        c=tuple(x+h*y for x,y in zip(v,gamma))
        return (c[0],c[2],c[3],c[1],c[4],c[5],c[6])
    require({turn(v) for v in lines}==set(lines), 'All 27 line classes')
    for v in lines:
        w=v
        for _ in range(6): w=turn(w)
        require(w==v, 'Marked six-cycle order')
        for z in lines:
            require(pairing(turn(v),turn(z))==pairing(v,z), 'Picard intersections')
    boundary=[(0,-1,0,0,0,0,0),(1,1,1,0,0,0,0),
              (0,0,-1,0,0,0,0),(1,0,1,1,0,0,0),
              (0,0,0,-1,0,0,0),(1,1,0,1,0,0,0)]
    require(all(turn(v)==boundary[(i+1)%6] for i,v in enumerate(boundary)), 'Marked boundary cycle')
    record=read_json(ROOT/'continuation.json')
    for claim in record['mathematics']:
        require((ROOT/claim['proof']).is_file(), 'Missing proof: '+claim['id'])
    require((ROOT/record['additional_geometric_proof']['proof']).is_file(),
            'Missing marked Picard proof')
    links=0
    for name in ['README.md','PROVENANCE.md','VERIFY.md','CORRECTIONS.md']:
        for raw in re.findall(r'\]\(([^)\s]+)\)', (ROOT/name).read_text(encoding='utf-8')):
            url=urlsplit(raw)
            if url.scheme or not url.path:
                continue
            require((ROOT/unquote(url.path)).exists(), 'Missing local link: '+raw)
            links+=1
    print(json.dumps({'status':'passed','original_files':429,'new_release_files':len(release['new_files']),
                      'replay_objects':comparisons,
                      'exact_affine_integer_states':checks,'picard_line_classes':27,'local_links':links,
                      'scope':'source integrity, finite exact checks and proof locators; not a universal ES proof'}))


if __name__ == '__main__':
    main()
