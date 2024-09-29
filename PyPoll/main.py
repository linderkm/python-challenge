import os
import csv

import_path = os.path.join('Resources', 'election_data.csv')

with open (import_path, 'r') as datafile:

    csvreader = csv.reader(datafile, delimiter = ',')
    header = next(csvreader)
    data = list(csvreader)


vote_count = 0
candidate1_count = 0
candidate2_count = 0
candidate3_count = 0


winner = ""


for i in range(len(data)):

    if data[i][2] == "Charles Casper Stockham":
        candidate1_count += 1
        vote_count += 1
    elif data[i][2] == "Diana DeGette":
        candidate2_count += 1
        vote_count += 1
    elif data[i][2] == "Raymon Anthony Doane":
        candidate3_count += 1
        vote_count += 1


candidate1_percentage = (candidate1_count / vote_count) * 100
candidate2_percentage = (candidate2_count / vote_count) * 100
candidate3_percentage = (candidate3_count / vote_count) * 100

winner = " "

if candidate1_count > candidate2_count and candidate3_count:
    winner = "Charles Casper Stockham"
elif candidate2_count > candidate1_count and candidate3_count:
    winner = "Diana DeGette"
elif candidate3_count > candidate1_count and candidate2_count:
    winner = "Raymon Anthony Doane"

print(" ")
print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {vote_count}")
print("----------------------------------------")
print(f"Charles Casper Stockham: {round(candidate1_percentage, 3)}% ({candidate1_count})")
print(f"Diana DeGette: {round(candidate2_percentage, 3)}% ({candidate2_count})")
print(f"Raymon Anthony Doane: {round(candidate3_percentage, 3)}% ({candidate3_count})")
print("----------------------------------------")
print(f"Winner: {winner}")
print("----------------------------------------")
print(" ")



output_path = os.path.join('Analysis', 'analysis.txt')
with open (output_path, 'w') as file:
    file.write("Election Results" + "\n")
    file.write("----------------------------------" + "\n")
    file.write(f"Total Votes: {vote_count}" + "\n")
    file.write("----------------------------------" + "\n")
    file.write(f"Charles Casper Stockham: {round(candidate1_percentage, 3)}% ({candidate1_count})" + "\n")
    file.write(f"Diana DeGette: {round(candidate2_percentage, 3)}% ({candidate2_count})" + "\n")
    file.write(f"Raymon Anthony Doane: {round(candidate3_percentage, 3)}% ({candidate3_count})" + "\n")
    file.write("----------------------------------" + "\n")
    file.write(f"Winner: {winner}" + "\n")
    file.write("----------------------------------" + "\n")



