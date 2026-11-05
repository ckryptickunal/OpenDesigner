#!/usr/bin/env python3
"""Tests for brand/tools/check_names.py's near-name rules: names of several words count as near only when they differ
in one distinctive word, so a misspelt invented name is caught and two different real names are not.

  python3 tools/test_check_names.py
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "brand" / "tools"))
import check_names as N  # noqa: E402

WORDS = {"health", "wealth", "clinic", "river", "rivet"}


class NearNames(unittest.TestCase):
    def test_one_distinctive_word_a_letter_apart(self):
        self.assertTrue(N.near_names("Vosberg Health", "Vossberg Health", WORDS))
        self.assertTrue(N.near_names("Tellwick Labs", "Stellwick Labs", WORDS))

    def test_distinct_names_stay_apart(self):
        for a, b in (("Mette Jensen", "Lars Jansen"),        # two real people: more than one word differs
                     ("Acme Health", "Acme Wealth"),         # the differing word is a generic company word
                     ("Acme River", "Acme Rivet"),           # the differing word is a dictionary word
                     ("Vosberg Health", "Vossberg Clinic"),  # two words differ
                     ("Vosberg Health", "Vossberg Health Group"),
                     ("Kell Bay Hotel", "Kelt Bay Hotel"),   # under five letters: too short to call a near miss
                     ("Vossberg", "Vosberg")):               # one word each: the single-word rule's job (near)
            self.assertFalse(N.near_names(a, b, WORDS), (a, b))

    def test_single_words_keep_their_rule(self):
        self.assertTrue(N.near("Tellwick", "Stellwick"))
        self.assertFalse(N.near("Tellwick", "Tellwicks"))


if __name__ == "__main__":
    unittest.main()
