import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:gset_test_series/main.dart';

void main() {
  group('MathAwareText', () {
    testWidgets('renders ordinary text unchanged', (tester) async {
      await tester.pumpWidget(const MaterialApp(
        home: Scaffold(body: MathAwareText(text: 'GSET Paper-II')),
      ));

      expect(find.text('GSET Paper-II'), findsOneWidget);
    });

    testWidgets('keeps unmatched math delimiters as ordinary text', (tester) async {
      await tester.pumpWidget(const MaterialApp(
        home: Scaffold(body: MathAwareText(text: r'Value $x is incomplete')),
      ));

      expect(find.text(r'Value $x is incomplete'), findsOneWidget);
    });

    testWidgets('creates an inline math widget for TeX delimiters', (tester) async {
      await tester.pumpWidget(const MaterialApp(
        home: Scaffold(body: MathAwareText(text: r'Energy is \(E=mc^2\)')),
      ));

      expect(find.byType(RichText), findsOneWidget);
      final richText = tester.widget<RichText>(find.byType(RichText));
      expect(richText.text.toPlainText(), contains('Energy is '));
      final rootSpan = richText.text as TextSpan;
      expect(rootSpan.children!.any((span) => span is WidgetSpan), isTrue);
    });
  });
}
