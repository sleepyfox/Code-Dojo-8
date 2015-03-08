"A test suite for a Roman numeral converter"

import unittest

class OutOfRangeError: pass
class LookupError: pass

class RomanNumeral():
	def toNumeral(self, v):
		numerals = { 1: "I", 5: "V" }
		if v < 1:
			raise OutOfRangeError
		elif v in numerals:
			return numerals[v]
		else:
			raise LookupError

class RomanNumeralConverter(unittest.TestCase):
	def testZero(self):
		"trying to convert zero should raise an exception"
		roman = RomanNumeral()
		with self.assertRaises(OutOfRangeError):
			roman.toNumeral(0)

	def testIisOne(self):
		"1 should be converted to I"
		roman = RomanNumeral()
		self.assertEqual(roman.toNumeral(1), "I")

	def testVisFive(self):
		"5 should be converted to V"
		roman = RomanNumeral()
		self.assertEqual(roman.toNumeral(5), "V")

if __name__ == "__main__":
	unittest.main()
