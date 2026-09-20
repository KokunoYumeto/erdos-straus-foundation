"""Exact local-algebra transport; includes the nonconstant residue-unit correction."""
import sympy as s
from common import Suite
T=Suite('local_es_rh_transport')
e,z,c=s.symbols('epsilon eta c', nonzero=True)
ga,gb,ha,hb=s.symbols('g_ES g_RH g1_ES g1_RH', nonzero=True)
# A double root has eta^2=2*g0*epsilon. The local residue is NOT
# merely extraction of the top eta coefficient: the cofactor derivative matters.
p,g=s.symbols('p gamma',positive=True); sign=s.symbols('sign',real=True)
r=s.symbols('r')
hes=-s.Rational(5,22)/p*(r-p)**2*(r-s.Rational(2,5)*p)*(r-2*p)
ges=s.div(hes,(r-p)**2,r)[0]
T.equal('ES cofactor constant',ges.subs(r,p),3*p/22)
T.equal('ES cofactor derivative',s.diff(ges,r).subs(r,p),s.Rational(1,11))
T.equal('actual repeated ES example',s.Rational(1,5)+s.Rational(1,2)+s.Rational(1,10),s.Rational(4,5))
# Use each explicit RH root so no equation for a symbolic sign is assumed.
for sig in [1,-1]:
 root=s.Rational(1,2)+sig*s.I*g
 hr=-s.Rational(1,2)*((r-s.Rational(1,2))**2+g**2)**2
 gr=s.div(hr,(r-root)**2,r)[0]
 T.equal(f'RH cofactor constant {sig}',gr.subs(r,root),2*g**2)
 T.equal(f'RH cofactor derivative {sig}',s.diff(gr,r).subs(r,root),-2*sig*s.I*g)
 T.equal(f'local unit coefficient {sig}',s.Rational(1,11)/(3*p/22)-(-2*sig*s.I*g)/(2*g**2),2/(3*p)+sig*s.I/g)
# The exact pullback identity on 1,epsilon,eta,eta*epsilon.
# c^2=g_ES/g_RH. Eliminate g_ES by c^2*g_RH.
ga=c**2*gb
u0=c**3; u1=c**3*(ha/ga-hb/gb)
# Lambda_ES(eta*(b0+b1*epsilon))=b1/g_ES-b0*g1_ES/g_ES^2.
for b0,b1 in [(0,0),(1,0),(0,1),(2,3)]:
 lhs=c*(b1/gb-b0*hb/gb**2)
 rhs=(u0*b1+u1*b0)/ga-u0*b0*ha/ga**2
 T.equal(f'full residue functional transport {b0},{b1}',lhs,rhs)
T.reject('the cofactor derivative may be silently discarded',s.cancel(c*(-hb/gb**2)-c**3*(-ha/ga**2))==0)
# Polynomial lift into eta^4=0 preserves centered action, and changes
# uncentered action by exactly p-root.
T.equal('centered generator under eta scaling',c**2*z**2/(2*ga),z**2/(2*gb))
T.equal('coordinate determinant',s.diag(1,c,c**2,c**3).det(),c**6)
T.save({'local_length':4,'residue_unit':'c^3*(1+(2/(3*p)+i*sign/gamma)*epsilon)',
        'scaling_equation':'c^2=3*p/(44*gamma^2)',
        'qualification':'Residue pairing is complex bilinear, not the original Hermitian norm.'})
