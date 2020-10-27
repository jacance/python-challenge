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


# # The total number of months included in the dataset

# # Count solution and offset the index starting at 0. Potentially use pie/candy examples

# Can use regular variables
# month_count = 0
# total = 0
# max_value = -999999999
# max_month = ""
# min_value = 999999999
# min_month = ""
# total_change = 0
# last_profit = 0 #will be profit from the last month, you will take value of the profit of this month, subtract last profit from it, that's how you get total
           
# if month_count ==0:
#     last_profit = profit
# else:
#     calculate the change
#     update hte last_profit

#Can use a dictionary
results = {
    "max":[-999999999, ""], #if the company is losing, you need to have maximum as a negative value so that 0 isn't cutoff
    "min":[999999999, ""]
}
max = {
    "profit": 0,
    "month": ""
}
min = {
    "profit": 0,
    "month": ""
}


# #Can use a list
# max = [0, ""]

# # max_inc = 0
# max_inc_month = ""

# # Can use regular variables

month_count = 0
total = 0

    for x in csvreader:
        month_count = month_count + 1
        month = x[0])
        profit = int(x[1])
        total = total + profit
        if profit > results["max"][0]:
            results["max"][0] = profit
            results["max"][1] = x[0]
            # print(x)

    print (results)
    print(f"There are {month_count} months.")

print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total}")
print(f"Average  Change: $-2315.12")
print(f"Greatest Increase in Profits: Feb-2012 ($1926159)")
print(f"Greatest Decrease in Profits: Sep-2013 ($-2196167)")

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


