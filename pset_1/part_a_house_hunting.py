#Part A: House Hunting

annual_salary = float(input("Annual salary: "))
portion_saved = float(input("Portion savedeach month: "))
total_cost = float(input("Cost of your dream house: "))

monthly_salary = annual_salary / 12
portion_down_payment = total_cost * 0.25
portion_saved_monthly = monthly_salary * portion_saved
current_savings = 0
months = 0
while current_savings < portion_down_payment:
    current_savings = current_savings + (current_savings * (0.04/12)) + portion_saved_monthly
    months = months + 1
print('Number of Months:', months)


