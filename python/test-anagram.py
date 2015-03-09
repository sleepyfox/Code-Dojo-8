"A test suite for a Roman numeral converter"

import unittest

class OutOfRangeError: pass
class LookupError: pass

class RomanNumeral():
	numerals = { 1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M" }

	def toNumeral(self, v):
		if v < 1 or v > 3999:
			raise OutOfRangeError
		else:
			numeral = ""
			remainder = v
			while remainder > 0:
				numeral += self.numerals[self.find_biggest(remainder)]
				remainder -= self.find_biggest(remainder)
			return numeral

	def find_biggest(self, v):
		return max(i for i in self.numerals.keys() if i <= v)

class RomanNumerals(unittest.TestCase):
	def setUp(self):
		self.roman = RomanNumeral()

	def testLargest1isI(self):
		"the largest numeral <= 1 is 1"
		self.assertEqual(self.roman.find_biggest(1), 1)

	def testLargest7is5(self):
		"the largest numeral <= 7 is 5"
		self.assertEqual(self.roman.find_biggest(7), 5)

	def testLargest13is10(self):
		"the largest numeral <= 13 is 10"
		self.assertEqual(self.roman.find_biggest(13), 10)

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

	def test2isII(self):
		"2 should be converted to II"
		self.assertEqual(self.roman.toNumeral(2), "II")

	def test3isIII(self):
		"3 should be converted to III"
		self.assertEqual(self.roman.toNumeral(3), "III")

	def test4isIV(self):
		"4 should be converted to IV not IIII"
		self.assertEqual(self.roman.toNumeral(4), "IV")

	def test8isVIII(self):
		"8 should be converted to VIII"
		self.assertEqual(self.roman.toNumeral(8), "VIII")

	def test9isIX(self):
		"9 should be converted to IX not VIIII"
		self.assertEqual(self.roman.toNumeral(9), "IX")

	def test49isXLIX(self):
		"49 should be converted to XLIX not XXXXIX"
		self.assertEqual(self.roman.toNumeral(49), "XLIX")

	def test90isXC(self):
		"90 should be converted to XC not LXXXX"
		self.assertEqual(self.roman.toNumeral(90), "XC")

	def test1999isMCMXCIX(self):
		"1967 should be converted to MCMLXVII"
		self.assertEqual(self.roman.toNumeral(1967), "MCMLXVII")


if __name__ == "__main__":
	unittest.main()
