    # Dustin Dunbar
    # P3LAB
    # June 26,2025
    # Calculates the number of dollars, quarters, dimes, nickles, and pennies
    
#Get value from user
change = float(input('Enter an amont of money as a float: $'))



#Converting the value to an interger
change = round(change * 100)



#Determin how many coins are needed
dollars = change // 100
change = change - (dollars * 100)

quarters = change // 25
change = change - (quarters * 25)               

dimes = change // 10
change = change - (dimes * 10)

nickels = change // 5
change = change - (nickels * 5)

pennies = change

if dollars > 0:
    if dollars == 1:
        print(f"{dollars} Dollar")
    else:
        print(f"{dollars} Dollars")

if quarters > 0:
    if quarters == 1:
        print(f"{quarters} Quarter")
    else:
        print(f"{quarters} Quarters")

if dimes > 0:
    if dimes == 1:
        print(f"{dimes} Dime")
    else:
        print(f"{dimes} Dimes")

if nickels > 0:
    if nickels== 1:
        print(f"{nickels} Nickel")
    else:
        print(f"{nickels} Nickels")

if pennies > 0:
    if pennies == 1:
        print(f"{pennies} Penny")
    else:
        print(f"{pennies} Pennies")
if change == 0:
    print(f"No Change")




