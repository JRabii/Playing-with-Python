# create a path to collect csv from the Resources folder

import os
import csv

pypolldata = os.path.join('..', 'Resources', 'pypolldata.csv')

# declare variables
total_votes = 0
candidate_list = []
candidate_votes = {}  

# create the function
with open(path_pypolldata,'r', newline = '') as pypolldata:
   reader_csv = csv.reader(pypolldata, delimiter=',')

   for row in reader_csv:
       total_votes += 1
       candidate_name = row[2]
       
       # add candidate_name to candidate_list
       if candidate_name not in candidate_list:
           candidate_list.append(candidate_name)

       # start vote count for individual candidates
       if candidate_name not in candidate_votes:
           candidate_votes[candidate_name] = 1
       else: 
           candidate_votes[candidate_name] += 1

print("------------------")
print("Election Results")
print("------------------")
print(f"Total Votes: {str(total_votes)}")
print("------------------")
# I'm lost on how to make dictionaries appear...
print(f"["candidate_name"] received {candidate_votes["candidate_name"]} which was int{candidate_votes[candidate_name]}/["total_votes"]*100 percent of the overall votes")