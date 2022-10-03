import csv

# create two empty lists for analysing
date_list = list()
profit_loss_list = list()

with open("budget_data.csv") as csv_file:
	# a csv.reader() create an object 
	# which can be iterated to many lists 
	data = csv.reader(csv_file)
	
	for row in data:
		date_list.append(row[0])
		profit_loss_list.append(row[1])

# remove the head and typecast the profit_loss_list
date_list = date_list[1:]
profit_loss_list = profit_loss_list[1:]
for i in range(len(profit_loss_list)):
	profit_loss_list[i] = int(profit_loss_list[i])


# create a change list to do the main calculation
change_list = list()
for i in range(1, len(profit_loss_list)):
	#print(int(profit_loss_list[i]))
	change = profit_loss_list[i] - profit_loss_list[i-1]
	change_list.append(change)


# ==============output part=======================================
# ================================================================
total_months = len(date_list)
total_amount = sum(profit_loss_list)
average_change = round(sum(change_list) / len(change_list), 2)
greatest_increase_amount = max(change_list)
greatest_increase_date = date_list[change_list.index(greatest_increase_amount) + 1]
greatest_decrease_amount = min(change_list)
greatest_decrease_date = date_list[change_list.index(greatest_decrease_amount) + 1]

print("Financial Analysis")
print("--------------------------------------")
print("Total Months:", total_months)
print("Total:$", total_amount)
print("Average Change:$",average_change, sep="")
print(f"Greatest Increase in Profits:{greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits:{greatest_decrease_date} (${greatest_decrease_amount})")

output_file = open("analysis report.txt", "w")
output_file.write("Financial Analysis\n")
output_file.write("--------------------------------------\n")
output_file.write(f"Total Months: {total_months}\n")
output_file.write(f"Total: ${total_amount}\n")
output_file.write(f"Average Change: ${average_change}\n")
output_file.write(f"Greatest Increase in Profits:{greatest_increase_date} (${greatest_increase_amount})\n")
output_file.write(f"Greatest Decrease in Profits:{greatest_decrease_date} (${greatest_decrease_amount})\n")	
output_file.close()	
