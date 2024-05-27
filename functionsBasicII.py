#Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countdown(n):
    list = []
    for i in range(n,-1,-1):
        list.append(i)
    return list
print(countdown(5))
#Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def print_and_return([x,y]):
    print(x)
    return y

