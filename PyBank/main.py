import csv
import os
csvpath = os.path.join("..",'Resources','budget_data.csv')
outpath = "output.txt"

total_profitloss = 0
date = [0]
profit = [1]
total_change = 0
change = 0

print("Financial Analysis")
print("-------------------------------")

with open(csvpath, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #print(csvreader)
    #print(f"CSV Header:{csv_header}")
    rowcount = 0

    for row in csvreader:
        rowcount = rowcount + 1 
    print("Total Months: " + str(rowcount))

with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader: 
        total_profitloss = total_profitloss + int(row[1])
    print("Total: " + "$" + str(total_profitloss))
change_list = []
month_list = []

with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    first_row = next(csvreader)
    previous = int(first_row[1])
    
    for row in csvreader:     
        change = int(row[1]) - previous
        change_list.append(change)
        month_list.append(row[0])
        #print(change)
        total_change = total_change + change
        #print(total_change)
        avg_change = total_change / (rowcount - 1)
        previous = int(row[1])
    print(f"Average Change: ${avg_change:.2f}")
   
    # print(max(change_list))
    max_change = max(change_list)
    max_index = change_list.index(max_change)
    print(f"Greatest Increase in Profits: {month_list[max_index]} (${max_change})")

    min_change = min(change_list)
    min_index = change_list.index(min_change)
    print(f"Greatest Decrease in Profits: {month_list[min_index]} (${min_change})")
    


with open(outpath, 'w') as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"----------------------------\n")
    txtfile.write(f"Total Months: {rowcount}\n")   
    txtfile.write(f"Total: ${total_profitloss}\n")
    txtfile.write(f"Average Change: ${avg_change:.2f}\n") 
    txtfile.write(f"Greatest Increase in Profits: {month_list[max_index]} (${max_change})\n")   
    txtfile.write(f"Greatest Decrease in Profits: {month_list[min_index]} (${min_change})") 