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
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    OTooley_votes = 0
    

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
    print(np.unique(x))
print("The complete list of candidates who received votes:")
unique(candidates)
print("----------------------------")

# Calculate how many votes each candidate received.
for x in candidates:
    if x == "Khan":
        Khan_votes += 1
    elif x == "Correy":
        Correy_votes += 1
    elif x == "Li":
        Li_votes += 1
    elif x == "O'Tooley":
        OTooley_votes += 1
#print(f"{Khan_votes}")
#print(f"{Correy_votes}")
#print(f"{Li_votes}")
#print(f"{OTooley_votes}")

# Calculate the percentage of votes each candidate won.
Khan_percent = round(float(int(Khan_votes) / int(total_votes))*100, 4)
#print(f"{Khan_percent}")
Correy_percent = round(float(int(Correy_votes) / int(total_votes))*100, 4)
#print(f"{Correy_percent}")
Li_percent = round(float(int(Li_votes) / int(total_votes))*100, 4)
#print(f"{Li_percent}")
OTooley_percent = round(float(int(OTooley_votes) / int(total_votes))*100, 4)
#print(f"{OTooley_percent}")




    




# Print analysis 
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")    
print("----------------------------")
print(f"Khan: {Khan_percent}% ({Khan_votes})")
print(f"Correy: {Correy_percent}% ({Correy_votes})")
print(f"Li: {Li_percent}% ({Li_votes})")
print(f"O'Tooley: {OTooley_percent}% ({OTooley_votes})")
print("----------------------------")
print(f"Winner: ")
print("----------------------------")


