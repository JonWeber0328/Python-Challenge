# Import the os module to create file path.
import os

# Import module for reading CSV files
import csv

# Set file path to .csv
csvpath = os.path.join('Resources', 'election_data.csv')
#print(csvpath)

# Open the .csv
with open(csvpath) as csvfile:

    # Split the data on commas
    election_data=csv.reader(csvfile, delimiter=",")
    #print(election_data)

    # Set header line
    header = next(election_data)
    print(f"{header}")
    
    # Define the variables
    total_votes = 0
    
    # Loop through the rows to find the total number of votes.
    for i in election_data:

        # Count the number of rows
        total_votes += 1
    #print(total_votes)

# Print analysis 
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")    
print("----------------------------")
print(f"Khan: ")
print(f"Corey: ")
print(f"Li: ")
print(f"O'Tooley: ")
print("----------------------------")
print(f"Winner: ")
print("----------------------------")


