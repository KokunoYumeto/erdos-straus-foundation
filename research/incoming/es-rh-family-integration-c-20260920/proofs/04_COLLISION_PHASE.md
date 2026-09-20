# 4. Complete two-scale collision exponents

**Basis and status.** GF(49)–(52) supplies the two-centre Hermite matrix, its unweighted collision exponents, and a finite minimum over weighted minors. This section evaluates that minimum for every pair of lengths and every common power-law scale. The result is a complete two-regime formula, not a numerical fit.

## 4.1 Original divided-jet map and metric scale

Let \(e\ge f\ge1\), \(n=e+f\), and retain the constant-degree source
\[
\mathbb C[u]/(u^e(u-z)^f),\qquad z\ne0.
\]
In the unmodified power basis \(1,u,\ldots,u^{n-1}\), the divided-jet evaluation matrix is
\[
(E_z)_{(0,j),m}=\mathbf1_{j=m},\quad 0\le j<e,
\qquad
(E_z)_{(z,j),m}=\binom mjz^{m-j},\quad0\le j<f.
\tag{CP1}
\]
Entries with \(m<j\) are zero. Give the two jet blocks the scale factor \(\eta^j\), with
\[
\eta=|z|^a,\qquad a\ge0.
\]
Fixed positive weights, including the exact \((j!)^2\binom{e-1}j\) and \((j!)^2\binom{f-1}j\) from GF, act through row factors \(\sqrt{c_\alpha}\), one coefficient for each row label \(\alpha\), and do not alter the exponents. The input metric is fixed and uniformly equivalent to the standard power-coordinate metric. After extracting the displayed row powers, the residual target metric is required to remain uniformly positive and uniformly bounded. This qualification does not discard a degenerating metric or a vanishing physical unit.

Let \(\nu_1\le\cdots\le\nu_n\) mean
\(\sigma_j(E_{z,\eta})\asymp |z|^{\nu_j}\), with singular values in decreasing order. Constants may depend on the fixed lengths and the retained fixed metrics, but not on \(z\) sufficiently near zero. All formulas retain the phase of complex \(z\) through unitary row/column factors.

## 4.2 The complete phase diagram

For \(0\le a\le1\), the ordered list is
\[
\boxed{
0,a,2a,\ldots,(e-1)a;
\quad e-f+2j-1+a(f-j),\quad j=1,\ldots,f.
} \tag{CP2}
\]
The semicolon separates the \(e\) first-centre jet directions from the \(f\) additional directions; the entire list is nondecreasing.

For \(a\ge1\), the ordered list is
\[
\boxed{
(a+1)j,\ (a+1)j+1\quad(j=0,\ldots,f-1);
\qquad aj+f\quad(j=f,\ldots,e-1).
} \tag{CP3}
\]
Thus the only change of formula occurs at \(a=1\). At that value, both lists are exactly
\[
\boxed{0,1,2,\ldots,e+f-1.} \tag{CP4}
\]
The determinant order is, in both regimes,
\[
ef+\frac a2\{e(e-1)+f(f-1)\}. \tag{CP5}
\]
At \(a=0\), CP2 reduces to the source's \(e\) zero exponents and \(e-f+1,e-f+3,\ldots,e+f-1\). When \(a>0\), even some of the directions that were bounded in the unweighted map acquire scale; they must not be kept as unweighted zeros.

For example, \((e,f)=(3,2)\) gives
\[
\begin{cases}
(0,a,2a,2+a,4),&0\le a\le1,\\
(0,1,a+1,a+2,2a+2),&a\ge1.
\end{cases}
\]
For \((e,f)=(2,2)\), the two lists are \((0,a,a+1,3)\) and \((0,1,a+1,a+2)\). These are exact specialization cases of the all-length theorem.

## 4.3 Proof for \(0\le a\le1\)

Subtract from the second-centre jet of order \(j\) the first-centre jets of orders \(j,\ldots,e-1\), with their exact Taylor coefficients. After weighting, these row-operation coefficients are constants times \((z/\eta)^{m-j}\). Their magnitudes stay bounded because \(|z|/\eta=|z|^{1-a}\le1\); the inverse row operations are bounded too. The matrix becomes a block diagonal matrix with first block \(\operatorname{diag}(1,\eta,\ldots,\eta^{e-1})\) and second block
\[
C_{j,c}=\eta^j\binom{e+c}{j}z^{e+c-j},\qquad 0\le j,c<f.
\tag{CP6}
\]
A nonzero \(r\)-minor of the second block has order
\[
re+\sum_{c\in J}c+(a-1)\sum_{j\in I}j.
\]
For \(a\le1\), its minimum is attained by columns \(0,\ldots,r-1\) and rows \(f-r,\ldots,f-1\), giving
\[
\mu_r=r(e-f+r)+\frac{ar(2f-r-1)}2. \tag{CP7}
\]
The chosen minor does not vanish. Put \(L=f-r\). Its binomial coefficient determinant is
\[
\frac{\prod_{c=0}^{r-1}(e+c)_{\underline L}}
{\prod_{j=L}^{L+r-1}j!}
\prod_{0\le c<d<r}(d-c)>0.
\tag{CP8}
\]
To see it, factor \((e+c)_{\underline L}\) from each column, then use the falling-factorial polynomials of degrees \(0,\ldots,r-1\), all monic. Their evaluation determinant is the ordinary Vandermonde. Here \(e\ge f\) ensures every retained factor is positive.

The squared Hilbert–Schmidt norm of an exterior matrix is the sum of the squared absolute values of all its minors. The operator and Hilbert–Schmidt norms differ by bounded dimension constants. Thus \(\mu_r\) is the exponent of the product of the largest \(r\) singular values of \(C\). Taking consecutive differences gives
\(e-f+2r-1+a(f-r)\), proving CP2 after adjoining the first block. The first exponent in this second block is larger than \((e-1)a\) by \(e-f+1-a(e-f)\ge1\), so the displayed global ordering is valid.

## 4.4 Proof for \(a\ge1\)

Factor a row power \(|z|^{(a-1)j}\) from each derivative row, and a column power \(|z|^m\) from column \(m\). Removing only unitary phase factors leaves the constant confluent matrix for nodes \(0,1\). Every nonzero \(r\)-minor therefore has order
\[
\sum_{m\in J}m+(a-1)\sum_{j\in I}j.
\]
Because \(a-1\ge0\), choose the smallest \(r\) column orders and the smallest \(r\) derivative orders in the multiset
\(\{0,\ldots,e-1\}\cup\{0,\ldots,f-1\}\).
These rows can be chosen as consecutive initial jet segments at each centre. Their first-\(r\)-column determinant is the divided-jet confluent Vandermonde at \(0,1\), equal to one up to row ordering. It is nonzero. If \(j_r\) is the \(r\)-th element of that ordered derivative multiset, the consecutive determinantal orders give
\[
\nu_r=(r-1)+(a-1)j_r.
\]
The paired values \(j,j\) for \(j<f\), followed by \(j=f,\ldots,e-1\), give CP3. Summing either list proves CP5.

## 4.5 Every inverse exterior rank, and explicit balanced-ray constants

For any \(1\le r\le n\), the inverse exterior divergence exponent is exactly
\[
\boxed{\mathfrak e_r(a)=\sum_{j=n-r+1}^{n}\nu_j(a).} \tag{CP9}
\]
This is a sum of an explicitly evaluated list, not the unresolved minimum over minors from the input. For \(0\le a\le1\) it has the closed form
\[
\mathfrak e_r(a)=
\begin{cases}
r(e+f-r)+ar(r-1)/2,&r\le f,\\
ef+\dfrac a2\{f(f-1)+(r-f)(2e-r+f-1)\},&r>f.
\end{cases} \tag{CP10}
\]
At \(a=0\) this is \(p(e+f-p)\), \(p=\min(r,f)\), exactly the original input formula. At \(a=1\),
\[
\mathfrak e_r(1)=\frac{r(2n-r-1)}2.
\]

There are fully finite constants on this balanced ray. In the standard power-coordinate input metric and the specified jet weights \(c_\alpha>0\), let \(B\) be the constant Hermite evaluation at \(0,1\), with row \(\alpha\) multiplied by \(\sqrt{c_\alpha}\). Then
\[
E_{z,|z|}=U_\phi B\operatorname{diag}(1,z,\ldots,z^{n-1}),
\]
where \(U_\phi\) is a diagonal unitary phase matrix. Define
\[
\beta_B=\operatorname{tr}(B^*B),\qquad
\alpha_B=\frac{\det(B^*B)}{\beta_B^{n-1}}>0.
\]
The determinant is \(\prod c_j\), since the unweighted divided-jet confluent determinant is one at the chosen nodes. The elementary eigenvalue product bound gives \(\alpha_B I\preceq B^*B\preceq\beta_B I\), whence
\[
\boxed{
\beta_B^{-r/2}|z|^{-r(2n-r-1)/2}
\le\|\wedge^rE_{z,|z|}^{-1}\|
\le\alpha_B^{-r/2}|z|^{-r(2n-r-1)/2}.
} \tag{CP11}
\]
A different fixed original input form is inserted by its actual square-root coordinate map \(C\). At inverse exterior rank \(r\), the transported constants use \(\|\wedge^r C\|\) and \(\|\wedge^r C^{-1}\|\), or the coarser bounds \(\|C\|^r\) and \(\|C^{-1}\|^r\); first-exterior norms alone would not control CP11. A common physical section multiplier \(T(z)>0\) multiplies the target Gram and therefore multiplies this inverse-exterior norm by \(T(z)^{-r/2}\). In particular the GF section scalar \(\prod_i\tau_{i,\eta}\) cannot be omitted from a physical comparison. If it is asymptotic to \(c|z|^{-b}\), each singular exponent shifts by \(-b/2\); the relative condition number does not change.

The code independently computes all nonzero exact minors for the stated finite test cases and compares their orders with CP2–CP3 at rational values on both sides of one. The all-length, all-real-\(a\) claim follows from the proofs above. No floating singular-value fitting is used as proof.
