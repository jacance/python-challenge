# Your task is to create a Python script that analyzes the records to calculate each of the following:

# Import the os and csv modules
import os
import csv

# Set path for csv
budgetcsv = os.path.join("resources/budget_data.csv")

# Create alias for budget_data.csv and pass through reader method
with open(budgetcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader) #skip header row


# The total number of months included in the dataset

    # Count solution and offset the index starting at 0. Potentially use pie/candy examples
    results = {
        "max":[-999999999, ""],
        "min":[999999999, ""]
    }
    # max = [0, ""]
    # max = {
    #     "profit": 0,
    #     "month": ""
    # }
    # min = {
    #     "profit": 0,
    #     "month": ""
    # }
    # max_inc = 0
    # max_inc_month = ""

    month_count = 0
    total = 0
    average_change = 0.00
    
    for x in csvreader:
        month_count = month_count + 1
        profit = int(x[1])
        total = total + profit
        # Find greatest increase in profits
        if profit > results["max"][0]:
            results["max"][0] = profit # Value
            results["max"][1] = x[0] # Month
        # Find greatest decrease in profits
        if profit < results["min"][0]:
            results["min"][0] = profit # Value
            results["min"][1] = x[0] # Month
        average_change = total / month_count

# print(average_change)    
# print(results)

print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total}")
print(f"Average  Change: ${average_change}")
print(f"Greatest Increase in Profits: {results['max'][1]}, ${results['max'][0]}") #Greatest Increase in profits
print(f"Greatest Decrease in Profits: {results['min'][1]}, ${results['min'][0]}") #Greatest Decrease in profits

# The net total amount of "Profit/Losses" over the entire period
    # set variable for pnl = 0
    # pnl = 0
    # for x in 
    # add second column up: pnl = pnl + column(i)

# The average of the changes in "Profit/Losses" over the entire period
    #


# The greatest increase in profits (date and amount) over the entire period
    #write function for max (biggest positive)

# The greatest decrease in losses (date and amount) over the entire period
    #write function for min (smallest negative)


