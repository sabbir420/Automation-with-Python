#!/usr/bin/env python3

from rearrange_name import rearrange_name
import unittest

class TestArrange(unittest.TestCase):
	def test_basic(self):
		testcase = "Lovelace, Ada"
		expected = "Ada Lovelace"
		self.assertEqual(rearrange_name(testcase), expected)

	def test_empty(self):
		testcase = ""
		expected = ""
		self.assertEqual(rearrange_name(testcase), expected)

	def test_double_name(self):
		testcase = "Kennedy, John F."
		expected = "John F. Kennedy"
		self.assertEqual(rearrange_name(testcase), expected)

	def test_one_name(self):
		testcase = "Voltaire"
		expected = "Voltaire"
		self.assertEqual(rearrange_name(testcase), expected)

if __name__ == "__main__":
	unittest.main()