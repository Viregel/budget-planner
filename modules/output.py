from process import income, bills, spending, balance
from dates import daysElapsed, daysRemaining

print("Total income:", income)
print("Total bills:", bills)
print("Spending per day:", round(spending/daysElapsed, 2))
print("Money remaining:", round(balance/daysRemaining, 2))
