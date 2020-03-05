#Modules
import os
import csv

#open CSV file
file=os.path.join('Resources','election_data.csv')
with open (file, 'r', newline= "") as csvfile:
    reader=csv.reader(csvfile, delimiter= ",")
   

   #variables
total_votes = 0
candidates= []
individual_votes = []

for row in reader:
        #Total Votes
        total_votes += 1
        #skip 
        candidate_in = (row[2])
        #add to vote count if candidate already exists
        if candidate_in in candidates:
            candidate_index = candidates.index(candidate_in)
            individual_votes[candidate_index] = individual_votes[candidate_index] + 1
        else:
            #if candidate was not found in candidates list then append to list and add 1 to vote count
            candidates.append(candidate_in)
            individual_votes.append(1)

pct = []
max_votes = individual_votes[0]
max_index = 0

for x in range(len(candidates)):
    #calculation to get the percentage
    vote_pct = round(individual_votes[x]/total_votes*100, 2)
    pct.append(vote_pct)
    
    if individual_votes[x] > max_votes:
        max_votes = individual_votes[x]
        max_index = x

election_winner = candidates[max_index] 


print('|                  Election Results                  |')
print('======================================================')
print(f'Total Votes: {total_votes}')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
for x in range(len(candidates)):
    print(f'{candidates[x]} : {pct[x]}% ({individual_votes[x]})')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(f'Election winner: {election_winner.upper()}')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')




Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
