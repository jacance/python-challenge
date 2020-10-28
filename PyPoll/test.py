# Import modules
import os
import csv

# Set path then open with csv.reader
electioncsvpath = os.path.join("resources/election_data.csv")

with open(electioncsvpath, newline="") as electioncsv:
    csvreader = csv.reader(electioncsv, delimiter=",")

    next(csvreader) # Skip header

   

      for row in csvreader:
        if row == 'Correy:
            vote_index[1] =+ 1
        if row == candidates_list[2]:
            vote_index[2] =+ 1
        if row == candidates_list[3]:
            vote_index[3] =+ 1
