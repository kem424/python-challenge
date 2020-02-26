#Modules
import os
import csv

#open CSV file
file=os.path.join("election_data.csv")
with open (file, 'r', newline= "") as csvfile:
    reader=csv.reader(csvfile, delimiter= ",")
    #skip header
    next(reader)

    #Iteration
    total_votes= 0
    percent_of_votes= 0.0
    winner_votes= 0
    winner=""
   
    khan_total= 0
    khan_percentage= 0.00
    correy_total=0
    correy_percentage= 0.00
    li_total= 0
    li_percent= 0.00
    o_tooley_total=0
    o_tooley_percent= 0.00
    candidates= []

    candidates=row[2]

#if candidate has other votes then add to vote tally
if candidate in candidates:
    candidate_index = candidates.index(candidate)
    vote_counts[candidate_index] = vote_counts[candidate_index] + 1
 #else create new spot in list for candidate
else:
    candidates.append(candidate)
    vote_counts.append(1)


    #loop the data
    #total_votes=len(candidate)
    for row in csvreader:
        total_votes += 1

    
    for row in candidate_list:
        if row[1]== winner:
            winner_name= row[0]



        khan_total= candidate.count('Khan')
        khan_percent=int(khan_total)/int(total_votes)*100

        correy_total=candidate.count('Correy')
        correy_percent= (correy_total/total_votes)*100

        li_total=candidate.count('Li')
        li_percent= (li_total/total_votes)*100

        o_tooley_total=candidate.count("O'Tooley")
        o_tooley_percent= (o_tooley_total/total_votes)*100

        #write the results to a dictionary array
        candidate_totals_percentage=[khan_percent,correy_percent,li_percent,o_tooley_percent]

        #print "max(candidates_totals_percentage) to calculate winner"
        winner=max(candidates_totals_percentage)
        


    

print("Election Results")
print("_________________")
print("Total:Votes:"+ str(total_votes))
print("_________________________")
print(f"Khan:{str(Khan_percent[0])}({str(khan_total)})")
print(f"Correy:{str(Correy_percent[0])}({str(Correy_total)})")
print(f"Li:{str(Li_percent[0])}({str(Li_total)})")
print(f"O'Tooley:{str(o_tooley_percent[0])}({str(o_tooley_total)})")
print("__________________________")
print("Winner:"+str(winner))
