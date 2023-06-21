#In the arguments module add these two functions;
#A function named concatenate_args that takes any
# number of string arguments in positional arguments format and concatenates them into a single string
#A function named concatenate_kwargs that takes any number of string arguments in keyword arguments  format and concatenates them into a single string


def concatenate_args(*string,sep ="/"):
    return sep.join(args)
    
# Write a Python function that returns the Nth Fibonacci number.
//leap year
year = int(input("Enter a year: "))  
 #Getting value for user 
if (year % 4) == 0:  
   if (year % 100) == 0:  
       if (year % 400) == 0:  
           print("{0} is a leap year".format(year))  
       else:  
           print("{0} is not a leap year".format(year))  
   else:  
       print("{0} is a leap year".format(year))
       # Number will be printed as leap year
else:  
   print("{0} is not a leap year".format(year))
   #Number will be printed as Non Leap Year




# Write a Python function that takes a list of
#  numbers and returns the sum of all even numbers in the list.

def summ(*nums):
    answer=0
    for num in nums:
        if(num%2==0)
        answer+=num
    return answer


# Write a Python function that takes two strings and returns True if they are anagrams, False otherwise.
# Write a Python function that takes a string and returns the reverse of the string.
# Write a Python function that takes a list of strings and returns the longest string in the list.
# Write a Python function that takes a list of integers and returns the second largest number in the list.
# Write a Python function that takes a string and returns True if the string is a palindrome, False otherwise.
# Write a Python function that takes a list of integers and returns the sum of all the numbers in the list.
# Write a Python function that takes a list of numbers and returns the product of all the numbers in the list.
# Write a Python function that takes a list of strings and returns the number of strings in the list that contain the substring 'abc'.
# Write a Python function that takes a list of integers and returns the difference between the maximum and minimum numbers in the list.
# Write a Python function that takes a list of integers and returns a new list with only the even numbers from the original list.
# Write a Python function that takes a list of integers and returns a new list with only the odd numbers from the original list.
# Write a Python function that takes a list of strings and returns a new list with only the strings that start with the letter 'a'.
# Write a Python function that takes a list of strings and returns a new list with the strings sorted in alphabetical order.
# Write a Python function that takes a list of integers and returns a new list with the numbers sorted in descending order.
# Write a Python function that takes a list of integers and returns a new list with the numbers sorted in ascending order.
# Write a Python function that takes a list of strings and returns a new list with the strings sorted in reverse alphabetical order.
# Write a Python function that takes a list of integers and returns True if the list is sorted in ascending order, False otherwise.
# Write a Python function that takes a list of integers and returns True if the list is sorted in descending order, False otherwise.