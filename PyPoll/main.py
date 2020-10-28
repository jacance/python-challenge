
# Calculate each of the following:


# Import modules
import os
import csv


vote_index = [0, 0, 0, 0]
candidates_list = []
all_votes = []

# Set path then open with csv.reader
electioncsvpath = os.path.join("resources/election_data.csv")


with open(electioncsvpath, newline="") as electioncsv:
    csvreader = csv.reader(electioncsv, delimiter=",")

    next(csvreader) # Skip header
    
    # # Set variables and start count at 0
    votes = 0
   
    for row in csvreader:
        votes = votes + 1
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
        all_votes.append(row[2])



with open(electioncsvpath, newline="") as electioncsv:
    csvreader = csv.reader(electioncsv, delimiter=",")

    next(csvreader) # Skip header

    for row in csvreader:    
        # if row[2] not in candidates_list:
        if all_votes[0] in row[2]:
            vote_index[0] += 1
        if all_votes[1] in row[2]:
            vote_index[1] += 1
        if all_votes[2] in row[2]:
            vote_index[2] += 1
        if all_votes[3] in row[2]:
            vote_index[3] += 1






print("Election Results")
print("-------------------------")
print(f"Total Votes: {votes}") # The total number of votes cast
print("-------------------------")
print(candidates_list[0],":",) #results['percent'][0], results['all_votes'][0])
print(candidates_list[1],":",) #results['percent'][1], results['all_votes'][1])
print(candidates_list[2],":",) #results['percent'][2], results['all_votes'][2])
print(candidates_list[3],":",) #results['percent'][3], results['all_votes'][3])
print("-------------------------")
print("Winner: _______")
print("-------------------------")