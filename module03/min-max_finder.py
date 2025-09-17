# Write a script to find the minimal and maximal
# This script is designed to find the minimal and maximal of a sequence of numbers

#We ask the user to input the numbers used in the min-max finder
number_list = input("Type numbers separated by spaces:")

#We make sure that the input is a list of numbers and not string variables
number_list = number_list.split()            
number_list = [int(num) for num in number_list]  

#We sort the list of numbers so it would be easy to extract the highest and lowest number in the list.
number_list.sort() 

#defining the number of numbers in the list
items_in_list = len(number_list)

#In this function we find the maximum and minimum value in the list of numbers
if number_list == "": 
    min_value = "None"
    max_value = "None"
else:  
    min_value = number_list[0]
    max_value = number_list[items_in_list-1]

#Output of the script
print("The list of number is:", number_list)
print("The minimal number is:", min_value)
print("The maximal number is:", max_value)








