# Jacob Fann
# 10/11/2026
# P3HW2
# Employee salary calculator


# Gather name from user
name = input("Enter Employee Name: ")

# Gather hours from user
hours = int(input("Enter how many hours worked: "))

# Gather pay rate from user
rate = float(input("Enter employee's hourly pay rate: "))

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

# Print final output to user
print("-"*20)
print(f"Employee Name: {name}")
print()
print(f"{'Hours Worked':<15}{"Pay rate":<12}{"Overtime Hours":<18}{'Overtime Pay':<17}{'RegHour Pay':<17}{"Gross Pay":<15} ")
print("-"*87)
print(f"{hours:<15}{rate:<12}{overtime_hours:<18}{'$'}{overtime_pay:<16,.2f}{'$'}{regular_pay:<16,.2f}{'$'}{gross_pay:<13,.2f} ")


