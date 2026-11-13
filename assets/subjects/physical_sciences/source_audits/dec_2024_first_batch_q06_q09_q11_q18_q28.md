# December 2024 Physical Sciences — First-batch source verification

Date: 2026-11-13
Branch: integration/combined-subject-banks

- Uploaded original question paper: `dec2402.pdf` (32 pages).
- Uploaded official final answer key: `dec2402 (1).pdf` (1 page).
- Official paper URL: https://gujaratset.ac.in/assets/papers/paperII/dec24/dec2402.pdf
- Official final key URL: https://gujaratset.ac.in/assets/anskey/paperII/dec24/dec2402.pdf

The question paper was visually inspected at its original scanned pages. PDF page references below are 1-based page numbers in the uploaded 32-page PDF. The final answer key was checked against the uploaded one-page key. The official key is recorded as published and is not altered.

| Q | Original PDF page | Printed question/options checked | Independent finding | Official key | Decision |
|---|---:|---|---|---|---|
| 06 | 9 | “A complex number satisfies … z²+2z+1=0”; options A −1+i, B −1+2i, C 2+i, D 1+2i. | (z+1)²=0, so the only root is z=−1. Its imaginary part is zero. None of the four printed options satisfies the equation; in particular B gives (z+1)²=(2i)²=−4, not 0. | B | Retain flag: no listed option is mathematically valid under the printed stem. |
| 09 | 9 | Residue of f(z)=4z²/[(z¹¹+2)(z−1)] at the simple pole z=1; options A 0, B 3/4, C 1, D 4/3. | Res(f,1)=lim(z→1)(z−1)f(z)=4/(1¹¹+2)=4/3, option D. | B (3/4) | Retain flag: direct residue calculation conflicts with the final key. |
| 11 | 10 | “Which of the following is true for a covariant tensor?” A inverse Jacobian; B Jacobian; C does not transform; D transforms as a covariant vector. | Under the standard convention x′=x′(x), a covariant rank-r tensor transforms with one inverse Jacobian factor per lower index: T′ᵢⱼ…=(∂xᵃ/∂x′ⁱ)(∂xᵇ/∂x′ʲ)…Tₐᵦ…. Thus A is the intended generic rule. D describes the rank-one special case (a covariant vector), not the general tensor transformation law. | B | Retain flag: under the standard stated convention the expected answer is A, not B. The stem does not define the coordinate-map convention explicitly, so record this convention in the explanation; do not alter the official key. |
| 18 | 12 | “In a two body collision problem of two masses m₁ and m₂ moving with velocities v₁ and v₂ respectively, the velocity of the centre of mass is given by”; B is (m₁v₁+m₂v₂)/(m₁+m₂). | From total momentum P=(m₁+m₂)v_cm=m₁v₁+m₂v₂, v_cm=(m₁v₁+m₂v₂)/(m₁+m₂), option B. Option A (zero) holds only in a special zero-total-momentum frame, not stated in the stem. | A | Retain flag: general expression conflicts with the final key. |
| 28 | 14 | Uniformly magnetized circular cylinder, radius R, axis z, M=M₀ z-hat; asks H(r), B(r) everywhere. Option A states for r<R: H=0 and B=μ₀M₀ z-hat. | For an ideal infinitely long cylinder, side bound current K_b=M×n=M₀ φ-hat gives B=μ₀M inside and zero outside; hence H=B/μ₀−M=0 inside. A finite cylinder has end-face magnetic pole density σ_m=M·n=±M₀ and demagnetizing/end fields. The stem does not specify infinite length or length/end geometry. | A | Retain flag as an assumption/wording ambiguity: A is correct for the ideal infinite-cylinder model, but “everywhere” is not uniquely determined for an unspecified finite cylinder. |

## First-batch outcome

- Original scan visually checked: Q06 and Q09 on PDF page 9; Q11 on page 10; Q18 on page 12; Q28 on page 14.
- All four options for each of the five questions were read from the uploaded scan.
- The official final key choices were checked in the uploaded key: Q06 B, Q09 B, Q11 B, Q18 A, Q28 A.
- Independent results: Q06 no valid option; Q09 D; Q11 A under the standard coordinate convention; Q18 B; Q28 A only under the ideal infinite-cylinder assumption.
- All five expert/content flags remain. None is safe to clear by merely editing an explanation.
- No official answer-key entries changed. No canonical question-bank answer letters changed in this batch.
- Other subjects and Paper-I untouched.
- No PR merge, CI run, or Combined APK build performed.
