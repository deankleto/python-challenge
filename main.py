import os
import csv

csvpath = os.path.join("//Users//deankleto//Desktop//python-challenge//**PyBank**//budget_data.csv")

total = 0

number_of_months = 0


# Open and read csv
with open(csvpath, newline="", errors='ignore') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    reader=next(csvreader)

    for row in csv.reader(csvfile):
        
        total+= int(row[1])

        number_of_months +=1

        average_changes = 1

        #Struggled to get this to work
        greatest_increase = 1

        greatest_decrease = 1


    


print("Total Number of Months: ", + number_of_months)

print("Net Total Amount:  $", + total)

print("Average Changes in Net Total Amount: ", + average_changes / number_of_months)

#Could not figure out the syntax to pull max number
print("Greatest Increase: ", + greatest_increase)

#Could not figure out the syntax to pull min number
print("Greatest Decrease", + greatest_decrease)





