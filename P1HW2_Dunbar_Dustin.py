# Dustin Dunbar
# June 16,2025
# P1HW2
# Create a program that does some basic math on numbers that are entered.

print("This program calculates and displays travel expenses")
budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas? "))
accommodation = int(input("Approximately, how much will you need for accommodation/hotel? "))
food = int(input("Last, how much do you need for food? "))

print("------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print(f"Fuel: {gas}")
print(f"Accommodation: {accommodation}")
print(f"Food: {food}")

total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

print(f"Remaining Balance: {remaining_balance}")


