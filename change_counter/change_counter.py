"""
Change counter!

1) Create a function, calculate_change(total_cost, total_paid) which returns float of change to give
2) Create function,  convert_tender(change_owed), which returns human-readable string of dollars, quarters
	dimes, nickles, and pennies owed
3) Create a function, main_loop(), that when run in the console will continually ask the user for a
	total cost and total paid then print the human-readable string of change
"""
#class of tender used to add information to the dollar, nickel, etc. variables
class Tender():
	def __init__(self, name, plural, value):
		self.name = name
		self.plural = plural
		self.value = value
# penny, nickel, dime, quart instances (object) made
penny = Tender('penny', 'pennies', 1)
nickel = Tender('nickel', 'nickels', 5)
dime = Tender('dime', 'dimes', 10)
quarter = Tender('quarter', 'quarters', 25)
dollar = Tender('dollar', 'dollars', 100)

# make "tenders", an array of the objects to make them easy to pass around
tenders = [dollar, quarter, dime, nickel, penny]

#####################################################################################################################


def convert_tender_2(change_owed):
	if (change_owed > 0):
		print "you get", change_owed, "back in change"
	else:
		change_owed = (-1) * change_owed
		print "you need to pay", change_owed, "more for the meal"

	cents_owed = int(change_owed * 100)

	for tender in tenders:
		count = 0
			# FILL THIS IN MAGGOT
		count = cents_owed / tender.value
		cents_owed = cents_owed - count * tender.value

	
		if count == 1:
			print count, tender.name
		else:
			print count, tender.plural

# Calculate difference between price and amount of money given
# learning the raise keyword
def calculate_change(total_cost, total_paid):
	if isinstance(total_paid, float) and isinstance(total_cost, float):
		diff = (total_paid) - (total_cost)
		return diff
	else:
		raise TypeError('Parameters must be Floats')


################################################ NEW MAIN SPACE#################################################
if __name__ == '__main__':
	yes = 1
	while (yes == 1):
		# Input Section
		total_cost = input("What was the price?:")
		total_paid = input("What did you pay?:")
		print " "

	# Calculate change, return difference in float calue
		change_owed = calculate_change(total_cost, total_paid)
		convert_tender_2(change_owed)

		go_again = raw_input("Do it again?(y/n):")
		if go_again != "y":
			yes = 0
#####################################################################################################################












# Convert difference into tender



# def convert_tender(change_owed):
# 	dollar_convert = 0
# 	quarter_convert = 0
# 	dime_convert = 0
# 	nickel_convert = 0
# 	penny_convert = 0

# 	# change = { dollar: 0, quarter: 0, dime: 0, nickel: 0, penny: 0 }

# 	# NOTE THIS WONT work if the numbers are exact (aka >= 0.25, >= 0.1) why is that? Super Frustrating

# 	#DOLLARS
# 	while (change_owed >= 1.00):
#    		change_owed = change_owed - 1
# 		dollar_convert = dollar_convert + 1

# 	#QUARTERS
# 	while (change_owed >= 0.2499999):
# 		change_owed = change_owed - 0.25
# 		quarter_convert = quarter_convert + 1

# 	#DIMES
# 	while (change_owed >= 0.0999999):
# 		change_owed = change_owed - 0.10
# 		dime_convert = dime_convert + 1

# 	#NICKELS
# 	while (change_owed >= 0.049999):
# 		change_owed = change_owed - 0.05
# 		nickel_convert = nickel_convert + 1

# 	#PENNIES
# 	while (change_owed > 0):
# 		change_owed = change_owed - 0.01
# 		penny_convert = penny_convert + 1

# 	return dollar_convert, quarter_convert, dime_convert, nickel_convert, penny_convert

# try:
# 	calculate_change('20', '18')
# except TypeError, as e:
# 	print e.message


# except: # THE WORST PYTHON YOU CAN WRITE
# 	pass # THIS CODE COULD HAVE ERRORS BUT I DONT GIVE A FUCK



#Convert tender and output it
# # If you gave too little money made sure to convert to positive float before passing into convert_tender
# if difference < 0:
# 	owed = (-1)*(difference)
# 	change_owed = round(owed, 2)
# 	(dollar, quarter, dime, nickel, penny) = convert_tender(change_owed)

# 	print "you need to pay", change_owed, "more for the meal"
# 	print dollar, "dollars", quarter, "quarters", dime, "dimes", nickel, "nickels", penny, "pennies"


# elif difference > 0:
# 	change_owed = round(difference, 2)
# 	(dollar, quarter, dime, nickel, penny) = convert_tender(change_owed)

# 	print "you get", change_owed, "back in change"
# 	print dollar, "dollars", quarter, "quarters", dime, "dimes", nickel, "nickels", penny, "pennies"



# # Example output: "$2.33 owed: 2 dollars, 1 quater, 0 dimes, 1 nickel, and 3 pennies"











# Use the input function to get input from user:
# total = input("Please Enter Total:")

# print total

#def main_loop():



# HERE'S SOME TESTS
# calculate_change(15.50, 20) == 4.50
# convert_tender(2.33) == "$2.33 owed: 2 dollars, 1 quater, 0 dimes, 1 nickel, and 3 pennies"
