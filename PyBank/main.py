# Import the os module to create file path.
import os

# Import module for reading CSV files
import csv

# Set file path to .csv
csvpath = os.path.join('Resources', 'budget_data.csv')

# Calculate the total number of months included in the dataset.
    # Define the functions
def budget_data(by_month):
    month = str(by_month[0])
    profit_loss = int(by_month[1])

# Open the .csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Make sure the file path is set up correctly(confirmed).
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")


    # Print header of financial analysis
    print("Financial Analysis")
    print("--------------------------------")

    

        
    print("Total Months: " + str(len(month)))
    print(month)
    










