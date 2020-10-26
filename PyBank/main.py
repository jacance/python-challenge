# Your task is to create a Python script that analyzes the records to calculate each of the following:

import os
import csv

# Set path for csv
budgetcsv = os.path.join("resources/budget_data.csv")
#--------------------------------------------------------------------

# Open csv path with csv.reader
with open(budgetcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader) #skip first row


# The total number of months included in the dataset

    # Count solution and offset the index starting at 0. Potentially use pie/candy examples
    month_count = 1
    for x in csvreader:
        month_count = month_count + 1
    
    print(f"There are {month_count - 1} months.")


# The net total amount of "Profit/Losses" over the entire period
    # skip header next(csvreader). for loop through 1-87
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


