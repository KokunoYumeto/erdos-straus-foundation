"""Retained mathematical source identity record; no source is changed."""
from pathlib import Path
import json,hashlib
here=Path(__file__).resolve().parent;arrival=here.parent;spectral=arrival.parent
sources={
 'received-primary-resolvent':arrival/'01_COMPLETE_PROOFS (5).md',
 'received-relative-growth-and-es':arrival/'03_Pasted text.txt',
 'received-angular-strengthening':spectral/'angular_strengthening_20260922/01_Pasted text.txt',
 'arxiv:0808.1408v2-translator-tex':arrival/'human_sources/0808.1408v2/tex/dirichlet.tex',
}
out=[dict(id=k,path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for k,p in sources.items()]
(here/'ES_SOURCE_IDENTITIES.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
