
# Dustin Dunbar
# July 7, 2025
# P4WH2
# Caculate pay roll for inserted personel. 


# Setting the variables for the totals.
over_hours = 0
total_over_pay = 0
total_reg = 0
total_gross = 0
total_employees = 0


# Prompts the user to input the employee's name and stores it into a variable.
employee_name = input('Enter employee\'s name or "Done" to terminate: ')


# Begins a loop to input employee data until terminated
while employee_name != 'Done':
    hours_worked = float(input(f'How many hours did {employee_name} work? '))
    pay_rate = float(input(f'What is {employee_name}\'s pay rate? '))
    
    # Calculates the regualar pay based on the standard 40 hours.
    if hours_worked <= 40:
        reg_pay = hours_worked * pay_rate
        over_pay = 0
    
    # Calculates the overtime hours and pay based on the standard.
    else:
        reg_pay = 40 * pay_rate
        over_hours = hours_worked - 40
        over_pay = over_hours * (pay_rate * 1.5)

    # Calculates the gross pay of the employee.
    gross_pay = reg_pay + over_pay

    # Updates the total variables.
    total_employees += 1
    total_reg += reg_pay
    total_gross += gross_pay
    total_over_pay += over_pay

    # Displays the employee's name and information.
    print()
    print('Employee Name:\t', employee_name)
    print()
    print('Hours Worked   Pay Rate    OverTime    OverTime Pay        RegHour Pay        Gross Pay')
    print('-------------------------------------------------------------------------------------------------')
    print(f'{hours_worked:<13.1f}  {pay_rate:<10.1f}  {over_hours:<10.1f}  {over_pay:<18.2f}  ${reg_pay:<16.2f}  ${gross_pay:<15.2f}')

    # Restarting the loop with the first question asked.
    print()
    employee_name = input('Enter employee\'s name or "Done" to terminate: ')
    
# Terminating the loop while displaying the grand total of info gathered if Done is entered.
else:
    #Displays the total of all obtained information
    print()
    print(f'Total number of employees entered: {total_employees}')
    print(f'Total amount paid for overtime: ${total_over_pay:.2f}')
    print(f'Total amount paid for regular hours: ${total_reg:.2f}')
    print(f'Total amount paid in gross: ${total_gross:.2f}')
