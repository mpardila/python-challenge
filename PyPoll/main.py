import os
import csv

# Path to collect data from the Resources folder
elections_csv = os.path.join ('Resources/election_data.csv')

# Read the CSV file and read the heather
with open (elections_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Lists and variables to store data
    votes = []
    candidates_dict = {}
   
    # Loop through the rows
    for row in csvreader:

        # For total number of votes cast
        votes.append(row)

        # A complete list of candidates who received votes
        candidate_name = row[2]
        if candidate_name not in candidates_dict:
            candidates_dict[candidate_name] = 1
        elif candidate_name in candidates_dict:
            candidates_dict[candidate_name] = candidates_dict[candidate_name] + 1

    # The total number of votes cast
    total_num_votes = len(votes)

    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(total_num_votes))
    print("----------------------------")

    most_votes = 0

    # The percentage of votes each candidate won
    for candidate in candidates_dict:
        print(f"{candidate}: {round((candidates_dict[candidate]/total_num_votes)*100, 2)}% ({candidates_dict[candidate]})")
        if candidates_dict[candidate] > most_votes:
            most_votes = candidates_dict[candidate]

    print("----------------------------")

    # The winner of the election based on popular vote
    for candidate in candidates_dict:    
        if most_votes == candidates_dict[candidate]:  
            print(f"Winner: {candidate}")
    print("----------------------------")

