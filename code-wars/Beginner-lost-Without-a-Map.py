#####Question#####

# Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]

# For the beginner, try to use the map method - it comes in very handy quite a lot so is a good one to know.

####################################################################################################################

####BDD####

# 1. Return a list using list() method.

# 2.The Question need us to use map() so we will use map. 
#     -Map function applies a given function to each item of an iterable (which is to be mapped).

# 3. Since map() expects a function to be passed in, lambda functions are commonly used while working with map() functions.
#     hence we shall use lambda

# 4. Inside the lambda function we will need to multiply by 2 (*2)

####################################################################################################################

def maps (a):
    
    return list(map(lambda a : a*2 , a) )