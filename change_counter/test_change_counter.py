import unittest
from change_counter import calculate_change

class ConvertTenderTests(unittest.TestCase):

	def test_case1(self):
		self.assertEqual(calculate_change(3.0, 5.0),2.0)

if __name__ == '__main__':
	unittest.main()

#test cases to run
#- negative change
#- exact change test case
