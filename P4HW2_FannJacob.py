# Jacob Fann
# 10/25/2026
# P4HW2
# Employee salary calculator w/ added loops

# Create accumlator variables
employee_amount = 0
overtime_total = 0
regular_total = 0
gross_total = 0

# Request employee information
employee = input("Enter Employee Name or 'done' to finish: ")

while employee != "done":
    # Add employee count
    employee_amount += 1
    # Ask for employee info
    hours = float(input(f"How many hours {employee} worked: "))
    rate = float(input(f"What is {employee}'s hourly pay rate: "))

    # Evaluate overtime
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate
        gross_pay = regular_pay + overtime_pay
    else:
        overtime_pay = 0
        overtime_hours = 0
        regular_pay = hours * rate
        gross_pay = regular_pay

    # Add to accumulator variables
    overtime_total += overtime_pay
    regular_total += regular_pay
    gross_total += gross_pay


    # Print final output to user
    print("-"*20)
    print(f"Employee Name: {employee}")
    print()
    print(f"{'Hours Worked':<15}{"Pay rate":<12}{"Overtime Hours":<18}{'Overtime Pay':<17}{'RegHour Pay':<17}{"Gross Pay":<15} ")
    print("-"*87)
    print(f"{hours:<15}{rate:<12}{overtime_hours:<18}{'$'}{overtime_pay:<16,.2f}{'$'}{regular_pay:<16,.2f}{'$'}{gross_pay:<13,.2f} ")


    employee = input("Enter Employee Name or 'done' to finish: ")

print(f"Total amount of employees entered: {employee_amount}")
print(f"Total amount paid for overtime: ${overtime_total}")
print(f"Total amount paid for regular hours: ${regular_total}")
print(f"Total amount paid in gross: ${gross_total}")