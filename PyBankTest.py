# create a path to collect csv from the Resources folder

import os
import csv

pybankdata = os.path.join('..', 'Resources', 'budget_data.csv')

# declare variables
months = 0
total_profloss = 0
change = 0
total_change = 0
max_increase = 0
max_decrease = 0
profloss_change_count = []

# create the function
with open(pybankdata, 'r') as csvfile:

   csv_reader = csv.reader(csvfile, delimiter=',')

   csv_header = next(csv_reader)
   previous_profloss = next(csv_reader)
   # use the following to make sure that the top two rows (header included) are being generated
   # print(csv_header)
   # print(previous_p_l)

   # because this needs to be turned into an int later, name it something different from the mutable variable
   previous_profloss_value = previous_profloss[1]

   for row in csv_reader:
           # each row will add 1 to the months count
           months += 1

           # add numbers from Profit/Losses column
           total_profloss += int(row[1])

           # track change from one row to the next in the profloss column
           change = int(row[1]) - int(previous_profloss_value)
           total_change += change

           # reset the 'current profloss' to whatever is currently in column 1 of the row being iterated
           previous_profloss = int(row[1])

            # Test:
            # print(months)
            # print(total_change)
            # print(total_profloss)

            # check if the difference between one cell to the next is bigger than any difference seen before
            # the max_increase will be row 2, column 2 at the start
           if(change > max_increase):
               max_increase = change
               # use a string because column 1 contains letters
               max_increase_date = str(row[0])
           if(change < max_decrease):
               max_decrease = change
               max_decrease_date = str(row[0])

# '2' because we only want to show to spaces beyond the decimal
average_change = round(total_change / (months), 2)

print("------------------")
print("Financial Analysis")
print("------------------")
print(f"Months in Dataset: {str(months)}")
print(f"Net Total of Profits/Losses: ${str(total_profloss)}")
print(f"Average Change Per Month: ${str(average_change)}")
print(f"Max Increase in Profits: {str(max_increase_date)} (${str(max_increase)})")
# technically, the homework assignment says to find the 'greatest decrease in losses' but I think they meant the greatest increase in losses
print(f"Max Increase in Losses: {str(max_decrease_date)} (${str(max_decrease)})")


   
  
           