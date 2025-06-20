# Dustin Dunbar
# June 18,2025
#P2LAB1
# Calculating the diameter , circumference, and area of a circle

import math


    # Get radius from user input
radius = float(input('Enter radius of circle:'))

    # Calculate diameter
diameter = 2 * radius

    # Calculate circumference
circumference = 2 * math.pi * radius

    # Calculate area
area = math.pi * (radius ** 2)

    # Display the results with formatting
print(f'What is the radius of the circle? {radius}') 
print(f'The diameter of the circle is {diameter:.1f}')
print(f'The circumference of the circle is {circumference:.2f}')
print(f'The area of the circle is {area:.3f}')
          

