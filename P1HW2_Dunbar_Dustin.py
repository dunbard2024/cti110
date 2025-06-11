# Dustin Dunbar
# June 11,2025
# P1HW2
# Create a program that does some basic math on numbers that are entered.

budget = 2000
city_name = "New Orleans"
gas = 300
lodge = 750
food = 350
expenses = gas+lodge+food
balance = budget-gas-lodge-food

print('This program calculates and display travel expenses')
print('Enter Budget:',budget)
print('Enter your travel destination:',city_name)
print('How much do you think you will spend on gas?',gas)
print('Approximately, how much will you need for accomodation/hotel?',lodge)
print('Last, how much do you need for food?',food)

print('-----Travel Expenses-----')
print('Location:',city_name)
print('Initial Budget:',budget)

print('Fuel:',gas)
print('Accomodation:',lodge)
print('Food:',food)

print('Remaining Balance:',balance)



