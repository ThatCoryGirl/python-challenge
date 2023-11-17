#Importing csv file for all operating systems to read
import csv
import os

# This is the csv pathing that worked for me
csvpath = os.path.normpath('c:/Users/CoryChapman/Desktop/dataanalytics/ModuleChallenges/Module3/python-challenge/PyPoll/Resources/election_data.csv' )


# Created Bucket/Lists to store the data
candidate_roster = []
voter_counts = []
vote_percentage = []
total_votes = 0
winner_count = 0
Winner = ""

# This is for opening the csv file as a written file with commas delimiters
with open(csvpath, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=",")

    # Printing Result Headers
    Headers = next(reader)
    # This is a for loop which will write and figure the total number of votes cast
    for row in reader:
        total_votes += 1
    
        # This is how we will store unique roster names
        if row[2] not in candidate_roster:
            candidate_roster.append(row[2])
            voter_counts.append(1)
        else:
            CandidateIndex = candidate_roster.index(row[2])
            voter_counts[CandidateIndex] += 1

#I am changing the decimal point into a percentage value        
def fixPercent(num):
    num = "{:.3%}".format(num)
    return num

#This is how I am calculating the percentage of votes for each roster candidate
for i in range(len(voter_counts)):
    vote_percentage.append(voter_counts[i] / total_votes)

#I am calculating the winner with the most votes
for j in range(len(voter_counts)):
    if voter_counts[j] > winner_count:
        winner_count = voter_counts[j]
        Winner = candidate_roster[j]

analysisfile = os.path.join("Analysis", "pypoll_analysis.txt")

#These are the written results that go onto the Analysis text file
with open(analysisfile, 'w') as pypoll_analysis:
    pypoll_analysis.write(f"Election Results\n"
        f"----------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"----------------------------\n")

    #This is a for loop to calculate candidate roster percentages of votes
    for i in range(len(candidate_roster)):
        pypoll_analysis.write(f"{candidate_roster[i]}: {fixPercent(vote_percentage[i])} ({voter_counts[i]})\n")

    pypoll_analysis.write(f"----------------------------\n"
        f"Winner: {Winner}\n"
        f"----------------------------\n")
    
#This is for reading of the new file
with open (analysisfile, 'r') as analysis:
    contents = analysis.read()
    print(contents)




