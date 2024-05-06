import pandas as pd
from monthly_income import getPostTaxIncome, getNDayTotal


income_data = pd.read_csv("./user_data/income.csv")
bills_data = pd.read_csv("./user_data/bills.csv")
spending_data = pd.read_csv("./user_data/spending.csv")

income_data["date"] = pd.to_datetime(income_data["date"])
income_data["taxable"] = income_data["taxable"].astype("bool")

income = getPostTaxIncome(income_data)

bills = getNDayTotal(bills_data)

spending = getNDayTotal(spending_data)

balance = round(income - (bills + spending), 2)
