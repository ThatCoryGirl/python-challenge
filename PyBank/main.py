import os
import csv

#Buckets/Lists to store data
months = []
profits_losses = []
changes = []

#Connecting the CSV with the main.py file from the PyBank Folder, os.path.join did not work for me.
csvpath = os.path.normpath('c:/Users/CoryChapman/Desktop/dataanalytics/ModuleChallenges/Module3/python-challenge/PyBank/Resources/budget_data.csv' )

#Printing header
print("Financial Analysis")
print("--------------")

#Telling how the CSV file should be read and set up, with delimiter and variable that holds contents
with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        months.append(row[0])
        profits_losses.append(int(row[1]))
    
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
           #print(f'\t{row[0]} profits or losses') - don't need
            line_count += 1
print(f'Total Months: {line_count} ')

#Sum as a function
def csv_total(brr):
    total = 0
    with open(brr) as a:
        csv_reader = csv.reader(a)
        csv_header = next(csv_reader)

        for line in csv_reader:
            total += int(line[1])
            
    return total
total = csv_total(csvpath)
print(f"Total: ${total}")

    
def csv_total(st):
    total = 0
    with open(st) as a:
        csv_reader = csv.reader(a)
        csv_header = next(csv_reader)

#Calculate average change here    
for i in range (1, len(months)):
        change = profits_losses[i]-profits_losses[i-1]
        changes.append(change)
        
        average_change = sum(changes)/len(changes)

print(f"Average Change is {average_change:.2f}")

#Calculate Greatest increase in profits over the entire period (date and month)    
for j in range (1, len(months)):
    greatest_increase = max(changes)
    greatest_increase_date = months[changes.index(greatest_increase)+ 1]

print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")

#Calculate Greatest decrease in profits over the entire period (date and month)
for k in range (1, len(months)):
    greatest_decrease = min(changes)
    greatest_decrease_date = months[changes.index(greatest_decrease)+ 1]

print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
