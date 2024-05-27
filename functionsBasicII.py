#Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
print("Problem #1")
def countdown(n):
    list = []
    for i in range(n,-1,-1):
        list.append(i)
    return list
print(countdown(5))
#Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
print("Problem #2")
def print_and_return(lst):
    print(lst[0])
    return lst[1]

print(print_and_return([2,4]))

#First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
print("Problem #3")
def first_plus_length(lst):
    return int(lst[0])+int(len(lst))
print(first_plus_length([1,2,3,4,5]))

#Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
print("Problem 4")
def values_greater_than_second(x):
    empty_array = []
    n=0
    if len(x)>1:
        for i in range(0,len(x),1):
                if (x[1] < x[i]):
                    empty_array.append(x[i])
                    n += 1
        print(n)
        return empty_array
    else:
        return False
    
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([5]))

#This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value
print("Problem 5")
def length_and_value(x,y):
    empty_list = []
    for i in range(x):
        empty_list.append(y)
    return empty_list
print(length_and_value(4,7))
print(length_and_value(6,2))