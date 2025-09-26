# Revise the script you wrote for Task 3: Write a script to find the minimal and maximal in the 
# Assignment of Module 03, transform it into three functions
# This script is designed to find the minimal and maximal of a sequence of numbers using functions

#We ask the user to input the numbers used in the min-max finder
def get_a_list_of_numbers(*args):
    try:
        list_of_numbers = [float(x) for x in args]
        print(list_of_numbers)
    except ValueError:
        raise ValueError(f"Invalid input: '{args}' include a non valid number.")  
    return list_of_numbers

#We define a function that finds the minimum number in the list of numbers
def find_min(list_of_numbers):
    """We define a function to find the min in the list of numbers"""
    if list_of_numbers == "": 
        min_value = "None"
    
    list_of_numbers.sort() 
    min_value = list_of_numbers[0]
    return min_value

#We define a function that finds the maximum number in the list of numbers
def find_max(list_of_numbers):
    """We define a function to find the max in the list of numbers"""
    if list_of_numbers == "": 
        max_value = "None"

    list_of_numbers.sort() 
    items_in_list = len(list_of_numbers)
    max_value = list_of_numbers[items_in_list-1]
    return max_value