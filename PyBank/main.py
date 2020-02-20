#Modules
import os
import csv

#creating an object out of the CSV file
budget_data = os.path.join('..', 'Resources', 'budget_data.csv')

#Opening and reading the CSV file
with open(budget_data, newline='') as csvfile:
    budget_reader=csv.reader(csvfile, delimiter= ",")
    #Skip header row
    next(budget_reader)

total_months=[]
total=[]
average_change=[]
greatest_increase=[]
greatest_decrease=[]

#Next from header row
csv_header= next(csvreader)

#Each row of data after the header
for row in budget_reader:
    total.append(row[0])
    #The total net amount of "Profit/Losses"
    total_pl=total_pl + int(row[1])
    #change 
    change=int(row[1])-value
    #Total number of months
    total_months += 1






