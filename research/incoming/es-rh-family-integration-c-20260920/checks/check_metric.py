from __future__ import annotations
import sys
import sympy as s
from core import top_chain_data,adjoint,zero
from receipt import Receipt
R=Receipt('metric_change_and_native_scale_obstruction')
# Exact exterior-power mechanism in weighted cyclic shifts.
# This is deliberately not labelled as the native arithmetic packet.
for q in range(2,11):
    rho=s.Integer(3);k=s.Integer(2)
    P=s.zeros(q)
    for j in range(q):P[(j+1)%q,j]=1
    M=k*P;D=s.diag(*[rho**j for j in range(q)]);G=D*D
    Mc=D*M*D.inv()
    sigmas=[k*rho]*(q-1)+[k/rho**(q-1)]
    R.equal((Mc.T*Mc).det(),s.prod(x*x for x in sigmas),'singular determinant')
    R.equal(Mc.det(),M.det(),'determinant preserved by actual metric isometry')
    R.equal(s.trace(adjoint(M,G)*M),sum(x*x for x in sigmas),'native-style weighted Hilbert-Schmidt trace')
    R.equal((Mc.T*Mc).trace(),k*k*((q-1)*rho*rho+rho**(-2*(q-1))),'singular list exact')
    median=s.Rational(q-1,2)
    distance_coefficient=2*sum(abs(s.Integer(j)-median) for j in range(q))
    for rank in range(1,q):
        exterior_log_coefficient=2*rank*(q-rank)
        R.require(exterior_log_coefficient>=2*rank,'finite exterior lower bound')
        R.require(distance_coefficient>=min(exterior_log_coefficient,2*rank),'scale-free trace-log bound')
        R.equal(exterior_log_coefficient,2*(sum(range(q-rank,q))-sum(range(rank))),'exact external rank coefficient')
    R.false(s.trace(M.T*M)==s.trace(adjoint(M,G)*M),'same eigenvalues do not fix metric singular values')
# Constructed repeated-jet blocks, all retained phases.
delta=s.Rational(1,5);gamma=s.Integer(3)
for k in [1,3,5]:
    for mult in [1,2,3]:
        D=k*(mult-1);eta=delta/(D+1) if D else s.Integer(1)
        G,N,_,_,_,_=top_chain_data([(D,7,0)],eta)
        NN=adjoint(N,G)*N
        if D:
            for j in range(D):
                R.equal(NN[j,j],eta**2*(j+1)*(D-j),'exact nilpotent singular coefficient')
                R.require(NN[j,j]<=delta**2/4,'source chosen eta contracts full nilpotent chain')
        xx,yy=s.symbols('xx yy',real=True)
        Ms=(xx+s.I*yy)*s.eye(D+1)-s.I*N
        local_cost=s.trace(adjoint(Ms,G)*Ms)-s.re(s.trace(Ms*Ms))
        R.equal(local_cost,2*(D+1)*yy**2+s.trace(NN),'general complex block metric identity')
        alpha=k*(gamma-s.I*delta)
        Mf=alpha*s.eye(D+1)-s.I*N
        ainv=s.expand_complex(1/alpha)
        powers=[ainv]
        for power in range(D):powers.append(s.expand(powers[-1]*s.I*ainv))
        Inv=s.zeros(D+1)
        for row in range(D+1):
            for col in range(row+1):Inv[row,col]=powers[row-col]
        R.equal((Mf*Inv).applyfunc(s.expand),s.eye(D+1),'finite exact local inverse')
        total=s.Integer(0)
        for a in range(k+1):
            for b in range(k+1):
                re=(2*b-k)*gamma; im=-(2*a-k)*delta
                R.require(re*re+im*im>=delta**2+gamma**2,'minimum original eigenvalue modulus')
                total+=2*(D+1)*im**2+s.trace(NN)
        q=(D+1)*(k+1)**2
        predicted=q*(2*delta**2*k*(k+2)/3+eta**2*D*(D+2)/6)
        R.equal(total,predicted,'incoming complete quadratic metric cost')
        R.equal(adjoint(N,5**k*G),adjoint(N,G),'actual scalar section cost cancels from adjoint only')
# Gauge-median identity, distinct from a largest/smallest norm ratio.
for logs in [[0,1,2,3],[0,0,0,10],[0,2,3,7,9],[1,1,1]]:
    n=len(logs);m=n//2;ls=sorted(logs,reverse=True)
    median=sorted(logs)[(n-1)//2]
    distance=sum(abs(v-median) for v in logs)
    R.equal(distance,sum(ls[:m])-sum(ls[n-m:]),'median and exterior identity')
R.false(sum([0,0,0,10])==4*(10-0),'log-volume distance is not dimension times condition')
R.extra['native_asymptotic_status']='Not numerically evaluated. Conditional theorem follows in manuscript from cited NG20-21 and the finite exterior inequality.'
R.write(sys.argv[1])
