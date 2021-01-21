# Import the os module to create file path.
import os

# Import module for reading CSV files
import csv

# Set file path to .csv
csvpath = os.path.join('Resources', 'budget_data.csv')
# Make sure the file path is set up correctly(confirmed).
    
# Open the .csv
with open(csvpath) as csv_file:

    # Split the data on commas
    budget_data=csv.reader(csv_file, delimiter=",")
    #print(budget_data)

    # Set header line
    header = next(budget_data)
    #print(f"{header}")
    
    # Loop through the rows
    for row in budget_data:
        print(row)

        # Count the number of rows
        #total_rows += 1

        #date.append(str(row[0]))
        #profit_loss.append(int(row[1]))
        #print(date)
        
        # Sum up net profit/loss
        #row_net = int(row[1])
        #net = net + row_net

#total_months = len(date)
        
# Define the variables
total_rows = 0
net = 0
date = []
profit_loss = []




# Print header of financial analysis
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {total_rows}")
    


     
    










