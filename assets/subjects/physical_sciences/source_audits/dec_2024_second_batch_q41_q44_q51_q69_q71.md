# December 2024 Physical Sciences — Second-batch source verification

Date: 2026-11-13
Branch: integration/combined-subject-banks
Uploaded official original question paper: `dec2402.pdf` (32 pages)
Uploaded official final answer key: `dec2402 (1).pdf` (1 page)

Official source URLs:
- Question paper: https://www.gujaratset.ac.in/assets/papers/paperII/dec24/dec2402.pdf
- Final answer key: https://www.gujaratset.ac.in/assets/anskey/paperII/dec24/dec2402.pdf

The page numbers below refer to the 32-page uploaded PDF (1-based). Official key letters were checked against the uploaded final-key table. No official key letter has been altered.

| Q | PDF page | Original printed content / options | Independent calculation / scientific check | Official key | Decision |
|---|---:|---|---|---|---|
| 41 | 16 | Spin-1/2 fermion in state [2, 1−i]ᵀ; options A 2ℏ, B ℏ/2, C ℏ, D 3ℏ/2. | Norm²=|2|²+|1−i|²=6. ⟨σx⟩=2Re(a* b)/6=4/6=2/3; ⟨Sx⟩=(ℏ/2)(2/3)=ℏ/3. No option equals ℏ/3. The canonical explanation previously used norm²=4 and got ℏ/2; that was incorrect and has been corrected. | A | Retain flag: no listed option equals the independently calculated ℏ/3; official A=2ℏ remains unchanged. |
| 44 | 17 | V(x)=½mω²x² for x>0 and V(x)=∞ for x≤0. ψ=−ψ₀/√5+2ψ₁/√5; ψ₀, ψ₁ are ground and first-excited eigenstates. Options A 31ℏω/10, B 11ℏω/10, C 13ℏω/10, D 25ℏω/10. | This is a half-harmonic oscillator with a hard wall at x=0. Allowed states correspond to odd-parity full-oscillator states: E₀=3ℏω/2, E₁=7ℏω/2. ⟨E⟩=(1/5)E₀+(4/5)E₁=31ℏω/10, option A. | A | Cleared. Source transcription in canonical bank corrected from α to ∞; corrected derivation matches official A. |
| 51 | 19 | “The entropy of a system always increases when it undergoes an irreversible process” (A); B says always decreases; C says second law follows from energy conservation; D says ideal-gas internal energy does not depend on temperature. | The second law guarantees entropy increase for an isolated system / total system plus surroundings. Entropy of the system alone can decrease if it exports entropy. The stem does not say isolated system. A is only valid under an unstated condition. | A | Retain flag: wording is overbroad unless “isolated system” is understood. |
| 69 | 23 | Silicon photodiode responsivity 0.67 A/W; measured photocurrent printed as 0.0134 mA; options A 10 mW, B 20 mW, C 40 mW, D 80 mW. | P=I/R=(0.0134 mA)/(0.67 A/W)=2.0×10⁻⁵ W=0.020 mW=20 μW, which is not listed. Option B=20 mW would require I=13.4 mA, a factor 1000 larger than printed. | B | Retain flag: printed current unit/value and keyed option differ by ×1000. |
| 71 | 24 | Emission transition ¹D₂→¹F₃, λ=3122 Å; asks population ratio at 5000 K. Options A 4.02×10⁻⁵, B 2.03×10⁻⁵, C 9.83×10⁻⁵, D 7.02×10⁻⁵. | Single-state Boltzmann factor exp[−hc/(λkBT)]=exp(−9.2276)=9.83×10⁻⁵, option C. If total fine-structure level populations include statistical-weight ratio (2J_f+1)/(2J_i+1)=7/5, the result becomes 1.38×10⁻⁴, absent from options. The question does not state whether degeneracy is included. | C | Corrected the canonical bank's incorrect hydrogen n=3→2 stem/options to the actual official scan. Retain flag only for the statistical-weight convention ambiguity; official C is preserved. |

## Data changes committed

- Q41 explanation corrected: norm² is 6 and ⟨Sx⟩=ℏ/3; flag remains.
- Q44 stem corrected to the printed infinite-wall condition; explanation corrected; expert flag cleared.
- Q71 question/options corrected to the printed ¹D₂→¹F₃ transition and actual four options; explanation recalculated; flag retained for the degeneracy convention.
- Q51 and Q69 remain flagged with the source-supported reasons above.
- December 2024 expert/content flags reduced from 15 to 14. Across the 22-flag review started on 2026-11-13, 8 have now been cleared (7 in the earlier batch plus Q44).
- Official answer-key letters unchanged; canonical answer parity is intended to remain 100/100.
- Other subjects and Paper-I untouched. No PR merge, CI run, or Combined APK build performed.
