#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
print("Problem1")
def biggie_size(x):
    lst = x
    for i in range(len(lst)):
        if lst[i] > 0:
            lst[i] = "big"
    return lst
print(biggie_size([-1, 3, 5, -5]))

#Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
#Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
print("Problem 2")
def count_positives(x):
    n=0
    lst = x
    for i in range(len(lst)):
        if lst[i]>=0:
            n += 1 
    lst[-1] = n # last element is -1 --> the one before is -2 and so on
    return lst
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

#Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
#Example: sum_total([1,2,3,4]) should return 10
#Example: sum_total([6,3,-2]) should return 7
print("Problem 3")
def sum_total(x):
    n=0
    for i in range(len(x)):
        n += x[i]
    return n
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))
#Average - Create a function that takes a list and returns the average of all the values.x
#Example: average([1,2,3,4]) should return 2.5
print("Problem 4")
def average(x):
    sum=0
    for i in range(len(x)):
        sum += x[i]
    avg = sum / len(x)
    return avg
print(average([1,2,3,4]))

#Length - Create a function that takes a list and returns the length of the list.
#Example: length([37,2,1,-9]) should return 4
#Example: length([]) should return 0
print("Problem 5")
def length(x):
    return len(x)
print(length([37,2,1,-9]))
print(length([]))
    
#Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#Example: minimum([37,2,1,-9]) should return -9
#Example: minimum([]) should return False
print("Problem 6")
def minimum(x):
    if len(x) == 0:
        return False
    min_value = x[0]  
    for i in x:
        print(i)
        if i < min_value:
            min_value = i  #
    
    return min_value
print(minimum([37,2,1,-9]))
print(minimum([]))

#Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
#Example: maximum([37,2,1,-9]) should return 37
#Example: maximum([]) should return False
print("Problem 7")
def maximum(x):
    if len(x) == 0:
        return False
    max_value = x[0]
    for i in x:
        if i > max_value:
            max_value = x
    return max_value
print(maximum([37,2,1,-9]))
print(maximum([]))