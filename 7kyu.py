# Make a function that an take any non-negative integer as an argument and return it with its digits in descendin order
# def descending_order(num):
#     numbr = str(num)
#     first_list = list(numbr)
#     first_list.sort(reverse = True)
    
#     newstr = ''.join([str(i) for i in first_list])
#     newstr = int(newstr)
#     return newstr

# Return the number (count) of vowels in the given string. 
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.
# def get_count(input_str):
#     num_vowels = 0
#     vowels = ['a', 'e', 'i', 'o', 'u']
    
#     char_list = list(input_str)
    
#     for i in char_list:
#         for j in vowels:
#             if i == j:
#                 num_vowels += 1
#             else:
#                 num_vowels += 0
    
#     return num_vowels

# Square every digit of a number and concatenate them. For example, 
# if we run 9119 through the function, 811181 will come out, because 
# 9 squared is 81 and 1 squared is 1.
# def square_digits(num):
    
#     num = str(num)  #turn integer into string
#     new_list = list(num)  #put every integer into a list
#     final_list = []  #initialize empty list
    
#     for i in new_list:
#         i = int(i)    #turn item in list into an integer
#         squared = i*i    #square int
#         final_list.append(squared)    #add new num to empty list
    
#     final_int = int(''.join([str(j) for j in final_list])) #make string out of final list and convert to int type
    
#     return final_int

# Friday 13th or Black Friday is considered as unlucky day. 
# Calculate how many unlucky days are in the given year.
# Find the number of Friday 13th in the given year.
# input: integer
# output: integer
import datetime
def unlucky_days(year):
    #initialize count of friday 13ths
    fridays = 0
    
    #set start of the year
    first = datetime.date(year, 1, 1)
    
    #set end date
    last = datetime.date(year, 12, 31)
    
    #set time to be changed by
    delta = datetime.timedelta(days = 1)
    
    while first <= last:
        if first.weekday() == 4 and first.day ==13:
            fridays += 1
        first += delta
    
    
    return fridays