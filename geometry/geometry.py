import math


# AREA CIRCLE

def area_circle(r):
	area = (math.pi)*(r**2)
	return area

print "-----"
print "Radius = 2, area circle=" 
print area_circle(2)
print "-----"


# AREA SQUARE
# QUESTION : is it bad that I use "area" as my variable in both area_circle and area_square? 
# YES because "area" is only scoped within each definition

def area_square(s):
	area = s*s
	return area

print "Side = 3, area square ="
print area_square(3)
print "-----"


# AREA TRIANGLE

def area_triangle(s1,s2):
	areaTRI = (s1*s2)/(2)
	return areaTRI

print "Side1 = 1.0 and side2 = 7.0, area triangle ="
print area_triangle(1.0,7.0)
print "-----"


# VOLUME SPHERE

def volume_sphere(rad):
	Vsphere = (4.0/3.0)*(math.pi)*(rad**3)
	return Vsphere

print "Radius = 3.0, volume ="
print volume_sphere(3)
print "-----"


# SURFACE AREA SPHERE
# QUESTION : How do you print both words and a numerical result on one line?

def surface_sphere(radius):
	SurfSphere = (4)*(math.pi)*(radius**2)
	return SurfSphere

print "Radius = 3.0, suface area =" 
print surface_sphere(3)
print "-----"


# CALCULATE HYPOTENUSE

def calc_hyp(side1,side2):
	hypSquared = (side1**2)+(side2**2)
	hyp = math.sqrt(hypSquared)
	return hyp

print "Side1 = 4.0 and side2 = 6.0, hypotenuse = "
print calc_hyp(4.0,6.0)
print "-----"

