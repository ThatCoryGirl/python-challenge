import os
import csv

#Buckets/Lists to store data
BallotID = []
County = []
Candidate = []

csvpath = os.path.normpath('c:/Users/CoryChapman/Desktop/dataanalytics/ModuleChallenges/Module3/python-challenge/PyPoll/Resources/election_data.csv' )

#Printing Result headers
print("Election Results")
print("------------------------")

with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    csv_header = next(csv_reader)

    for row in csv_reader:
        #print(row)
        line_count += 1
    print(f'Total Votes: {line_count} ')