#Modules
import os
import csv

#creating an object out of the CSV file
budget_data = os.path.join("Resources", "budget_data.csv")

#Opening and reading the CSV file
with open(budget_data, newline='') as csvfile:
    budget_reader=csv.reader(csvfile, delimiter= ",")
    #Skip header row
    header = next(budget_reader)

    total_months=0
    Greatest_Increase= ["", 0]
    Greatest_Decrease=["",1,000,000]
    total_change=0
    average_change=[]
    row_change=0
    total_pl = 0
#Next from header row
    first_row = next(budget_reader)
    # print(first_row)
    total_pl=total_pl+ int(first_row[1])
    row_change= int(first_row[1])
#Each row of data after the header
    for row in budget_reader:
        # total.append(row[0])
        #The total net amount of "Profit/Losses"
        total_pl=total_pl + int(row[1])
        #change 
        # change=int(row[1])-value
        #Total number of months
        total_months += 1
        total_change = int(row[1])- row_change 
        row_change= int(row[1])
        average_change.append(total_change)
        if total_change > Greatest_Increase[1]:
            Greatest_Increase[0]= row[0]
            Greatest_Increase[1]= total_change

        if total_change < Greatest_Decrease[1]:
            Greatest_Decrease[0]= row[0]
            Greatest_Decrease[1]= total_change 

print(average_change)

average_pl = (sum(average_change)/len(average_change))

# print(average_pl)

print("Financial Analysis")

# #Count of Total Months
print("Total_Months:" + str(total_months))

# #Total net amount of "Profit/Losses"
print("Total:$" + str(total_pl))

# #Average of changes in "Profit/Losses"
print("Average Change:$" +str(average_pl))

#Greatest Increase and Greatest Decrease in Profits
print(f"Greatest Increase in Profit:{Greatest_Increase[0]} ({Greatest_Increase[1]})")


print(f"Greatest Decrease in Profit:{Greatest_Decrease[0]} ({Greatest_Decrease[1]})")

bank=open("PyBank.text","w")
<<<<<<< HEAD
=======

bank.write("Financial Analysis")
bank.write("Total_Months:" + str(total_months))
bank.write("Total:$" + str(total_pl))
bank.write("Average Change:$" +str(average_pl))
bank.write(f"Greatest Increase in Profit:{Greatest_Increase[0]} ({Greatest_Increase[1]})")
bank.write(f"Greatest Decrease in Profit:{Greatest_Decrease[0]} ({Greatest_Decrease[1]})")
>>>>>>> ea0f11fdb31a1e643855d021e02195efd8a29670

bank.write("Financial Analysis")
bank.write("Total_Months:" + str(total_months))
bank.write("Total:$" + str(total_pl))
bank.write("Average Change:$" +str(average_pl))
bank.write(f"Greatest Increase in Profit:{Greatest_Increase[0]} ({Greatest_Increase[1]})")
bank.write(f"Greatest Decrease in Profit:{Greatest_Decrease[0]} ({Greatest_Decrease[1]})")





