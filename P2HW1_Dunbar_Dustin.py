# Dustin Dunbar
# June 22, 2025
# P2HW1
# Program calculates travel expenses

# Input section
print("This program calculates and displays travel expenses")
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Display section
print("\n------------ Travel Expenses ------------")
print(f"{'Location:':<20} {destination}")
print(f"{'Initial Budget:':<20} ${budget:,.2f}")
print(f"{'Fuel:':<20} ${gas:,.2f}")
print(f"{'Accommodation:':<20} ${accommodation:,.2f}")
print(f"{'Food:':<20} ${food:,.2f}")
print("-----------------------------------------")



# Calculate remaining balance
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

print(f"{'Remaining Balance:':<20} ${remaining_balance:,.2f}")
