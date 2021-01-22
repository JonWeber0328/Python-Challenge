# Import the os module to create file path.
import os

# Import module for reading CSV files.
import csv

# Import module to get unique values in list.
import numpy as np

# Set file path to .csv
csvpath = os.path.join('Resources', 'election_data.csv')
#print(csvpath)

# Open the .csv
with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    election_data=csv.reader(csvfile, delimiter=",")
    #print(election_data)

    # Set header line
    header = next(election_data)
    #print(f"{header}")
    
    # Define the variables
    total_votes = 0
    candidates = []
    
    

    # Loop through the rows to find the total number of votes.
    for i in election_data:

        # Count the number of rows
        total_votes += 1
    #print(total_votes)

        # get list of all candidate names
        candidates.append(str(i[2]))
    
# Print a complete list of candidates who received votes
# Function found on geeksforgeeks.org/python-get-unique-values-list/
def unique(candidates):
    x = np.array(candidates)
    #print(np.unique(x))
#print("The complete list of candidates who received votes:")
unique(candidates)


    




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


