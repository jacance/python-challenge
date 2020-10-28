
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


percentage = [0, 0, 0, 0]
percentage[0] = vote_index[0]/(votes)
percentage[1] = vote_index[1]/(votes)
percentage[2] = vote_index[2]/(votes)
percentage[3] = vote_index[3]/(votes)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {votes}") # The total number of votes cast
print("-------------------------")
print(f'{candidates_list[0]}: {vote_index[0]}, {percentage[0]}'),
print(f'{candidates_list[1]}: {vote_index[1]}, {percentage[1]}'),
print(f'{candidates_list[2]}: {vote_index[2]}, {percentage[2]}'),
print(f'{candidates_list[3]}: {vote_index[3]}, {percentage[3]}'),
print("-------------------------")
print("Winner: _______")
print("-------------------------")