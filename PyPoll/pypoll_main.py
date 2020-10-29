
# Calculate each of the following:


# Import modules
import os
import csv


vote_index = [0, 0, 0, 0]
candidates_list = []
all_votes = []
candidates = {}


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
        # all_votes.append(row[2])



with open(electioncsvpath, newline="") as electioncsv:
    csvreader = csv.reader(electioncsv, delimiter=",")

    next(csvreader) # Skip header

    for row in csvreader:    
        if candidates_list[0] == row[2]:
            vote_index[0] += 1
        elif candidates_list[1] == row[2]:
            vote_index[1] += 1
        if candidates_list[2] == row[2]: # Producing duplicate
            vote_index[2] += 1
        elif candidates_list[3] == row[2]: # Producing duplicate
            vote_index[3] += 1



percentage = [0, 0, 0, 0]
percentage[0] = (vote_index[0]/(votes) * 100)
percentage[1] = vote_index[1]/(votes ) * 100
percentage[2] = vote_index[2]/(votes ) * 100
percentage[3] = vote_index[3]/(votes) * 100
print(all_votes)
print(vote_index)

# # Function for percentage
# def finalpercentage(x):
#     percentage[x] = (vote_index[x]/(votes)
#     percentage[x] * 100
    


print("Election Results")
print("-------------------------")
print(f"Total Votes: {votes}") # The total number of votes cast
print("-------------------------")
print(f'{candidates_list[0]}: {vote_index[0]:,.0f}, {percentage[0]:.2f}%'),
print(f'{candidates_list[1]}: {vote_index[1]:,.0f}, {percentage[1]:.2f}%'),
print(f'{candidates_list[2]}: {vote_index[2]:,.0f}, {percentage[2]:.2f}%'), 
print(f'{candidates_list[3]}: {vote_index[3]:,.0f}, {percentage[3]:.2f}%'), 
print("-------------------------")
print(f'Winner: {max(vote_index)}') # Needs to be name using key value pair (dictionary)
print("-------------------------")