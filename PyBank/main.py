import os
import csv

def data_pull(csv):
    months = 0
    total = 0
    high_month = ""
    high_profit = 0
    average_change = 0
    low_month = ""
    low_profit = 0
    last_month = None
    changes = []
    for row in csv:
        current_month = row[0]
        net_total = int(row[1])
        total += net_total
        months += 1
        if last_month is not None:
            current_change = net_total-last_month
            changes.append(current_change)
            if current_change > high_profit:
                high_profit = current_change
                high_month = current_month
            if current_change < low_profit:
                low_profit = current_change
                low_month = current_month

        last_month = net_total
    average_change = sum(changes)/len(changes)
    return [months, total, high_profit, low_profit, average_change]

with open("budget_data.csv") as file:
    csvreader = csv.reader(file, delimiter = ',')
    header = next(csvreader)
    data = data_pull(csvreader)
print(f"""
Financial Analysis
----------------
Total Months: {data[0]}
Total: ${round(data[1], 2)}
Average Change: ${round(data[4], 2)}
Greatest Increase: {data[5]} (${data[2]})
Greatest Decrease: {data[6]} (${data[3]})
""")
