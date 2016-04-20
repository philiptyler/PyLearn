"""
Change counter!

1) Create a function, calculate_change(total_cost, total_paid) which returns float of change to give
2) Create function,  convert_tender(change_owed), which returns human-readable string of dollars, quarters
	dimes, nickles, and pennies owed
3) Create a function, main_loop(), that when run in the console will continually ask the user for a
	total cost and total paid then print the human-readable string of change
"""

# Input Section
total_cost = input("What was the price?:")
total_paid = input("What did you pay?:") 

# Example output: 2.66 (make sure its only 2 decimal places! your parameters may not be)

def calculate_change(total_cost, total_paid):
	diff = (total_paid) - (total_cost)
	return diff

def convert_tender(change_owed):
	dollar_convert = 0
	quarter_convert = 0
	dime_convert = 0
	nickel_convert = 0
	penny_convert = 0
	while (change_owed >= 1.00):
   		change_owed = change_owed - 1
		dollar_convert = dollar_convert + 1 
	while (change_owed >= 0.25):
		change_owed = change_owed - 0.25
		quarter_convert = quarter_convert + 1
	while (change_owed >= 0.10):
		change_owed = change_owed - 0.10
		dime_convert = dime_convert + 1
	while (change_owed >= 0.05):
		change_owed = change_owed - 0.05
		dime_convert = dime_convert + 1
	while (change_owed >= 0):
		change_owed = change_owed - 0.01
		penny_convert = penny_convert + 1
	return dollar_convert, quarter_convert, dime_convert, nickel_convert, penny_convert

# Calculate change and tell
difference = calculate_change(total_cost, total_paid)
print difference

if difference < 0:
	owed = (-1)*(difference)
	change_owed = round(owed, 2)
	print "you need to pay", change_owed, "more for the meal"
	(dollar, quarter, dime, nickel, penny) = convert_tender(change_owed)
	print change_owed, "converts to"
	print dollar, "dollars"
	print quarter, "quarters"
	print dime, "dimes"
	print nickel, "nickels"
	print penny, "pennies"
		

elif difference > 0:
	change_owed = round(difference, 2)
	print "you get", change_owed, "back in change"
	convert_tender(change_owed)
	print (change_owed)
	

# Example output: "$2.33 owed: 2 dollars, 1 quater, 0 dimes, 1 nickel, and 3 pennies"











# Use the input function to get input from user:
# total = input("Please Enter Total:")

# print total

#def main_loop():



# HERE'S SOME TESTS
# calculate_change(15.50, 20) == 4.50
# convert_tender(2.33) == "$2.33 owed: 2 dollars, 1 quater, 0 dimes, 1 nickel, and 3 pennies"
