"""Exact tensor-product Bernstein bounds on rational boxes.

This is a finite polynomial certificate, not a model of native moments.
A successful box certificate is sufficient even when the feasible native
parameters are correlated. Failure on the box need not imply native failure.
"""
from itertools import product
import sympy as s

def coefficients(expr,variables,box):
    if not variables or len(variables)!=len(box): raise ValueError('dimension mismatch')
    if len(set(variables))!=len(variables): raise ValueError('variables must be distinct')
    expr=s.sympify(expr)
    if expr.has(s.Float): raise ValueError('exact coefficients are required; floats are not certificates')
    box=tuple((s.sympify(lo),s.sympify(hi)) for lo,hi in box)
    if not all(lo.is_Rational and hi.is_Rational for lo,hi in box):
        raise ValueError('exact rational box endpoints are required')
    for lo,hi in box:
        if not (lo<hi): raise ValueError('box intervals must have positive width')
    tt=s.symbols(f'_t0:{len(variables)}',real=True)
    p=s.Poly(s.expand(expr.subs({x:lo+(hi-lo)*u for x,(lo,hi),u in zip(variables,box,tt)},simultaneous=True)),*tt)
    if p.is_zero: return {(0,)*len(variables):s.Integer(0)}
    if not all(c.is_Rational for c in p.coeffs()):
        raise ValueError('this implementation requires exact rational polynomial coefficients')
    deg=p.degree_list();terms=p.terms();out={}
    for alpha in product(*[range(d+1) for d in deg]):
        total=s.Integer(0)
        for beta,c in terms:
            if all(b<=a for a,b in zip(alpha,beta)):
                total+=c*s.prod(s.binomial(a,b)/s.binomial(d,b) for a,b,d in zip(alpha,beta,deg))
        total=s.cancel(total)
        if total.is_real is not True: raise ValueError('real coefficients are required')
        out[alpha]=total
    return out

def enclosure(expr,variables,box):
    c=coefficients(expr,variables,box)
    return min(c.values()),max(c.values())

def certify_positive(expr,variables,box,max_depth=16):
    stack=[(tuple(box),0)];leaves=[]
    while stack:
        B,depth=stack.pop();lo,hi=enclosure(expr,variables,B)
        if lo>0:leaves.append({'box':[[str(a),str(b)] for a,b in B],'lower':str(lo),'upper':str(hi)});continue
        mid=tuple((a+b)/2 for a,b in B);val=s.cancel(expr.subs(dict(zip(variables,mid))))
        if val<0:return {'status':'negative witness','point':[str(v) for v in mid],'value':str(val),'positive_leaves':len(leaves)}
        if depth>=max_depth:return {'status':'inconclusive','positive_leaves':len(leaves)}
        j=max(range(len(B)),key=lambda k:B[k][1]-B[k][0]);a,b=B[j];m=(a+b)/2
        B1=list(B);B2=list(B);B1[j]=(a,m);B2[j]=(m,b)
        stack.extend([(tuple(B2),depth+1),(tuple(B1),depth+1)])
    return {'status':'positive certificate','leaf_count':len(leaves),'leaves':leaves}
