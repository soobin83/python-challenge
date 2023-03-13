import csv
import os
csvpath = os.path.join("..",'Resources','election_data.csv')
outpath = "output.txt"

print("Election Results")
print("---------------------------------")

#open csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
#find the total number of rows, thus the total vote count
    rowcount = 0
   
    for row in csvreader:   
        # Add to the total vote count
        rowcount = rowcount + 1 
    print("Total Votes: " + str(rowcount))
    print("---------------------------------")

vote_list = []
winner_list = []

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    candidate_list = {}
    
    for row in csvreader:  
        candidate = str(row[2])
        # If the candidate does not match any existing candidate...
            # Add it to the list of candidates in the running
        if candidate not in candidate_list:
            candidate_list[candidate] = 1
        else:
            candidate_list[candidate] += 1
        

# calculate percentage
    for c in candidate_list:
        percentage = ((candidate_list[c])/rowcount)*100
        print(f"{c}: {percentage:.3f}% ({candidate_list[c]})")
        vote_list.append(candidate_list[c])
        winner_list.append(c)
    print("---------------------------------")
    
    #find the winner
    max_vote = max(vote_list)
    #print(max_vote)
    winner_index = vote_list.index(max_vote)
    print(f"Winner: {winner_list[winner_index]}")
    print("---------------------------------")

#export to a text file
with open(outpath, 'w') as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"----------------------------\n")
    txtfile.write(f"Total Votes: {rowcount}\n")   
    txtfile.write(f"----------------------------\n")
    for c in candidate_list:
        percentage = ((candidate_list[c])/rowcount)*100
        txtfile.write(f"{c}: {percentage:.3f}% ({candidate_list[c]})\n")
    txtfile.write(f"----------------------------\n")
    txtfile.write(f"Winner: {winner_list[winner_index]}\n") 
    txtfile.write(f"----------------------------\n")

