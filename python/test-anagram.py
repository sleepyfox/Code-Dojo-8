"A test suite for a Roman numeral converter"

import unittest

class OutOfRangeError: pass

class RomanNumeral():
	def toDecimal(self, v):
		if v < 1:
			raise OutOfRangeError
		else:
			return "I"

class RomanNumeralConverter(unittest.TestCase):
	def testZero(self):
		"trying to convert zero should raise an exception"
		roman = RomanNumeral()
		with self.assertRaises(OutOfRangeError):
			roman.toDecimal(0)

	def testIisOne(self):
		"1 should be converted to 'I'"
		roman = RomanNumeral()
		self.assertEqual(roman.toDecimal(1), "I")

if __name__ == "__main__":
	unittest.main()
