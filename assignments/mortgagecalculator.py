#mortgage calculator

principal = float(input("Enter the principal amount: "))

annual_rate= float(input("Enter the annual interest rate: "))

time_in_years= int(input("Enter the duration in years: "))

monthly_rate = annual_rate/1200

time_in_months = time_in_years*12

monthly_payment = principal*((monthly_rate*((1+(monthly_rate))**time_in_months))/(((1+monthly_rate)**time_in_months)-1))

print(round(monthly_payment,2))