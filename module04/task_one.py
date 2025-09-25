#In this script we call the functions defined in MyModule and run function to determine min and max values

#We import the module with our defined functions
import MyModule

#We call the number list function and create a list of numbers
number_list = MyModule.get_a_list_of_numbers()

#Using the fin_min function we find the minimum value in the list of numbers
min = MyModule.find_min(number_list)

#Using the fin_min function we find the maximum value in the list of numbers
max = MyModule.find_max(number_list)

#We print the output of the script
print(f"The list of number is: {number_list}")
print(f"The minimal number is: {min}")
print(f"The maximal number is: {max}")
