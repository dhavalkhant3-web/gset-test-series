# December 2024 Physical Sciences — First-batch source verification

Date: 2026-11-13
Branch: integration/combined-subject-banks
Source paper: https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2402.pdf
Official final key: https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2402.pdf

This is a question-level source audit. The official final key is recorded as published and is not altered.

| Q | Printed question / options verified from official PDF | Independent finding | Official key | Decision |
|---|---|---|---|---|
| 06 | Page containing Q06: solve z²+2z+1=0; options A −1+i, B −1+2i, C 2+i, D 1+2i. | (z+1)²=0, so the only root is z=−1. Its imaginary part is zero; none of the four options satisfies the equation and the nonzero-real/nonzero-imaginary condition. | B | Retain flag: defective item/options or key. No option is mathematically valid. |
| 09 | Q09: residue of 4z²/[(z¹¹+2)(z−1)] at simple pole z=1; options 0, 3/4, 1, 4/3. | Res = lim(z→1)(z−1)f(z)=4/(1+2)=4/3, option D. | B (3/4) | Retain flag: direct residue conflicts with final key. |
| 11 | Q11 asks the transformation law of a covariant tensor; options include inverse Jacobian (A), Jacobian (B), no transformation (C), covariant vector (D). | With the standard convention x′=x′(x), a covariant rank-one component transforms as A′μ=(∂xν/∂x′μ)Aν: inverse Jacobian. A is the standard answer. | B | Source/math resolves the earlier ambiguity: explanation should state the coordinate convention and identify A. The final-key B conflicts. Keep a discrepancy flag until the canonical record is safely updated. |
| 18 | Q18 asks the two-body centre-of-mass velocity; options A 0, B (m₁v₁+m₂v₂)/(m₁+m₂), C (v₁+v₂)/2, D crossed mass/velocity expression. | General formula is v_cm=(m₁v₁+m₂v₂)/(m₁+m₂), option B. Zero is only a special case when total momentum is zero, not stated in the question. | A | Retain flag: general expression conflicts with final key. |
| 28 | Q28 describes a uniformly magnetized circular cylinder of radius R, axis z, M=M₀ z-hat, and asks H(r), B(r) everywhere. Option A says inside r<R: H=0, B=μ₀M₀ z-hat. | For an ideal infinitely long cylinder, end effects vanish and A follows. A finite cylinder has end poles/demagnetizing fields and generally nonuniform internal H/B. The stem gives no length or infinite-cylinder condition, so “everywhere” is under-specified. | A | Retain flag: A is valid only with an unstated infinite-cylinder idealization. |

## First-batch outcome

- Source wording and all four options checked for Q06, Q09, Q11, Q18, Q28 against the official scanned paper.
- Independent calculations/conventions checked.
- Q11's physics is resolved (inverse Jacobian, option A), but its official key says B; preserve discrepancy pending canonical JSON update.
- Q06, Q09, Q18, Q28 remain genuine source/key/statement issues.
- No official answer-key entries changed.
- No other subjects or Paper-I modified.
- No PR merge, CI run, or APK build performed.
