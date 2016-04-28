
dollars = { count: 0, value: 100 }
quarters = { count: 0, value: 25 }
dimes = { count: 0, value: 10 }
nickels = { count: 0, value: 5 }
pennies = { count: 0, value: 1 }

change_owed = 4.87
cents_owed = int(change_owed*100)

dollars = cents_owed / 100
cents_owed = cents_owed - dollars * 100
quarters = cents_owed / 25
cents_owed = cents_owed - quarters * 25
dimes = cents_owed / 10
cents_owed = cents_owed - dimes * 10
nickels = cents_owed / 5
cents_owed = cents_owed - nickels * 5
pennies = cents_owed / 1


dollars.count = cents_owed / dollars.value
cents_owed = cents_owed - dollars.count * dollars.value
quarters.count = cents_owed / quarters.value
cents_owed = cents_owed - quarters.count * quarters.value
dimes.count = cents_owed / dimes.value
cents_owed = cents_owed - dimes.count * dimes.value
nickels.count = cents_owed / nickels.value
cents_owed = cents_owed - nickels.count * nickels.value
pennies.count = cents_owed / pennies.value
cents_owed = cents_owed - pennies.count * pennies.value

tenders = [dollars, quarters, dimes, nickels, pennies]
for tender in tenders:
