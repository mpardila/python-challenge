import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join ('Resources/budget_data.csv')

# Read the CSV file and read the heather
with open (budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Lists and variables to store data
    date = []
    pl_running_total = 0
    previous_pl = 0
    math = []

    # Loop through the rows
    for row in csvreader:

        # For the total number of months included in the dataset
        date.append(row)
        
        # The net total amount of "Profit/Losses" over the entire period
        pl_running_total = pl_running_total + int(row[1])

        # For the changes in "Profit/Losses" over the entire period, and then the average of those changes
        current_pl = int(row[1])
        if previous_pl != 0:
            pl_change = current_pl - previous_pl
            math.append(pl_change)
        previous_pl = current_pl

    # The total number of months included in the dataset
    total_num_months = len(date)

    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    average_pl = round(sum(math)/(total_num_months-1), 2)

    # The greatest increase in profits (date and amount) over the entire period
    greatest_inc = max(math)
    index_greatest_inc = math.index(greatest_inc)
    month_greates_inc = date[index_greatest_inc +1]

    # The greatest decrease in profits (date and amount) over the entire period
    greatest_dec = min(math)
    index_greatest_dec = math.index(greatest_dec)
    month_greates_dec = date[index_greatest_dec + 1]

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_num_months))
print("Total: $" + str(pl_running_total))
print("Average Change: $" + str(average_pl))
print("Greatest Increase in Profits: " + month_greates_inc[0] + " ($" + str(greatest_inc) + ")")
print("Greatest Decrease in Profits: " + month_greates_dec[0] + " ($" + str(greatest_dec) + ")")