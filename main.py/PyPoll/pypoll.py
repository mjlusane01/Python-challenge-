import csv

store_list = list()
ballot_dictionary = dict()

csv_file = open("election_data.csv")
data = csv.reader(csv_file)
for row in data:
	store_list.append(row)
csv_file.close()

# now I have all the data stored in the store_list
# remove the data that is not legit, the header and the last line
store_list = store_list[1: len(store_list)-1]

# the data style:
# ['1005842', 'Jefferson', 'Charles Casper Stockham']
for i in store_list:
	name = i[2]
	if name not in ballot_dictionary:
		ballot_dictionary.update({name: 1})
	else:
		ballot_dictionary.update({name: ballot_dictionary[name] + 1})

# dict: {'Charles Casper Stockham': 76911, 'Diana DeGette': 31317, 
#         'Raymon Anthony Doane': 1169}

total = 0
for i in ballot_dictionary:
	total = total + ballot_dictionary[i]


charles = ballot_dictionary["Charles Casper Stockham"] / total 
diana = ballot_dictionary["Diana DeGette"] / total 
raymon = ballot_dictionary["Raymon Anthony Doane"] / total 

# find the winner
ballot_max = max(ballot_dictionary.values())
winner = ""
for i in ballot_dictionary:
	if ballot_dictionary[i] == ballot_max:
		winner = i

#===============================================================================
#==output the result============================================================
print("Election Results")
print("-----------------------")
print(f"Total Votes: {total}")
print("------------------------")
print(f"Charles Casper Stockham: {charles: 7.3%} ({ballot_dictionary['Charles Casper Stockham']})")
print(f"Diana Degette: {diana: 7.3%} ({ballot_dictionary['Diana DeGette']})")
print(f"Raymon Anthony Doane: {raymon: 7.3%} ({ballot_dictionary['Raymon Anthony Doane']})")
print("-------------------------------------------------------------------------")
print(f"Winner: {winner}")

output_pypoll = open("output_pupoll.txt", "w")

output_pypoll.write("Election Results\n")
output_pypoll.write("-----------------------\n")
output_pypoll.write(f"Total Votes: {total}\n")
output_pypoll.write("------------------------\n")
output_pypoll.write(f"Charles Casper Stockham: {charles: 7.3%} ({ballot_dictionary['Charles Casper Stockham']})\n")
output_pypoll.write(f"Diana Degette: {diana: 7.3%} ({ballot_dictionary['Diana DeGette']})\n")
output_pypoll.write(f"Raymon Anthony Doane: {raymon: 7.3%} ({ballot_dictionary['Raymon Anthony Doane']})\n")
output_pypoll.write("-------------------------------------------------------------------------\n")
output_pypoll.write(f"Winner: {winner}\n")

output_pypoll.close()



