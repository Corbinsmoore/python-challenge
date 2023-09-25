import os 
import csv
import math

#importing csv
csvpath = os.path.join(".", "Resources", "budget_data.csv")

#open csv
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

#defining variables 
months = 0
total_amount  = 0
total_changes = []
previous_amount = 0
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0
total_months = []

#loop
for row in csvreader:
#       print(row)
      months = months + 1
      total_amount = total_amount + 1
      change = int(row[1]) - previous_amount
      previous_amount = int(row[1])
      total_changes.append(change)
      greatest_increase = max(total_changes)
      greatest_decrease = min(total_changes)
      greatest_increase_month = total_changes.index(max(total_changes))
      greatest_decrease_month = total_changes.index(min(total_changes))
      total_months.append(row[0])

print (f"Total Months: {months}")
print (f"Total: ${total_amount}")
total_changes.pop(0)
print (f"Average Change: ${sum(total_changes)/len(total_changes)}")
print (f"Greatest Increase in Profits: {total_months[greatest_increase_month]}(${str(greatest_increase)})")
print (f"Greatest decrease in profits: {total_months[greatest_decrease_month]}(${str(greatest_decrease)})")

