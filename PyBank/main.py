# Import the os module to create file path.
import os

# Import module for reading CSV files
import csv

# Set file path to .csv
csvpath = os.path.join('..','Resources', 'budget_data.csv')

# Open the .csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")





