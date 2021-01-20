# Import the os module to create file path.
import os

# Import module for reading CSV files
import csv

# Set file path to .csv
csvpath = os.path.join('Resources', 'budget_data.csv')
# Make sure the file path is set up correctly(confirmed).
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

# Open the .csv
with open(csvpath) as csv_file:

    # Split the data on commas
    budget_data = csv.reader(csv_file, delimiter=",")


    # Set header line
    header = next(budget_data)
    #print(f"{header}")

    # Define the variables
    net = 0
    date = []
    profit_loss = []
    
    # Loop through the rows to calculate profit/loss
    for row in budget_data:
        #print(rows)

        date.append(str(row[0]))
        profit_loss.append(int(row[1]))

        
        # Sum up net profit/loss
        row_net = int(row[1])
        net += row_net

        
        





# Print header of financial analysis
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {net}")
    


     
    










