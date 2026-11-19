import 'package:flutter_test/flutter_test.dart';
import 'package:gset_test_series/main.dart';

void main() {
  group('MathAwareText tokenizer', () {
    test('preserves prose around inline TeX', () {
      final parts = MathAwareText.tokenize('Find \\(x^2 + 1\\) for real x.');
      expect(parts.map((part) => part.text).toList(), ['Find ', 'x^2 + 1', ' for real x.']);
      expect(parts.map((part) => part.isMath).toList(), [false, true, false]);
      expect(parts[1].display, isFalse);
    });

    test('recognizes display TeX without swallowing adjacent prose', () {
      final parts = MathAwareText.tokenize('Evaluate \\[\\int_0^1 x^2\\,dx\\] now.');
      expect(parts.map((part) => part.isMath).toList(), [false, true, false]);
      expect(parts[1].display, isTrue);
      expect(parts[1].text, r'\int_0^1 x^2\,dx');
    });

    test('recognizes paired dollar delimiters and leaves unmatched dollar alone', () {
      final parts = MathAwareText.tokenize(r'Let $A=\begin{pmatrix}1&0\\0&1\end{pmatrix}$ then $continue');
      expect(parts.where((part) => part.isMath).length, 1);
      expect(parts.last.text, r' then $continue');
    });

    test('leaves ordinary text and unsupported raw OCR unchanged', () {
      const source = 'Question: f(x)=x2? OCR: ∫_0^1, do not guess.';
      final parts = MathAwareText.tokenize(source);
      expect(parts.length, 1);
      expect(parts.single.isMath, isFalse);
      expect(parts.single.text, source);
    });

    test('does not treat currency-like dollar with no closing delimiter as math', () {
      final parts = MathAwareText.tokenize(r'Price is $5 and no closing marker');
      expect(parts.length, 1);
      expect(parts.single.isMath, isFalse);
    });
  });
}
