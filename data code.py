import.csv

f = open("Cars20192014.csv", newline = '')
header = next(reader)#Turns the csv file into a list of the contents in the csv file.

dataListed = [row for row in reader]#This line will print the code.

print("The first row is ", (dataListed[0]))#This will now pick the first row and print the elements

print("Just one element is", (dataListed[0])[0])#This line will print the element in that first row.

f.close()