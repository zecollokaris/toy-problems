#############################################################################################################

######Question######

# Summation
# Write a program that finds the summation of every number between 1 and num. The number will always be a positive integer greater than 0.

# For example:

# summation(2) -> 3
# 1 + 2

# summation(8) -> 36
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8


#############################################################################################################
######BDD######

# 1. We have to first get the range between 1 and num-: range()
#     ##Note##
#     in range function it does not return the largest number in the range hence we will need to add one
#     #EXAMPLE#
#         NUMBERS BETWEEN (1 and 8),

#             We expect [1, 2, 3, 4, 5, 6, 7, 8]

#         ######################################

#         LETS USE -: range()

#             >>> range(1, 8)
#             We get  [1, 2, 3, 4, 5, 6, 7]

#             -: The last number   8<<== is missing when we use range

#         ######################################

#         >>>In this case we will use add +1 to get number 8 included in the list


# 2. We have to find the sum of numbers between 1 and num-: sum()

# 3. If sum is less than 0 we have to return 1-: (we will use an if statement in this case) 
#         #Example# 
#         if num < 0
#             return 1


# 4. Return summation (solution)
#############################################################################################################

###### Solution ######

def summation(num):
    summation = sum(range(1,num+1))
    if summation <= 0:
        summation = 1
    return summation

#############################################################################################################
#############################################################################################################