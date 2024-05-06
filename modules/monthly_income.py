from dates import today, getMonthStartAndEnd, nDayRange
from tax import getIncomeTax, getIncomeTaxBreakdown, getNationalInsurance


def getPostTaxIncome(table, month=today):
    monthly = getMonthlyData(table, month)

    taxable = isTaxable(monthly)
    non_taxable = isNotTaxable(monthly)

    taxable_total = getMonthlyTotal(taxable)
    non_taxable_total = getMonthlyTotal(non_taxable)

    total_tax = getTaxForMonth(taxable_total)
    post_tax = (taxable_total - total_tax) + non_taxable_total
    return post_tax


def getTaxForMonth(income):
    tax_data = getIncomeTaxBreakdown(income)
    total_tax = getIncomeTax(tax_data) + getNationalInsurance(income)
    return total_tax


def getMonthlyTotal(table, month=today):
    monthly_data = getMonthlyData(table, month)
    monthly_total = monthly_data["amount"].sum()
    return monthly_total


def getNDayTotal(table, month=today, n=30):
    monthly_data = getNDayData(table, month, n)
    monthly_total = monthly_data["amount"].sum()
    return monthly_total


def isTaxable(table):
    monthly_data = table[(table["taxable"])]
    return monthly_data


def isNotTaxable(table):
    monthly_data = table[~(table["taxable"])]
    return monthly_data


def getMonthlyData(table, month=today):
    start, end = getMonthStartAndEnd(month)
    monthly_data = table[(table["date"] >= start) &
                         (table["date"] <= end)]
    return monthly_data


def getNDayData(table, month=today, n=30):
    start, end = nDayRange(month, n)
    monthly_data = table[(table["date"] >= start) &
                         (table["date"] <= end)]
    return monthly_data
