# Import the os module to create file path.
import os

# Import module for reading CSV files
import csv

# Set file path to .csv
csvpath = os.path.join('Resources', 'budget_data.csv')
# Make sure the file path is set up correctly(confirmed).
    
# Open the .csv
with open(csvpath) as csvfile:

    # Split the data on commas
    budget_data=csv.reader(csvfile, delimiter=",")
    #print(budget_data)

    # Set header line
    header = next(budget_data)
    #print(f"{header}")
    
    # Define the variables
    total = 0
    total_rows = 0
    profit_loss = []

    # Loop through the rows
    for i in budget_data:
        #print(i)

        # Count the number of rows
        total_rows += 1

        # Find total of profit/loss column
        row_total = int(i[1])
        total += row_total






# Print header of financial analysis
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {total_rows}")
print(f"Total: ${total}")


     
    










