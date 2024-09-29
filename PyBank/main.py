#importing libraries required for this assignment (1)
import os
import csv

#defining a function to count the number of months in a csv object (3)
def month_counter(x):

    count = 0
    for i in x:
        count += 1

    return count

#defining a function to add the profit and loss recorded in each row of a csv object, and return the sum as an integer (3)
def profit_counter(x):

    profit = 0
    for i in x:
        profit = profit + int(i[1])

    return profit

#defining a function to return the average of change between data points in a list
def average_change(x):

    #creating a list object containing values from iterable input, using list comprehension (4)
    rawValues = [int(value[1]) for value in x]

    #iterating over rawValues, starting with index 1. Evaluating the difference between to list items, and adding those to a new list.
    changevalues = [(rawValues[n]-rawValues[(n-1)]) for n in range(1, len(rawValues))]

    #adding together all values in changevalues, for calculating average.
    sum_change = 0
    for i in changevalues:
        sum_change += i

    #calculating the average of changes between items in changevalues. Using round() to limit the output value to two decimal palces (5)
    average_change = round((float((sum_change / len(changevalues)))),2)

    return(average_change)




#defining a function to identify and return the greatest increase value in a list composed of lists with two entries (sample list item: [str, int]).
def greatest_increase(x):

    rawValues = [int(value[1]) for value in x]
    changevalues = [(rawValues[n] - rawValues[(n - 1)]) for n in range(1, len(rawValues))]
    #creating a new list of only string values, extracted from the first index of each list item in the list passed into the function.
    string_value = [value[0] for value in x]

    #initializing variables. The first variable is a string value, the second is stored as a string and converted into int.
    value = 0
    value_pair = " "

    for i in range(len(changevalues)):

        #conditional to evaluate if value in list is greater than the stored value
        if int(changevalues[i]) > value:
            value = int(changevalues[i])
            value_pair = string_value[(i+1)]

    #function returns two values (7)
    return value, value_pair



#defining a function to identify and return the greatest decrease value in a list composed of lists with two entries (sample list item: [str, int]).
def greatest_decrease(x):

    rawValues = [int(value[1]) for value in x]
    changevalues = [(rawValues[n] - rawValues[(n - 1)]) for n in range(1, len(rawValues))]
    # creating a new list of only string values, extracted from the first index of each list item in the list passed into the function.
    string_value = [value[0] for value in x]

    #initializing variables. The first variable is a string value, the second is stored as a string and converted into int.
    value = 0
    value_pair = " "

    for i in range(len(changevalues)):

        #conditional to evaluate if value in list is less than the stored value
        if int(changevalues[i]) < value:
            value = int(changevalues[i])
            value_pair = string_value[(i+1)]

    #function returns two values (7)
    return value, value_pair


#using the os library to create a path object, which I will use when opening a csv file (1)
input_path = os.path.join('Resources', 'budget_data.csv')

#opening the indicated csv file using path object and read mode (1)
with open (input_path, 'r') as datafile:

    #creating parsable csv data object csvreader (1)
    csvreader = csv.reader(datafile, delimiter= ',')

    #storing the csv headers in the header object using the next() funtion, to prevent the headers from being parsed with the rest of the csv data (1)
    header = next(csvreader)

    #offloading the csvreader object into a list, so that the data can be iterated over more than once. (6)
    csvdata = list(csvreader)

    #the following block of code creates variables and sets their values using the functions defined above.
    #the following block also writes the values of the variables to the terminal.
    print("")
    print("Financial Analysis")
    print("------------------------------------")

    total_months = month_counter(csvdata)
    print(f"Total Months: {total_months}")

    total_profit = profit_counter(csvdata)
    print(f"Total: ${total_profit}")

    avg_change = average_change(csvdata)
    print(f"Average Change: {avg_change}")

    greatest_increase, greatest_increase_date = greatest_increase(csvdata) #(6)
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")

    greatest_decrease, greatest_decrease_date = greatest_decrease(csvdata) #(6)
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

    print("------------------------------------")


output_path = os.path.join('analysis', 'analysis.txt')

#outputing the variables set in the read block above. The output is written to a txt file in the "PyBank/analysis" folder (7)
with open (output_path, "w") as output_txt:
    #writing indiviual lines to the txt file. "\n" is used to move to a new line before the next write() call. (7)
    output_txt.write("Financial Analysis" + "\n")
    output_txt.write("-------------------------" + "\n")
    output_txt.write(f"Total Months: {total_months}" + "\n")
    output_txt.write(f"Total: ${total_profit}" + "\n")
    output_txt.write(f"Average Change: {avg_change}" + "\n")
    output_txt.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})" + "\n")
    output_txt.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})" + "\n")




