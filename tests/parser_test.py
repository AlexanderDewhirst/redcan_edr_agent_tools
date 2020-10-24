#!/usr/bin/env python

import sys
import unittest
from unittest.mock import patch
from parsers.parser import Parser

class ParserTest(unittest.TestCase):

    def setUp(self):
        args = ['file_manager', '-a', 'create', '-f', 'output.csv', '-l', 'logfile.csv']
        with patch.object(sys, 'argv', args):
            self.parser = Parser()

    def test_parser(self):
        self.assertIsNotNone(self.parser.parser)
        # self.assertIsNone(self.parser.__description)
        self.assertTrue(self.parser.status)

    def test_repr(self):
        self.assertEqual(
            self.parser.__repr__(),
            "Parser ['test.py'] has description: None"
        )
