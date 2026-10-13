import unittest

from tool.import_mathematical_archive import (
    looks_like_cover_or_instruction,
    options,
    parse_blocks,
    question_stem,
    starts,
)


class MathematicalArchiveParserTests(unittest.TestCase):
    def test_extracts_four_labeled_options_without_rewriting(self):
        block = """Which statement is correct?
(A) x^2 + y^2
(B) x^2 - y^2
(C) \\int_0^1 x dx
(D) \\sum_{n=1}^\\infty 1/n^2
"""
        self.assertEqual(
            options(block),
            [
                "x^2 + y^2",
                "x^2 - y^2",
                "\\int_0^1 x dx",
                "\\sum_{n=1}^\\infty 1/n^2",
            ],
        )

    def test_question_stem_preserves_equation_line_breaks(self):
        block = """Find the derivative.
f(x) = x^2 + 3x
(A) 2x + 3
(B) 2x - 3
(C) x + 3
(D) x^2
"""
        self.assertEqual(question_stem(block), "Find the derivative.\nf(x) = x^2 + 3x")

    def test_cover_instruction_is_detected(self):
        block = """At the commencement of examination, the question booklet will be given to you.
(A) One (B) Two (C) Three (D) Four"""
        self.assertTrue(looks_like_cover_or_instruction(block))

    def test_real_question_is_not_misclassified_as_instruction(self):
        block = """Which one is an algebraically closed field?
(A) Z101
(B) Q
(C) R
(D) C"""
        self.assertFalse(looks_like_cover_or_instruction(block))

    def test_question_starts_are_anchored_to_line_starts(self):
        text = """Question 1. First question
Equation includes 2018 and 32.
2) Second question
The value is 86."""
        found = [number for _, _, number in starts(text, 100)]
        self.assertEqual(found, [1, 2])

    def test_parse_blocks_prefers_complete_mcq_candidate(self):
        pages = [
            (1, """1. Which is true?
(A) one
(B) two
(C) three
(D) four
2. Second question has incomplete options"""),
            (2, """1. Which is true?
(A) one
(B) two
(C) three
(D) four
2. Second question
(A) alpha
(B) beta
(C) gamma
(D) delta"""),
        ]
        blocks, source_pages = parse_blocks(pages, 2, include_page=True)
        self.assertEqual(len(options(blocks[1])), 4)
        self.assertEqual(len(options(blocks[2])), 4)
        self.assertEqual(source_pages[2], 2)


if __name__ == "__main__":
    unittest.main()
