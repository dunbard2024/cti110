    # Dustin Dunbar
    # P3HW2
    # June 27, 2025
    # Progam calculate payroll for a given employee


def calculate_pay():
    # Input employee details
    employee_name = input("Enter employee's name: ")
    hours_worked = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))

    # Initialize variables
    if hours_worked > 40:
        regular_hours = 40
        overtime_hours = hours_worked - regular_hours
    else:
        regular_hours = hours_worked
        overtime_hours = 0

    # Calculate pay
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay

    # Display results with proper spacing
    print("\nEmployee Name:         ", employee_name)
    print("Pay Rate:                ", format(pay_rate, '.2f'))
    print("Number of Hours Worked:  ", hours_worked)
    print("Overtime Hours:          ", overtime_hours)
    print("Overtime Pay:            ", format(overtime_pay, '.2f'))
    print("Pay for Regular Hours:   $", format(regular_pay, '.2f'))
    print("Gross Pay:               $", format(gross_pay, '.2f'))
   

# Execute the program
calculate_pay()
