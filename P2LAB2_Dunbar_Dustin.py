# Dustin Dunbar
# June 18,2025
# P2LAB2
# Create dictionaries where the key and value pair

# Define a dictionary of cars and their MPG
cars = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

#Get keys from dict
keys=cars.keys()

print(keys)

print(*keys, sep=", ")


#Get car info from user
car_name = input ("Enter a vehicle to see it's mpg: ")

#Get car gas mileage
car_mpg = cars[car_name]
print (f"The {car_name} gets {car_mpg} mpg.")


#Get info from user miles driven
miles_driven = float(input(f"How many miles will you drive the {car_name}? "))

#Calculate
gallons_needed = miles_driven/car_mpg

#Display results
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles")
