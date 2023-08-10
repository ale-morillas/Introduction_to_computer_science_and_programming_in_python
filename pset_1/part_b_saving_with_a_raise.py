#Part B: Saving, with a raise

annual_salary = float(input("Annual salary: "))
portion_saved = float(input("Portion saved each month: "))
total_cost = float(input("Cost of your dream house: "))
semi_annual_raise = float(input("Semi-annual raise: "))

current_savings = 0
months = 0
   
while current_savings < portion_down_payment:
    if months % 6 == 0 and months / 6 > 0:
        annual_salary = annual_salary + (annual_salary * semi_annual_raise)
        monthly_salary = annual_salary / 12
        portion_down_payment = total_cost * 0.25
        portion_saved_monthly = monthly_salary * portion_saved
    current_savings = current_savings + (current_savings * (0.04/12)) + portion_saved_monthly     
    months = months + 1
print('Number of Months:', months)