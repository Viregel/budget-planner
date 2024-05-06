def getTotalCost(table, time_period=30):
    # TODO: Limit table to anything within relevant time period
    # Change to current month?
    table_in_range = table

    return sum(table_in_range["amount"])