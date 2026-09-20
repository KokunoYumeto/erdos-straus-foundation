import sympy as s
from common import Suite
from bernstein import coefficients,enclosure,certify_positive
T=Suite('polynomial_sign_certificate');x,y=s.symbols('x y',real=True);box=[(s.Integer(0),s.Integer(1))]*2
P=(x-s.Rational(1,2))**2+(y-s.Rational(1,2))**2+s.Rational(1,100)
T.require('initial positive polynomial needs subdivision',enclosure(P,(x,y),box)[0]<0)
receipt=certify_positive(P,(x,y),box)
T.require('strictly positive polynomial certified',receipt['status']=='positive certificate')
trap=2*(x-s.Rational(1,4))*(x-s.Rational(3,4))+y*(1-y)/100
T.require('all trap corners positive',all(trap.subs({x:a,y:b})>0 for a in [0,1] for b in [0,1]))
negative=certify_positive(trap,(x,y),box)
T.require('interior negative value found',negative['status']=='negative witness')
T.reject('positive vertices certify positive current',trap.subs({x:s.Rational(1,2),y:s.Rational(1,2)})>0)
# reconstruct a nontrivial degree (3,2) polynomial from exact coefficients
f=x**3-2*x*y+3*y*y+s.Rational(2,7);coeff=coefficients(f,(x,y),box);d=(3,2)
recon=sum(c*s.binomial(3,a[0])*x**a[0]*(1-x)**(3-a[0])*s.binomial(2,a[1])*y**a[1]*(1-y)**(2-a[1]) for a,c in coeff.items())
T.equal('Bernstein reconstruction',f,recon)
T.save({'positive':receipt,'negative':negative})
