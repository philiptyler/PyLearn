import geometry
import unittest
import math

# Why is the "self" necessary here again when defining test?? What context are we using? math.pi?
# Why is TestGeometry a class? Is it just telling the interpreter to prepare for testcases? We never call TestGeometry anywhere...
# I dont understand that third part in the documentation, msg=None, what is that for?

#try to work in assert trye

class TestGeometry(unittest.TestCase):

	def test_area_circle(self):
		self.assertEqual(geometry.area_circle(2), 4.0*math.pi)
		self.assertNotEqual(geometry.area_circle(2), 4.1*math.pi)
	print "circle test all good, assertEqual and assertNotEqual tests used"


	def test_area_triangle(self):
		self.assertIs(geometry.area_triangle(2, 1), geometry.area_triangle(2, 1))
		self.assertNotEqual(geometry.area_triangle(4,2), geometry.area_triangle(2,1))
	print "area triangle all good, assertIs and assertNotEqual tests used"


	def test_volumeofthesphere(self):
		self.assertEqual(geometry.volume_sphere(7), geometry.volume_sphere(7.0))
		self.assertEqual(geometry.volume_sphere(0), 0.0)
		self.assertNotAlmostEqual(geometry.volume_sphere(6),geometry.volume_sphere(8.6),1)		
	print "volume sphere all good, assertEqual and assertNotAlmostEqual"


	def test_sphere_surface(self):
		self.assertIsNot(geometry.surface_sphere(2), geometry.surface_sphere(2.01))
		self.assertIsNotNone(geometry.surface_sphere(0.00001))
	print "sphere surface all good, assertIsNot and assertIsNotNone used"
	
	def test_PARTAYPARTYAYAYAYAhonestlythisisjusttheHYPOTENUSEtestOMGOMG0000(self):
		self.assertGreaterEqual(geometry.calc_hyp(2,2), geometry.calc_hyp(1,1))
		self.assertAlmostEqual(geometry.calc_hyp(2,2), geometry.calc_hyp(2.01,2.01),1)
	print "hypotenuse tests assertGreaterEqual and assertAlmostEqual 2.01,2.01 and 2,2 are equal to 1st decimal digit"

if __name__ == '__main__':
    unittest.main()

