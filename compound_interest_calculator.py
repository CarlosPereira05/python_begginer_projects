import math
print("Welcome to the Compound Interest Calculator!")
print("We will ask a bunch of informations before!")
input("Press Enter to Start...")

time = int(input("Enter the deadline of your investment (number of years): "))
capital = float(input("Enter the amount you want to invest: $"))
annual_interest = float(input("Enter the interest rate (anually): "))

result = 0
profit = 0

#compound interest formula: A = P * (1+r)^n 
total = (((annual_interest / 100) + 1) ** time) * capital
profit = total - capital
last_month_total = (((annual_interest / 100) + 1) ** (time - 1/12)) * capital
last_month_profit = total - last_month_total

print("Total is ${:,.2f}".format(total))
print("Last Month Profit is ${:,.2f}".format(last_month_profit))
print("The total profit is ${:,.2f}".format(profit))
