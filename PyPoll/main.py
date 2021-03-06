# This Python script analyzes the voting records found in election_data.csv.

# Import modules
import os
import csv


# Set path then open with csv.reader
electioncsvpath = os.path.join("resources/election_data.csv")

with open(electioncsvpath, newline="") as electioncsv:
    csvreader = csv.reader(electioncsv, delimiter=",")

    next(csvreader) # Skip header
    
    # Set variables and start vote count at 0
    votes = 0
    candidates = {}
   
    for row in csvreader:
        votes = votes + 1
        if row[2] not in candidates.keys(): 
            candidates[row[2]] = 1 # Adds unique candidate names to dictionary as keys
        else:
            candidates[row[2]] += 1 # Adds a candidate vote every time a candidates name is found

# Sorted candidates dictionary by values/vote counts in descending order
sorted_candidates = {
    k: v for k, v in sorted(candidates.items(), 
    key=lambda item: item[1], reverse=True)
}

# Convert percentage of candidate votes
def percentfunction(parameter):
    percent = ((parameter/votes) * 100)
    return round(percent, 2) 

# Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {votes}") # The total number of votes cast
print("-------------------------")
for kv in sorted_candidates.items(): # For loop to print candidates, votes, and percentage of votes
    print(f'{kv[0]}: {kv[1]}, {percentfunction(kv[1]):,.2f}%')
print("-------------------------")
print('Winner:', (list(sorted_candidates.keys())[0])) # Prints name of candidate with most votes
print("-------------------------")

# Print results to txt file
with open("Analysis/pypoll_output.txt", "a") as f:
    print("Election Results", file=f)
    print("-------------------------", file=f)
    print(f"Total Votes: {votes}", file=f) 
    print("-------------------------", file=f)
    for kv in sorted_candidates.items(): 
        print(f'{kv[0]}: {kv[1]}, {percentfunction(kv[1]):,.2f}%', file=f)
    print("-------------------------", file=f)
    print('Winner:', (list(sorted_candidates.keys())[0]), file=f) 
    print("-------------------------", file=f)

f.close()