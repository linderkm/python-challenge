import os
import csv

#creating a path object (1)
import_path = os.path.join('Resources', 'election_data.csv')
#opening and reading a csv file ('election_data.csv') located in the PyPoll/Resources folder (1)
with open (import_path, 'r') as datafile:
    #creating a iterable csv object (1)
    csvreader = csv.reader(datafile, delimiter = ',')
    #removing the first row (headers) in the csv, offloading it into a variable using next() (1)
    header = next(csvreader)
    #offloading csvreader data into a list object that can be iterated over more than once (2)
    data = list(csvreader)

#initializing variables, and setting their initial values.
vote_count = 0
candidate1_count = 0
candidate2_count = 0
candidate3_count = 0


#loop to go over each line of the csv data (3)
for i in range(len(data)):

    #conditional to check if string matches specific candidate's name. If there's a match, update the total vote count variable and respective candidate's counter variable. (4)
    if data[i][2] == "Charles Casper Stockham":
        candidate1_count += 1
        vote_count += 1
    #conditional to check if string matches specific candidate's name. If there's a match, update the total vote count variable and respective candidate's counter variable. (4)
    elif data[i][2] == "Diana DeGette":
        candidate2_count += 1
        vote_count += 1
    #conditional to check if string matches specific candidate's name. If there's a match, update the total vote count variable and respective candidate's counter variable. (4)
    elif data[i][2] == "Raymon Anthony Doane":
        candidate3_count += 1
        vote_count += 1


#creating variables to store calculated percentage values
candidate1_percentage = (candidate1_count / vote_count) * 100
candidate2_percentage = (candidate2_count / vote_count) * 100
candidate3_percentage = (candidate3_count / vote_count) * 100

#initialzing variable to store the name of the winning candidate.
winner = " "
#conditional that compares the values of candidate  vote count variables (4)
if candidate1_count > candidate2_count and candidate3_count:
    winner = "Charles Casper Stockham"
elif candidate2_count > candidate1_count and candidate3_count:
    winner = "Diana DeGette"
elif candidate3_count > candidate1_count and candidate2_count:
    winner = "Raymon Anthony Doane"

#block of code that prints the results to the terminal.
print(" ")
print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {vote_count}") #using fstring to integrate a variable into the print statement (5)
print("----------------------------------------")
print(f"Charles Casper Stockham: {round(candidate1_percentage, 3)}% ({candidate1_count})") #rounding variables to three decimal points (6)
print(f"Diana DeGette: {round(candidate2_percentage, 3)}% ({candidate2_count})")
print(f"Raymon Anthony Doane: {round(candidate3_percentage, 3)}% ({candidate3_count})")
print("----------------------------------------")
print(f"Winner: {winner}")
print("----------------------------------------")
print(" ")


#outputting the findings to analysis.txt, stored in python-challenge/PyPoll/analysis (7)
output_path = os.path.join('Analysis', 'analysis.txt')
with open (output_path, 'w') as file:
    file.write("Election Results" + "\n") #using "\n" to force the next line of text to be written on the next line in the .txt file (7)
    file.write("----------------------------------" + "\n")
    file.write(f"Total Votes: {vote_count}" + "\n")
    file.write("----------------------------------" + "\n")
    file.write(f"Charles Casper Stockham: {round(candidate1_percentage, 3)}% ({candidate1_count})" + "\n")
    file.write(f"Diana DeGette: {round(candidate2_percentage, 3)}% ({candidate2_count})" + "\n")
    file.write(f"Raymon Anthony Doane: {round(candidate3_percentage, 3)}% ({candidate3_count})" + "\n")
    file.write("----------------------------------" + "\n")
    file.write(f"Winner: {winner}" + "\n")
    file.write("----------------------------------" + "\n")



