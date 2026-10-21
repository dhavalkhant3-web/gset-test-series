# November 2025 Mathematical Sciences — source comparison, Questions 1–10

**Official question paper:** https://gujaratset.ac.in/assets/papers/paperII/nov25/nov2501.pdf  
**Official final answer key:** https://gujaratset.ac.in/assets/anskey/paperII/nov25/nov2501.pdf  
**Scope:** This is a first-batch source comparison of printed questions 1–10 against the recovered archive. The official PDF was parsed for this review; OCR/extraction itself has visible errors in some mathematical glyphs, so the report does not clear any record as verified.

## Official answer labels (Q1–Q10)

The official final answer key gives: Q1 B, Q2 B, Q3 A, Q4 B, Q5 D, Q6 B, Q7 D, Q8 D, Q9 C, Q10 C. The key states that a question with answer `Z` is not evaluated; none of Q1–Q10 is marked Z.

## Comparison against recovered records

| Printed Q.No. | Recovered record | Finding from source comparison | Answer-key check | Status |
|---:|---|---|---|---|
| 1 | `mathematical_sciences_nov25_q1` | Recovered text is garbled and appears to be an unrelated integral-equation question; official Q1 is the piecewise function involving (x^2\sin(1/x)) at (x=0). | Archive B = official B, but text does not match. | FAIL — wording/options wrong |
| 2 | `mathematical_sciences_nov25_q2` | Recovered text is OCR-corrupted and resembles unrelated/instruction text; official Q2 concerns countability of roots of integer-coefficient polynomials and functions from natural numbers to ({0,1,2}). | Archive B = official B, but text does not match. | FAIL — wording/options wrong |
| 3 | `mathematical_sciences_nov25_q3` | Recovered text is examination instructions, not printed Q3. Official Q3 asks about lim sup and lim inf of a sequence; extraction has some exponents/parity symbols unclear, so inspect the rendered page before transcribing its expression. | Archive A = official A, but text does not match. | FAIL — wrong question |
| 4 | `mathematical_sciences_nov25_q4` | Recovered text resembles official Q1, not printed Q4. Official Q4 is an improper integral (int_3^infty dx/(x^2+x-2)). | Archive B = official B by coincidence; question is misaligned. | FAIL — question number alignment |
| 5 | `mathematical_sciences_nov25_q5` | Recovered text is examination instructions, not printed Q5. Official Q5 defines a piecewise function (g), a parity-dependent sequence (f_n), and asks for (liminf f_n(x)) and a limit of integrals. | Archive D = official D, but text does not match. | FAIL — wrong question |
| 6 | No recovered record | Official Q6 asks for the directional rate of change of (f(x,y)=ye^x) at (P(0,2)) in the direction of (Q(2,1/2)). Need transcribe all options directly from PDF; do not reconstruct a missing bank record from this summary. | Official B. | MISSING |
| 7 | `mathematical_sciences_nov25_q7` | Recovered text is garbled/unrelated. Official Q7 concerns compact subsets of (mathbb R) under the discrete metric. | Archive D = official D, but text does not match. | FAIL — wording/options wrong |
| 8 | `mathematical_sciences_nov25_q8` | Recovered text partially resembles official Q8 about (O_n=(-1/n,1+1/n]) and their intersection, but the interval/brackets and expression are corrupted. Four options require source-page review. | Archive D = official D. | HOLD — notation/options not verified |
| 9 | `mathematical_sciences_nov25_q9` | Recovered text broadly resembles official Q9 on a subspace topology, but symbols and options are incomplete; compare every option to the printed PDF. | Archive C = official C. | HOLD — options not verified |
| 10 | `mathematical_sciences_nov25_q10` | Recovered text broadly resembles official Q10 about a topology defined using distinguished points (p,q); OCR has corrupted set notation and the options need exact comparison. | Archive C = official C. | HOLD — notation/options not verified |

## Result of this batch

- Questions reviewed against the official PDF: 10 printed question numbers.
- Clear record-level mismatches: Q1–Q5 and Q7; Q4 is also misaligned by printed question number.
- Missing in recovered archive: Q6.
- Partial text match but not yet safe to clear: Q8–Q10.
- **Records cleared as verified: 0.** Even where answer labels match, that does not validate the text or options.

## Required next pass

1. Inspect the rendered official PDF page images for Q3, Q5, Q6 and Q8–Q10 to confirm exact notation and every option.
2. Transcribe from source, preserving formulas and set notation; do not copy OCR output where it is visibly corrupted.
3. Compare Q11–Q20 next, then continue in printed question-number order.
4. Keep all affected records `review_flag: true` and `source_verified: false` until the complete question/options/figure/key comparison passes.

**Release decision: BLOCKED.** This batch found concrete OCR/order failures and is not permission to import the recovered archive into production.
