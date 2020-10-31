
# Calculate each of the following:


# Import modules
import os
import csv


vote_index = [0, 0, 0, 0]
candidates_list = []
all_votes = []
candidates = {}
# candidates.keys() +> keys in the dict as list
# candidates.values() >> values as list
# candidates.items() >> list of tuples (k,v)
# .sorted


# Set path then open with csv.reader
electioncsvpath = os.path.join("resources/election_data.csv")

with open(electioncsvpath, newline="") as electioncsv:
    csvreader = csv.reader(electioncsv, delimiter=",")

    next(csvreader) # Skip header
    
    # Set variables and start count at 0
    votes = 0
   
    for row in csvreader:
        votes = votes + 1
        if row[2] not in candidates.keys():
            #candidates_list.append(row[2])
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1

print(candidates)

#def sorted(dict, sortBy = value):
 #   for k, v in dict.items():
  #      sortingFunction (v)


#def mysort(val):
    #steps

sortedCandidate = {k: v for k, v in sorted(candidates.items(), key=lambda item: item[1], reverse=True)}

print(sortedCandidate)



def percentfunction(parameter):
    percent = ((parameter/votes) * 100)
    return round(percent, 2) # 



print("Election Results")
print("-------------------------")
print(f"Total Votes: {votes}") # The total number of votes cast
print("-------------------------")
for kv in sortedCandidate.items():
    #kv = ('Khan',443433)
    print(f'{kv[0]}: {kv[1]}, {percentfunction(kv[1]):,.2f}%')
print("-------------------------")
print('Winner:', (list(sortedCandidate.keys())[0])) # Needs to be name using key value pair (dictionary)
print("-------------------------")





# with open(electioncsvpath, newline="") as electioncsv:
#     csvreader = csv.reader(electioncsv, delimiter=",")

#     next(csvreader) # Skip header

#     for row in csvreader:    
#         if candidates_list[0] == row[2]:
#             vote_index[0] += 1
#         elif candidates_list[1] == row[2]:
#             vote_index[1] += 1
#         if candidates_list[2] == row[2]: 
#             vote_index[2] += 1
#         elif candidates_list[3] == row[2]: 
#             vote_index[3] += 1


# Function for calculating and rounding vote


# print(percentfunction(vote_index[1]))
    

# # percentage = [0, 0, 0, 0]
# # percentage[0] = vote_index[0]/(votes) * 100
# # percentage[1] = vote_index[1]/(votes) * 100
# # percentage[2] = vote_index[2]/(votes) * 100
# # percentage[3] = vote_index[3]/(votes) * 100


# # # Function for percentage
# # def finalpercentage(x):
# #     percentage[x] = (vote_index[x]/(votes)
# #     percentage[x] * 100
    

# # Base for dictionary
# # candidates = {
# # 	"Khan": "",
# #     "Correy": "",
# #     "Li": "",
# #     "O'Tooley: ""
# # }

# # x = candidates.keys()
# # candidate["Khan"] = 30

# # print(x)

# # def print_results(x)
#     # for x in x:


# print("Election Results")
# print("-------------------------")
# print(f"Total Votes: {votes}") # The total number of votes cast
# print("-------------------------")
# print(f'{kv[0]}: {kv[1]:,.2f}, {percentfunction(kv[1]):,.2f}%'),
# print(f'{candidates_list[1]}: {vote_index[1]:,.2f}, {percentfunction(vote_index[1]):,.2f}%'),
# print(f'{candidates_list[2]}: {vote_index[2]:,.2f}, {percentfunction(vote_index[2]):,.2f}%'), 
# print(f'{candidates_list[3]}: {vote_index[3]:,.2f}, {percentfunction(vote_index[3]):,.2f}%'), 
# print("-------------------------")
# print(f'Winner: {max(vote_index)}') # Needs to be name using key value pair (dictionary)
# print("-------------------------")