"A test suite for a Roman numeral converter"

import unittest

class OutOfRangeError: pass
class LookupError: pass

class RomanNumeral():
	def toNumeral(self, v):
		numerals = { 1: "I", 5: "V", 10: "X" }
		if v < 1:
			raise OutOfRangeError
		elif v in numerals:
			return numerals[v]
		else:
			raise LookupError

class RomanNumeralConverter(unittest.TestCase):
	def setUp(self):
		self.roman = RomanNumeral()

	def testZero(self):
		"trying to convert zero should raise an exception"
		with self.assertRaises(OutOfRangeError):
			self.roman.toNumeral(0)

	def test1isI(self):
		"1 should be converted to I"
		self.assertEqual(self.roman.toNumeral(1), "I")

	def test5isV(self):
		"5 should be converted to V"
		self.assertEqual(self.roman.toNumeral(5), "V")

	def test10isX(self):
		"10 should be converted to X"
		self.assertEqual(self.roman.toNumeral(10), "X")

if __name__ == "__main__":
	unittest.main()
