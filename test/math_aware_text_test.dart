import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:gset_test_series/main.dart';

Finder richTextContaining(String value) => find.byWidgetPredicate(
      (widget) => widget is RichText && widget.text.toPlainText().contains(value),
    );

void main() {
  group('MathAwareText', () {
    testWidgets('renders ordinary text unchanged', (tester) async {
      await tester.pumpWidget(const MaterialApp(
        home: Scaffold(body: MathAwareText(text: 'GSET Paper-II')),
      ));

      final finder = richTextContaining('GSET Paper-II');
      expect(finder, findsOneWidget);
      expect(tester.widget<RichText>(finder).text.toPlainText(), 'GSET Paper-II');
    });

    testWidgets('keeps unmatched math delimiters as ordinary text', (tester) async {
      await tester.pumpWidget(const MaterialApp(
        home: Scaffold(body: MathAwareText(text: r'Value $x is incomplete')),
      ));

      final finder = richTextContaining(r'Value $x is incomplete');
      expect(finder, findsOneWidget);
      expect(tester.widget<RichText>(finder).text.toPlainText(), r'Value $x is incomplete');
    });

    testWidgets('creates an inline math widget for TeX delimiters', (tester) async {
      await tester.pumpWidget(const MaterialApp(
        home: Scaffold(body: MathAwareText(text: r'Energy is \(E=mc^2\)')),
      ));

      final finder = richTextContaining('Energy is ');
      expect(finder, findsOneWidget);
      final richText = tester.widget<RichText>(finder);
      expect(richText.text.toPlainText(), contains('Energy is '));
      final rootSpan = richText.text as TextSpan;
      expect(rootSpan.children!.any((span) => span is WidgetSpan), isTrue);
    });
  });
}
