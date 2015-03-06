"A test suite for a Roman numeral converter"

import unittest

class RomanNumeral():
	def toDecimal(self, v):
		return "I"

class RomanNumeralConverter(unittest.TestCase):
	def testIisOne(self):
		"1 should be converted to 'I'"
		roman = RomanNumeral()
		self.assertEqual(roman.toDecimal(1), "I")

if __name__ == "__main__":
	unittest.main()
