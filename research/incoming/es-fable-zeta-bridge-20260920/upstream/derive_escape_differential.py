"""Exact Laurent matrices on the original ES escaping branch; no float arithmetic."""
import contextlib
import io
import itertools
import json
import sys
from pathlib import Path
import sympy as s

base = Path(__file__).resolve().parent
sys.path.insert(0, str(base / 'independent'))
with contextlib.redirect_stdout(io.StringIO()):
    from verify_four_labels import P, a, y, z, w

t = s.symbols('epsilon', positive=True)
qs = s.Matrix([t, 0, s.I / 2, 0])
qe = s.Matrix([-t, 2*s.I/t, 6*s.I/t**2-s.I/2, 40*s.I/t**3])
J = P.jacobian([a,y,z,w])
Js = J.subs(dict(zip([a,y,z,w],qs))).applyfunc(s.expand)
Je = J.subs(dict(zip([a,y,z,w],qe))).applyfunc(s.expand)
Ji = (-Je.adjugate()/2).applyfunc(s.expand)
assert (Je*Ji-s.eye(4)).applyfunc(s.expand)==s.zeros(4)
assert s.factor(Je.det()) == -2

def leading(mat):
    terms = [(int(term.as_powers_dict().get(t,0)), term)
             for x in mat for term in s.Add.make_args(s.expand(x)) if term != 0]
    valuation = min(k for k,_ in terms)
    limit = mat.applyfunc(lambda x:s.expand(x).coeff(t,valuation))
    return valuation, limit

def compound(mat,r):
    inds = list(itertools.combinations(range(4),r))
    return s.Matrix([[s.expand(mat.extract(I,J).det()) for J in inds] for I in inds])

out = {'branch':[str(x) for x in qe], 'forward':{}, 'inverse':{}}
lines=[]
for name,mat in [('forward',Je),('inverse',Ji)]:
    lines += [name+' full matrix', s.latex(mat)]
    out[name]['matrix']=[[str(mat[j,k]) for k in range(4)] for j in range(4)]
    for r in range(1,5):
        C=compound(mat,r)
        val,L=leading(C)
        out[name][str(r)]={'valuation':val,'limit_rank':L.rank(),
             'leading_matrix':[[str(x) for x in row] for row in L.tolist()]}
        lines += [f'{name} wedge {r}: valuation={val}, rank={L.rank()}',s.latex(L)]
        assert L != s.zeros(L.rows,L.cols)
        assert (t**(-val)*C-L).applyfunc(lambda x:s.limit(x,t,0)) == s.zeros(L.rows,L.cols)

velocity=qe.diff(t)
image_velocity=(P.subs(dict(zip([a,y,z,w],qs)))).diff(t)
assert (Je*velocity-image_velocity).applyfunc(s.expand)==s.zeros(4,1)
out['velocity_identity']=True
out['inverse_determinant']=str(s.factor(Ji.det()))
out['all_checks_passed']=True
(base/'escape_differential_exact.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
(base/'escape_differential_matrices.txt').write_text('\n\n'.join(lines)+'\n',encoding='utf-8')
print('\n'.join(x for x in lines if 'valuation=' in x))
print('Exact matrix inverse, every exterior leading coefficient, and velocity identity passed.')
