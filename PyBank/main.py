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

    # Loop through the rows to find total months and total profit.
    for i in budget_data:
        #print(i)

        # Count the number of rows
        total_rows += 1

        # Find total of profit/loss column
        row_total = int(i[1])
        total += row_total

        # Find average change in profit/loss column
        # Look at profit/loss column and collect the data in a list.
        profit_loss.append(int(i[1]))
    
    #print(profit_loss)

# Use profit/loss column to find change from month to month.
# Define the variables
change_list = []

# Create new column for monthly change.
for x in profit_loss:
    prior_month = profit_loss[profit_loss.index(x) -1]
    change = x - prior_month
    change_list.append(int(change))
#print(change_list)

# First number is not accurate.
# Change first number to 0.
change_list=[0 if x==196785 else x for x in change_list]
#print(change_list)

# Find the average change
sum_change = sum(change_list)
average_change = round(float(int(sum_change) / int(85)), 2)
#print(average_change)

# Find the greatest increase in profits.
greatest_increase = max(change_list)
#print(greatest_increase)

# Find the greatest decrease in profits.
greatest_decrease = min(change_list)
print(greatest_decrease)

# Print financial analysis
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {total_rows}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change}")


     
    










