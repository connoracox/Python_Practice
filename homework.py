# Exercise 1
#Given a list as a parameter, write a function that returns a list of 
# numbers that are less than ten

#For example: Say your input parameter to the function is [1,11,14,5,8,9]
# ...Your output should [1,5,8,9]

#why doesn't this work?:

# def under_ten (numbers):
#     for item in numbers:
#         if item < 10:
#             return item

# SOLUTION:

def under_ten (numbers):
    return [item for item in numbers if item < 10]
   
numbers = [1,11,14,5,8,9]

print(under_ten(numbers))


# Exercise 2
# Write a function that takes in two lists and returns the two lists merged together and sorted
# Hint: You can use the .sort() method

list_1 = [1,2,3,4,5,6]
list_2 = [3,4,5,6,7,8,10]
list_3 = []

def ultra_list(list1, list2):
    list_3 = list1 + list2
    list_3.sort()
    return(list_3)

print(ultra_list(list_1, list_2))