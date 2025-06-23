# Dustin Dunbar
# July 23, 2025
# P2HW2
# Enter grades for module 1-6 and display the lowest grade, highest grade, sum, and average grad

# Input section
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

# Creating the list of grades
student_grades = [module1, module2, module3, module4, module5, module6]

# Calculate grades for modules
total_sum = sum(student_grades)
average_grade = total_sum / 6

# Find lowest and highest grades
lowest_grade = min(student_grades)
highest_grade = max(student_grades)


# Display section
print("------------Results------------")
print(f"{'Lowest Grade:':<20}{lowest_grade:.1f}")
print(f"{'Highest Grade:':<20}{highest_grade:.1f}")
print(f"{'Sum of Grades:':<20}{total_sum:.1f}")
print(f"{'Average:':<20}{average_grade:.2f}")

print("----------------------------------------")
