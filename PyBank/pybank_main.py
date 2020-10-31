# This Python script analyzes the financial records found in budget_data.csv.


# Import the os and csv modules
import os
import csv

# Set path for csv
budgetcsv = os.path.join("resources/budget_data.csv")

# Create alias for budget_data.csv and pass through reader method
with open(budgetcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader) # Skip header row

    # Create dictionary to hold greatest profit increase and decrease
    results = {
        "max":[-999999999, ""], 
        "min":[999999999, ""]
    }
 
    # Set variables and counts to 0
    month_count = 0
    total = 0
    average_change = 0.00
    
    for x in csvreader:
        month_count = month_count + 1
        profit = int(x[1]) # Profit equals value in second column
        total = total + profit # Sum all values in second column for total profit 

        # Find greatest increase in profits
        if profit > results["max"][0]: # Maximum profit value is added to results dicitonary
            results["max"][0] = profit # Value
            results["max"][1] = x[0] # Month

        # Find greatest decrease in profits
        if profit < results["min"][0]: # Minimum profit value is added to results dicitonary
            results["min"][0] = profit # Value
            results["min"][1] = x[0] # Month
        average_change = total / month_count # Divide total profit by months to get average change
       

# Print results
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total}")
print(f"Average  Change: ${average_change:,.2f}")
print(f"Greatest Increase in Profits: {results['max'][1]} (${results['max'][0]})") # Greatest Increase in profits month and value
print(f"Greatest Decrease in Profits: {results['min'][1]} (${results['min'][0]})") # Greatest Decrease in profits month and value