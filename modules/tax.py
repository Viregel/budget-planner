import pandas as pd


def getIncomeTax(table):
    total_tax = table["Tax"].sum()
    return total_tax


def getIncomeTaxBreakdown(income):

    # TODO: Annual tax readjustment

    tax_data = pd.read_csv("./info/income_tax.csv")
    tax_data["Start"] = tax_data["Start"]/12

    def getIncomeInBracket(start_rate, end_rate=None):
        if income <= start_rate:
            return 0
        if end_rate is None:
            return income - start_rate
        if income > end_rate:
            return end_rate
        return income - start_rate

    start = tax_data["Start"]

    in_bracket = [getIncomeInBracket(start[0], start[1]),
                  getIncomeInBracket(start[1], start[2]),
                  getIncomeInBracket(start[2], start[3]),
                  getIncomeInBracket(start[3], None)
                  ]

    if income > start[3]:
        in_bracket[1] += in_bracket[0]
        in_bracket[0] = 0

    tax_data["Taxable"] = in_bracket

    tax_data["Tax"] = round(tax_data["Taxable"] * tax_data["Rate"], 2)

    return tax_data


def getNationalInsurance(income):
    ni = 0
    lower = 12570/12
    upper = 50270/12

    if income > upper:
        ni = (income-upper)*0.02 + (upper-lower)*0.08
    elif income > lower:
        ni = (income-lower)*0.08

    return ni


def getPensionContribution(income, p):
    pension = (income*p)
    post_pension_income = income - pension
    return post_pension_income


def getTakeHomePay(income):
    tax = getIncomeTax(income)
    ni = getNationalInsurance(income)
    pay = income - (tax+ni)
    return round(pay, 2)
