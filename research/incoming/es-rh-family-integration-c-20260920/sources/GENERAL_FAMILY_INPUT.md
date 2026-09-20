# General-family control: multiplicities, collisions, source sections, and all mixed minima

**The family calculation now works without assuming equal multiplicities or separated sum centres.** It gives an exact formula for the mixing caused by unequal primary lengths, a finite enlargement that captures every adjoint-generated direction, and a uniform construction inside the original ordered tensor theta source.

For a fixed original divisor `h`, of degree `d`, and any prescribed positive tolerance `t_*`, the construction produces a section `\mathcal R_{k,t_*}` with

```math
\boxed{ \begin{aligned} \deg_{\mathrm{total}}\mathcal R_{k,t_*} &\le k(2d-1),\\ 0\le \operatorname{Tr}(A_k+A_k^\dagger-kI)_+ -\mathcal L_k &\le t_*,\\ \log\operatorname{cond}(G_{k,t_*},G_{k,1}) &\le C_hk\bigl[\log(k+2)+\log^+(1/t_*)\bigr]. \end{aligned}} \tag{1}
```

Here `\mathcal L_k` is the **original full algebraic spectral aggregate**, including every multiplicity. The constructed metric does not remove it. The condition number in (1) compares two explicitly constructed metrics on the same cyclic space; it is not silently a comparison with the original canonical `G_N`.

The return to that original scalar-source metric is also explicit below. It retains the actual cross Gram and the complete additional minimum.

[**Complete proofs, with intact LaTeX**](sandbox:/mnt/data/Programme_General_Families_20260920/COMPLETE_PROOFS.md) · [**Full package**](sandbox:/mnt/data/Programme_General_Families_20260920.zip) · [**Scope, inputs, and result register**](sandbox:/mnt/data/Programme_General_Families_20260920/README.md)

This continuation uses the preserved original-source definitions and the supplied complete section construction. **I have not verified a newer GitHub revision for this package.**

The Deligne/BBT direction is useful here in a precise way: we can calculate the parameter strata, boundary exponents, metric connections, and full subquotient corrections directly. I have not inserted an unconstructed Hodge filtration, polarization, or horizontal period map into the argument.

---

# 1. The full tensor metric can be calculated before imposing equal multiplicities

For factor `i`, retain

```math
h_i(s)=\prod_{\rho\in Z_i}(s-\rho)^{m_{i,\rho}}, \qquad d_{i,\rho}=m_{i,\rho}-1.
```

The original divided-jet coordinates are

```math
J_i[P]_{\rho,j}=\frac{P^{(j)}(\rho)}{j!}.
```

Their inverse is the complete Hermite remainder map. With

```math
h_{i,\rho}=\frac{h_i}{(s-\rho)^{m_{i,\rho}}},
```

it sends local polynomials `p_\rho` to

```math
\sum_\rho h_{i,\rho}(s)\, \operatorname{rem}_{(s-\rho)^{m_{i,\rho}}} \left(\frac{p_\rho(s-\rho)}{h_{i,\rho}(s)}\right). \tag{2}
```

The physical injection still contains

```math
\upsilon_i=j_{h_i}(2\xi/h_i).
```

Let `U_i` be multiplication by this **complete** unit. Its local matrix is lower triangular, with

```math
(U_i)_{\rho;jl}=(\upsilon_i)_{\rho,j-l}, \qquad j\ge l.
```

The original tensor injection is

```math
\eta_k=(U_1\otimes\cdots\otimes U_k)\beta, \qquad \beta[P]=P(s_1+\cdots+s_k).
```

These are the retained cyclic and physical maps from the source calculation.

## 1.1 A metric adapted to the complete nilpotent chains

Choose positive root weights `a_{i,\rho}` and one common scale `0<\eta\le1`. On polynomial divided jets, define

```math
\boxed{ g_{i,\rho,j} = a_{i,\rho}(j!)^2 \binom{d_{i,\rho}}j\eta^{2j}. } \tag{3}
```

On physical jets, use the exact transported metric

```math
(U_i^{-1})^*\operatorname{diag}(g_{i,\rho,j})U_i^{-1}. \tag{4}
```

Thus `U_i` is the displayed isometry between the two descriptions. No derivative of the physical unit is omitted.

On a local factor `\mathbb C[z]/z^{d+1}`, multiplication `N=M_z` has adjoint

```math
N^\dagger z^j = \eta^2j(d-j+1)z^{j-1}. \tag{5}
```

Consequently

```math
E=N/\eta,\qquad F=N^\dagger/\eta,\qquad H=[F,E]
```

satisfy, by direct calculation,

```math
Hz^j=(d-2j)z^j,
```

```math
[H,E]=-2E,\qquad [H,F]=2F,\qquad [F,E]=H. \tag{6}
```

The actual orthonormal-coordinate entries of `N` are

```math
\eta\sqrt{(j+1)(d-j)}.
```

The unitary rotation of the degree-`d` two-variable polynomial representation therefore gives

```math
\boxed{ \operatorname{spec}(N+N^\dagger) = \eta\{-d,-d+2,\ldots,d\}. } \tag{7}
```

This is an exact finite representation, including the whole nilpotent chain.

## 1.2 Collect all coincident sum centres explicitly

For an ordered tuple `\boldsymbol\rho=(\rho_1,\ldots,\rho_k)`, set

```math
\kappa_{\boldsymbol\rho}=\sum_i\rho_i, \qquad D_{\boldsymbol\rho}=\sum_i d_{i,\rho_i}, \qquad A_{\boldsymbol\rho}=\prod_i a_{i,\rho_i}.
```

At a sum centre `\kappa`, the original cyclic length is

```math
D_\kappa+1,\qquad D_\kappa= \max_{\kappa_{\boldsymbol\rho}=\kappa}D_{\boldsymbol\rho}.
```

Thus

```math
\chi_k(S)=\prod_\kappa(S-\kappa)^{D_\kappa+1}. \tag{8}
```

Define

```math
W_{\kappa,D} = \sum_{\substack{\kappa_{\boldsymbol\rho}=\kappa\\ D_{\boldsymbol\rho}=D}} A_{\boldsymbol\rho}, \qquad S_{\kappa,j} = \sum_DW_{\kappa,D}\binom Dj. \tag{9}
```

Every ordered tuple is counted in `W_{\kappa,D}`. The binomial identity gives

```math
\left\|\left(\sum_i z_i\right)^j\right\|^2 = A_{\boldsymbol\rho}(j!)^2\eta^{2j} \binom{D_{\boldsymbol\rho}}j.
```

The full induced cyclic metric is therefore

```math
\boxed{ \|v\|_{G_{k,\eta}}^2 = \sum_\kappa\sum_{j=0}^{D_\kappa} (j!)^2\eta^{2j}S_{\kappa,j}|v_{\kappa,j}|^2. } \tag{10}
```

There is a compact exact formula for all its coefficients:

```math
S_{\kappa,j} = [X^\kappa z^j] \prod_{i=1}^k \left( \sum_{\rho\in Z_i} a_{i,\rho}X^\rho(1+z)^{d_{i,\rho}} \right), \tag{11}
```

in the group algebra with `X^\rho X^\sigma=X^{\rho+\sigma}`.

Equation (11) incorporates additive coincidences by their actual equality. It does not assume that the root labels are additively independent.

---

# 2. Unequal-length mixing is exactly a weighted variance

The original forward action satisfies

```math
A_{\mathrm{sum}}\beta=\beta A_{\mathrm{cyc}}.
```

Let `\Pi` be the orthogonal projection onto `\operatorname{im}\beta` in the metric just specified. Define the actual adjoint leakage

```math
Z= A_{\mathrm{sum}}^\dagger\beta -\beta A_{\mathrm{cyc}}^\dagger = (I-\Pi)A_{\mathrm{sum}}^\dagger\beta. \tag{12}
```

At `(\kappa,j)`, `j\ge1`, introduce the probability weights

```math
\pi_{\kappa,j-1}(D) = \frac{W_{\kappa,D}\binom D{j-1}}{S_{\kappa,j-1}}.
```

The complete calculation is

```math
\boxed{ Z^\dagger Z\big|_{(\kappa,j)} = \eta^2 \frac{S_{\kappa,j-1}}{S_{\kappa,j}} \operatorname{Var}_{\pi_{\kappa,j-1}}(D). } \tag{13}
```

Its value at `j=0` is zero.

To prove it, the full tuple adjoint acts by

```math
R^\dagger R^j = \eta^2j(D-j+1)R^{j-1}.
```

Projection onto the common cyclic coefficient gives

```math
\eta^2j^2\frac{S_{\kappa,j}}{S_{\kappa,j-1}}.
```

Subtract this coefficient inside every tuple and sum the squared residual in the original tensor metric. The result is precisely the variance in (13). Distinct `j` have distinct output degree, so the displayed operator is diagonal; no off-diagonal residual has been discarded.

There are three concrete consequences.

### Exact rank

Let `D_{\max}>D_{\mathrm{second}}` be the two largest **distinct** lengths occurring at `\kappa`. Then

```math
\boxed{ \operatorname{rank}Z_\kappa=D_{\mathrm{second}}+1. } \tag{14}
```

The variance is positive exactly for `j=1,\ldots,D_{\mathrm{second}}+1`.

When all lengths at that centre agree, the variance is zero at every level. Conversely, its `j=1` value shows that zero leakage forces those lengths to agree.

### Uniform size

Writing `X=D-j+1` in the probability measure above gives

```math
\eta^2\frac{S_{j-1}}{S_j}\operatorname{Var}(D) = \eta^2j\frac{\operatorname{Var}X}{EX}.
```

Since `0\le X\le D_\kappa-j+1`,

```math
\boxed{ \|Z_\kappa\|^2 \le\frac{\eta^2(D_\kappa+1)^2}{4}. } \tag{15}
```

### A complete small example

For tuple lengths `(2,2,0)`, unit weights and `\eta=1/3`,

```math
G_{\mathrm{cyc}} = \operatorname{diag}(3,4/9,8/81).
```

The relative leakage operator and the raw leakage Gram are respectively

```math
\boxed{ Z^\dagger Z=\operatorname{diag}(0,2/27,0), }
```

```math
\boxed{ Z^*G_{\mathrm{tensor}}Z =\operatorname{diag}(0,8/243,0). }
```

Both describe the same map, through the displayed cyclic metric.

## 2.1 The entire adjoint-stable enlargement is known

For each distinct retained length `D`, let `1_D` be the vector supported on exactly those tuple factors of length `D`. Then

```math
\boxed{ \mathscr W_\kappa = \bigoplus_{D:W_{\kappa,D}>0} \operatorname{span}\{R^j1_D:0\le j\le D\}. } \tag{16}
```

This is the smallest subspace containing the original cyclic image and invariant under both the action and its adjoint.

The proof gives the projectors, rather than merely counting dimensions. The actual Casimir

```math
\mathfrak C=H^2+2H+4EF
```

acts on a length-`D` chain by `D(D+2)`. Hence

```math
\prod_{D'\ne D} \frac{\mathfrak C-D'(D'+2)I} {D(D+2)-D'(D'+2)} \tag{17}
```

extracts `1_D` from the original cyclic constant vector. All denominators are nonzero integers. Multiplication by `R` supplies its whole chain.

The enlargement has dimension

```math
\sum_D(D+1),
```

not the sum of the dimensions of all ordered tuple factors separately.

Its exact projection back to the original cyclic coordinates is

```math
\boxed{ v_{\kappa,j} = \frac{ \sum_DW_{\kappa,D}\binom Dj\,u_{D,j} }{ S_{\kappa,j} }. } \tag{18}
```

The kernel consists of the corresponding full weighted relations at each level.

This is a direct control of the unequal-length mixing: its rank, norm, generated subspace, and return map are all calculated.

---

# 3. The whole positive-trace error is controlled without a sum-gap assumption

Put

```math
d_\kappa=2\Re\kappa-k, \qquad \mathcal L_k=\sum_\kappa(D_\kappa+1)(d_\kappa)_+.
```

This is the original algebraic aggregate.

In the metric (10), the arithmetic weight at `\kappa` is

```math
d_\kappa I+\eta J_\kappa,
```

where `J_\kappa` is the explicit real Jacobi matrix with entries

```math
(J_\kappa)_{j+1,j} = (j+1)\sqrt{\frac{S_{\kappa,j+1}}{S_{\kappa,j}}}.
```

Its spectrum is symmetric, and

```math
\|J_\kappa\|\le D_\kappa.
```

For each positive eigenvalue `\lambda_{\kappa,l}` of `J_\kappa`, use the elementary identity

```math
(a+s)_++(a-s)_+-2a_+=(s-|a|)_+.
```

Summing the actual pairs proves

```math
\boxed{ \operatorname{Tr}(A_{\mathrm{cyc}}+A_{\mathrm{cyc}}^\dagger-kI)_+ -\mathcal L_k = \sum_{\kappa,l} (\eta\lambda_{\kappa,l}-|d_\kappa|)_+. } \tag{19}
```

This includes arbitrarily small displacements, critical sum centres, unequal lengths and exact collisions. Therefore

```math
\boxed{ 0\le \operatorname{Tr}(A_{\mathrm{cyc}}+A_{\mathrm{cyc}}^\dagger-kI)_+ -\mathcal L_k \le \frac{q\eta D_*}{2}, \qquad D_*=\max_\kappa D_\kappa. } \tag{20}
```

The explicit choice

```math
\boxed{ \eta= \min\left\{1,\frac{2t_*}{q(D_*+1)}\right\} } \tag{21}
```

makes the excess at most `t_*`. There is no inverse sum-centre separation in this estimate.

## 3.1 The original odd quartet attains the aggregate exactly

For a common multiplicity `m`, put

```math
D=k(m-1),\qquad q=(D+1)(k+1)^2.
```

The ordered tuple count at `(a,b)` is

```math
\binom ka\binom kb.
```

All its lengths are `D`, so (13) is zero and no adjoint enlargement is needed.

The exact weight spectrum is

```math
\boxed{ 2(2a-k)\delta+\eta(D-2j), \qquad 0\le a,b\le k,\quad0\le j\le D. } \tag{22}
```

For `D>0`, choose

```math
\eta=\frac{\delta}{D+1};
```

for `D=0`, the metric has no `\eta`-dependence. Since `k` is odd, each eigenvalue in (22) has the sign of `2a-k`. Thus

```math
\boxed{ \operatorname{Tr}(A_{\mathrm{cyc}}+A_{\mathrm{cyc}}^\dagger-kI)_+ = \frac{\delta q(k+1)}2. } \tag{23}
```

Its positive rank is **`q/2`**. This is not the canonical rank-one positive allowance. The exact operator norm is

```math
2k\delta+\eta D,
```

and the full squared trace is

```math
\boxed{ \operatorname{Tr}(A_{\mathrm{cyc}}+A_{\mathrm{cyc}}^\dagger-kI)^2 = \frac q3 \left[ 4\delta^2k(k+2)+\eta^2D(D+2) \right]. } \tag{24}
```

For comparison, a common critical two-root packet has the fully evaluated residual

```math
\boxed{ (k+1)\eta \left\lfloor\frac{(D+1)^2}{4}\right\rfloor. } \tag{25}
```

It is positive at finite `\eta>0` when `D>0`, and decreases at the displayed rate. The nilpotent algebra has not been replaced by its reduced roots.

---

# 4. These metrics are realized by actual finite tensor-source sections

This is where the family control acquires a source interpretation.

For a fixed one-factor divisor `h` of degree `d`, use the original polynomial source at degree

```math
n_0=2d-1.
```

Let `H` be its original Gram, `J` its remainder map, and

```math
G_0=(JH^{-1}J^*)^{-1}, \qquad R_0=H^{-1}J^*G_0.
```

Let `B` contain the **full** relation columns

```math
h,sh,\ldots,s^{d-1}h,
```

and put

```math
S=B^*HB,\qquad W=BS^{-1/2}.
```

Then

```math
JR_0=I,\quad JW=0,\quad R_0^*HW=0,\quad W^*HW=I.
```

Let `T_\eta` be the one-factor polynomial metric from (3), returned through the Hermite map (2). Put

```math
d_*=\max_\rho(m_\rho-1),
```

```math
\Lambda_h= 1+\|T_1^{-1/2}G_0T_1^{-1/2}\|, \qquad \tau_\eta=\Lambda_h\eta^{-2d_*}.
```

Since

```math
T_\eta\succeq\eta^{2d_*}T_1,
```

we have

```math
\tau_\eta T_\eta-G_0\succeq T_1>0.
```

The actual source section is

```math
\boxed{ R_\eta= R_0+W(\tau_\eta T_\eta-G_0)^{1/2}. } \tag{26}
```

Direct multiplication proves

```math
\boxed{ JR_\eta=I,\qquad R_\eta^*HR_\eta=\tau_\eta T_\eta. } \tag{27}
```

The factor `\tau_\eta` is the norm of the changed representative; the original measure has not been rescaled.

Tensor these sections and apply the original cyclic substitution:

```math
\boxed{ \mathcal R_{k,\eta} = (\mathcal A_{h_1}R_{1,\eta}\otimes\cdots\otimes \mathcal A_{h_k}R_{k,\eta})\beta. } \tag{28}
```

Its physical injection is still

```math
(U_1\otimes\cdots\otimes U_k)\beta.
```

Its degree in variable `i` is at most `2d_i-1`, so

```math
\boxed{ \deg_{\mathrm{total}}\mathcal R_{k,\eta} \le\sum_i(2d_i-1). } \tag{29}
```

Its complete metric is

```math
\boxed{ \mathcal R_{k,\eta}^*\mathcal R_{k,\eta} = \left(\prod_i\tau_{i,\eta}\right)G_{k,\eta}. } \tag{30}
```

For a fixed `h`,

```math
q_k\le(kd_*+1)\binom{k+r-1}{r-1}, \qquad r=|Z|.
```

This follows by counting occupation vectors; collisions only reduce the number of distinct centres.

Combining this with (21) gives the family bounds (1), and also

```math
\boxed{ \log^+\|\mathcal R_{k,t_*}\|_{G_{k,1}\to\mathrm{physical}} \le C_hk[\log(k+2)+\log^+(1/t_*)]. } \tag{31}
```

On compact one-factor coefficient charts with retained root separation, positive source margins and nonzero unit constants, `C_h` is uniform. **No separation of the** **`k`****-fold sum centres is required.**

## 4.1 The entire physical action defect is retained

Write the actual one-factor decomposition as

```math
D_i\mathscr R_i-\mathscr R_iA_i = \mathscr R_iC_i+N_i, \qquad \mathscr R_i^*N_i=0,
```

where `\mathscr R_i=\mathcal A_{h_i}R_{i,\eta}`.

Let `C_\Sigma=\sum_iC_i` on the ordered tensor space, and let

```math
L_i=(\mathscr R_i^*\mathscr R_i)^{-1}N_i^*N_i.
```

On the cyclic image, put

```math
C_{\mathrm{cyc}}=\beta^\dagger C_\Sigma\beta, \qquad Z_C=(I-\Pi_\beta)C_\Sigma\beta.
```

The full physical defect

```math
\mathfrak D = D_{\mathrm{tot}}\mathcal R_{k,\eta} -\mathcal R_{k,\eta}A_{\mathrm{cyc}}
```

has the exact squared operator

```math
\boxed{ \mathfrak D^\dagger\mathfrak D = C_{\mathrm{cyc}}^\dagger C_{\mathrm{cyc}} +Z_C^\dagger Z_C +\beta^\dagger\left(\sum_iL_i\right)\beta. } \tag{32}
```

External normal terms in different slots are orthogonal because one factor is `\mathscr R_i^*N_i=0`. The terms `C_i^\dagger C_j` are **not** dropped: they occur inside `C_\Sigma^\dagger C_\Sigma`, before its cyclic and normal decomposition.

Let `s_i` be the actual finite norm of one-factor multiplication by `s` between degrees `2d_i-1` and `2d_i`, and put

```math
a_i=\max_{\rho\in Z_i}|\rho|+\eta(d_{i,*}+1)/2.
```

Then

```math
\boxed{ \|\mathfrak D\|^2 \le \left(\sum_i(s_i+a_i)\right)^2+\sum_i s_i^2. } \tag{33}
```

For a fixed packet, this is `O_h(k^2)`.

On the odd common-multiplicity quartet, the original integration-by-parts identity gives

```math
C_{\mathrm{cyc}}+C_{\mathrm{cyc}}^\dagger = kI-A_{\mathrm{cyc}}-A_{\mathrm{cyc}}^\dagger.
```

Using (22)–(24),

```math
\boxed{ \operatorname{rank}\mathfrak D\ge q/2, \qquad k\delta+\eta D/2\le\|\mathfrak D\|\le C_hk. } \tag{34}
```

Also

```math
\boxed{ \|\mathfrak D\|_{\mathrm{HS}}^2 \ge q\left[ \frac{\delta^2k(k+2)}3+ \frac{\eta^2D(D+2)}{12} \right]. } \tag{35}
```

The source family therefore has a controlled order-`k` operator defect, but necessarily many defect directions. Equations (23) and (34) show why that operator norm cannot be inserted as the original canonical rank-two positive-trace allowance.

## 4.2 The exact return to the original scalar-source minimum

The source in (28) is in the original **ordered tensor theta source**. It need not lie in the narrower space of scalar polynomials in `D_1+\cdots+D_k` of the original cutoff.

Let `B_X` be the original scalar-source coefficient map, with full Gram `H_X`, quotient map `J_N`, and canonical metric `G_N`. Put

```math
C_X=B_X^*\mathcal R_{k,\eta}.
```

Its complete orthogonal normal Gram and value map are

```math
H_Z= \mathcal R_{k,\eta}^*\mathcal R_{k,\eta} -C_X^*H_X^{-1}C_X,
```

```math
F_Z=I-J_NH_X^{-1}C_X. \tag{36}
```

The actual equality of source representatives proves

```math
\ker H_Z\subset\ker F_Z.
```

The full minimum on the physical sum of the two sources is therefore

```math
\boxed{ G_N^{\mathrm{joint}} = \left[ G_N^{-1}+F_ZH_Z^+F_Z^* \right]^{-1}. } \tag{37}
```

Here `H_Z^+` is the inverse on its positive range and zero on its actual kernel.

The exact determinant return is

```math
\boxed{ \log\det G_N-\log\det G_N^{\mathrm{joint}} = \log\det\left[ I+G_N^{1/2}F_ZH_Z^+F_Z^*G_N^{1/2} \right]. } \tag{38}
```

Every entry of `C_X` is a finite original-moment expression. In coefficient form it is obtained from

```math
n![t^n]\sum_\alpha\beta_{\alpha,v} \prod_i \left( \sum_{j=0}^N \frac{t^j}{j!} \langle s^j,R_ie_{\alpha_i}\rangle_{w_{h_i}} \right). \tag{39}
```

This is the full multinomial source expansion, with its complex pairings.

Equation (38), not an asserted equality `G_N=G_{k,\eta}`, is the receiver for the new family.

---

# 5. Every restriction and full quotient has controlled mixing

Set `x=\eta^2`. In a fixed original coefficient chart, the constructed metric has the form

```math
G(x)=C^*\operatorname{diag}(a_ix^{n_i})C, \qquad a_i>0,\quad0\le n_i\le D_*.
```

For any specified inclusion `X` of rank `r`,

```math
\boxed{ \det(X^*G(x)X) = \sum_{|I|=r} |\det(CX)_I|^2 \left(\prod_{i\in I}a_i\right) x^{\sum_{i\in I}n_i}. } \tag{40}
```

All phases occur inside the full minors. They have not been removed from the Gram.

Let `R_l` be the rank of the actual rows of `CX` of weight at most `l`. The leading exponent is exactly

```math
\boxed{ m_X=\sum_{l=0}^{D_*-1}(r-R_l). } \tag{41}
```

A basis obtained by successively extending these nested row spaces attains that weight; every basis has at most `R_l` rows below level `l`.

Writing

```math
\det(X^*GX)=x^{m_X}(a_{X,0}+a_{X,1}x+\cdots),
```

with `a_{X,0}>0`, and `A_X=\sum_{j\ge1}a_{X,j}`, gives the finite bound

```math
\boxed{ 0\le \log\det(X^*GX)-m_X\log x-\log a_{X,0} \le \log\left(1+\frac{A_X}{a_{X,0}}x\right). } \tag{42}
```

For an original relation inclusion `B` and specified value lift `L`, retain the entire minimum

```math
K=L^*GL-L^*GB(B^*GB)^{-1}B^*GL.
```

Its exact determinant is

```math
\boxed{ \det K = \frac{\det([B,L]^*G[B,L])}{\det(B^*GB)}. } \tag{43}
```

Thus its leading exponent, coefficient and finite remainder are differences of the explicitly specified quantities in (40)–(42). At four endpoints the signs act on those complete expressions; they do not make the positive errors independently selectable.

## 5.1 The full projection derivative keeps the complex cross terms

For a fixed actual kernel inclusion `B`, put

```math
P=B(B^*GB)^{-1}B^*G, \qquad \Omega=G(I-P).
```

With a dot denoting `d/d\log x`,

```math
\boxed{ \dot P=PG^{-1}\dot G(I-P), \qquad \|\dot P\|_G\le D_*/2. } \tag{44}
```

The observed and kernel forms have different, explicitly related derivatives:

```math
\boxed{ \dot\Omega=(I-P)^*\dot G(I-P), }
```

```math
\boxed{ \frac{d}{d\log x}(GP) = P^*\dot GP+ P^*\dot G(I-P)+(I-P)^*\dot GP. } \tag{45}
```

The last two terms are the complete kernel mixing. For any original three columns `V`,

```math
0\preceq V^*\dot\Omega V \preceq D_*V^*\Omega V. \tag{46}
```

This controls one full positive semidefinite three-by-three error matrix, including its determinant constraint, rather than three unrelated complex errors.

When the subspace itself moves, its contribution is explicit too. Define

```math
\nabla=\frac d{dt}+\frac12G^{-1}G'.
```

This is a metric-compatible finite connection by direct substitution. With

```math
\mathcal S= (I-P)\left(B'+\tfrac12G^{-1}G'B\right) (B^*GB)^{-1}B^*G,
```

one has

```math
\boxed{\nabla P=\mathcal S+\mathcal S^{\dagger_G}.} \tag{47}
```

Thus a varying period, unit, or kernel frame contributes its actual `B'` term.

For several scales, the full curvature of this specified connection is

```math
\boxed{ \mathcal F_{\nabla,ij} = -\frac14 [G^{-1}\partial_iG,G^{-1}\partial_jG]. } \tag{48}
```

For fixed coefficient matrices, its norm is bounded by one eighth the product of the two retained exponent ranges.

These are concrete parameter-control formulas. They do not identify this constructed metric connection with a Gauss–Manin connection.

---

# 6. Sum-centre collisions have complete singular-value exponents

Take two labelled channels of lengths `e\ge f`, at `\kappa_0` and `\kappa_0+z`. Retain the constant-degree polynomial family

```math
\overline E_z = \mathbb C[S]\big/ \bigl[(S-\kappa_0)^e(S-\kappa_0-z)^f\bigr].
```

Its actual observation is the pair of full divided jets.

At `z=0`,

```math
\boxed{ \ker\operatorname{ev}_0 = (u^e)/(u^{e+f}), \qquad \dim\ker\operatorname{ev}_0=f, } \tag{49}
```

where `u=S-\kappa_0`.

In the original translated polynomial basis, bounded invertible row operations reduce the evaluation to

```math
\operatorname{diag}(I_e,B_z),
```

```math
(B_z)_{j,c} = \binom{e+c}{j}z^{e+c-j}, \qquad0\le j,c<f.
```

For an `r\times r` minor, the least exponent is

```math
r(e-f+r).
```

Its coefficient is nonzero: choosing the lowest columns and highest rows reduces it to a falling-factorial Vandermonde. Consecutive determinantal orders therefore give all the collapsing singular scales:

```math
\boxed{ |z|^{e-f+1},\ |z|^{e-f+3},\ldots,|z|^{e+f-1}. } \tag{50}
```

The other `e` singular values stay of order one in any retained positive output metric extending to the collision.

For inverse exterior rank `r`, put `p=\min(r,f)`. Its exact divergence exponent is

```math
\boxed{p(e+f-p).} \tag{51}
```

The full determinant has exponent `ef`, agreeing with

```math
\det(E_z^*W_zE_z)=|z|^{2ef}\det W_z.
```

For simultaneous `\eta=|z|^a`, the exponents are determined by the finite list

```math
\min_{I,J} \left[ \sum_{i\in I}a\,j_i+ \operatorname{ord}_z\det(E_z)_{I,J} \right]. \tag{52}
```

There is no cancellation between the squared minors. The resulting exponents are piecewise linear in `a`, with computable breakpoints.

## 6.1 Relate the lost flat directions to adjoint mixing

For `e>f`, the collision’s two top chains are

```math
\mathscr T=E_e\oplus E_f, \qquad E_r=\mathbb C[u]/u^r.
```

The exact sequence is

```math
\boxed{ 0\longrightarrow E_e \xrightarrow{p\mapsto(p,p\bmod u^f)} \mathscr T \xrightarrow{(p,q)\mapsto q-p\bmod u^f} E_f\longrightarrow0. } \tag{53}
```

The flat kernel in (49) maps to the last term by `u^ea\mapsto a`, with inverse `a\mapsto u^ea`. All maps commute with multiplication by `u`.

The adjoint leakage has rank exactly `f`, and its reducing enlargement is all of `\mathscr T`, by (14)–(16). The quotient metric at level `j<f`, with the two original weights denoted `a_j,b_j`, is

```math
\boxed{ \|z_j\|_{\mathrm{quot}}^2 =\frac{a_jb_j}{a_j+b_j}|z_j|^2, }
```

with exact minimum representative

```math
\left( -\frac{b_j}{a_j+b_j}z_j,\ \frac{a_j}{a_j+b_j}z_j \right). \tag{54}
```

For `e=f`, the diagonal image is already reducing, so its adjoint leakage is zero, while the flat observation still loses `e` directions. The independent difference channel is not generated by applying the common action and adjoint to the diagonal. Equations (49) and (53) retain that case rather than assigning a generic recovery statement.

---

# 7. The constructed general families also have controlled heat actions

Let

```math
M=(A_{\mathrm{cyc}}-kI/2)/i.
```

In the explicit orthonormal jet frame, write `M=Z+N`, where `Z` is block scalar at

```math
\alpha_\kappa=(\kappa-k/2)/i.
```

The complete nilpotent part satisfies

```math
\|N\|\le\eta(D_*+1)/2.
```

For every heat time `t\ge0`,

```math
\boxed{ \frac1q\operatorname{Tr}e^{-t(M/k)^2} = \frac1q\sum_\kappa(D_\kappa+1) e^{-t(\alpha_\kappa/k)^2}. } \tag{55}
```

The full operator still contains all its confluent derivatives; only their strictly triangular trace contributions vanish.

Put

```math
R_k=\max_\kappa|\alpha_\kappa|/k, \qquad e_k=\eta(D_*+1)/(2k).
```

The genuine metric heat action obeys

```math
\boxed{ \left| \frac1q\operatorname{Tr}e^{-tM^\dagger M/k^2} -\frac1q\sum_\kappa(D_\kappa+1)e^{-t|\alpha_\kappa/k|^2} \right| \le t(2R_ke_k+e_k^2). } \tag{56}
```

This is the exact Duhamel estimate between two positive squared operators. With `\eta=\tau/(D_*+1)`, it is `O(1/k)` uniformly on bounded heat-time intervals, for unequal multiplicities and all actual sum collisions.

## 7.1 The common quartet limit is evaluated

For the original common-multiplicity quartet,

```math
\mathcal H_k(t) = \frac1{(k+1)^2} \sum_{a,b=0}^k e^{-t[\gamma(2b/k-1)-i\delta(2a/k-1)]^2}.
```

It converges, with an explicit `O(1/k)` error, to

```math
\mathcal H_\infty(t) = \frac1{4\delta\gamma} \int_{-\gamma}^{\gamma}\int_{-\delta}^{\delta} e^{-t(x-iy)^2}\,dy\,dx.
```

For `t>0`, define

```math
J_t(z)= \frac{\sqrt\pi}{2\sqrt t}\, z\,\operatorname{erf}(\sqrt t\,z) +\frac{e^{-tz^2}}{2t}.
```

Since `J_t''(z)=e^{-tz^2}`,

```math
\boxed{ \mathcal H_\infty(t) = \frac{\Im J_t(\gamma+i\delta)}{\gamma\delta}. } \tag{57}
```

The full metric heat limit is

```math
\boxed{ \mathcal K_\infty(t) = \frac{\pi}{4t\delta\gamma} \operatorname{erf}(\gamma\sqrt t) \operatorname{erf}(\delta\sqrt t). } \tag{58}
```

Both extend to value one at `t=0`.

Their evaluated difference starts as

```math
\boxed{ \mathcal H_\infty(t)-\mathcal K_\infty(t) = \frac{2\delta^2}{3}t -\frac{4\gamma^2\delta^2}{9}t^2 +O_{\delta,\gamma}(t^3). } \tag{59}
```

The finite quadratic identity is stronger than this local expansion:

```math
\boxed{ \frac{ \operatorname{Tr}(M^\dagger M)-\Re\operatorname{Tr}M^2 }{qk^2} = \frac{2\delta^2(k+2)}{3k} +\frac{\eta^2D(D+2)}{6k^2}. } \tag{60}
```

It is exactly one half of the normalized squared weight (24). Thus the two trace actions are connected by the calculated metric term, not by an asserted equality.

---

# 8. What the Deligne/BBT-style control amounts to here

There are now explicit answers to the family questions that were previously left as broad “mixing” issues.

The full tensor metric is (10). Unequal primary lengths contribute precisely the variance (13), with exact rank (14). The required adjoint-stable enlargement and its return are (16)–(18). The entire positive-trace excess is (19), with the separation-free tolerance (20)–(21). Actual finite tensor-source sections realize those metrics with the family costs (29)–(31), and their full action defect is (32).

For each fixed degree, the coefficient equations, positive-square-root graph, rank strata and minors give a finite algebraic description. On compact off-axis one-factor parameter charts, the original moment map

```math
(\rho_a)\longmapsto \int \overline{s}^{\,i}s^j \frac{|2\xi(s)|^2}{2\pi|h(s)|^2}\,dy, \qquad s=\frac12+iy,
```

is real analytic with explicit Cauchy bounds: the denominator remains uniformly separated from zero on the line. The proof package gives the bounds and the exact Hermite inverse estimates.

That compact estimate is **not** extended across a critical-line denominator by fiat. At an actual complete divisor, the original removable values of `2\xi/h` must be used. The finite collision maps in (49)–(54) keep the corresponding kernel and higher jets explicit.

The number of possible sum-collision strata may grow with `k`. The family estimates above do not require a `k`-independent enumeration of those strata.

The remaining original native quantities are still

```math
\mathcal R\log\det(I_K^*G_NI_K),
```

```math
\mathcal M^p = \mathcal R\log\det \left[(Q_N^p)^{-1/2}H_N^p(Q_N^p)^{-1/2}\right],
```

and the actual signed projected-current values. The new family enters those calculations through the complete cross Gram and minimum in (36)–(39). It does not assign their values merely by controlling a different metric.

The package contains the complete proofs, the exact auxiliary checker, separately labelled non-interval diagnostics, and its [machine-generated execution report](sandbox:/mnt/data/Programme_General_Families_20260920/state/VERIFICATION.json). The numerical examples are coefficient-family tests, not evaluations of an unspecified xi packet or period.

**The substantive advance is that “control the general family” is now a collection of explicit, uniform calculations: no sum-centre gap is needed for the positive-trace tolerance; every unequal-length adjoint term is known; every added source direction has a retained metric and normal defect; and every return to the original scalar source keeps the full mixed minimum. The still-uncomputed native orientation is isolated in that last receiver rather than hidden inside an appeal to general machinery.**