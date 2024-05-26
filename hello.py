print("Hello world")
name="Majd"
age = 27
x = "hello maajd"
print("My name is"+name) # + has no space
print("My name is",name) # see how this ( , ) provides a space
print(f"my name is {name} and i'm {age} years old") # with f : use {}
print("my name is {} and my age is {}".format(name,age)) # see how string.format() works

#------------------------------- below is old method
hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27
#---------------------------------

#: built in functions below
print(x.title()) ## this makes the first letter of every word capital ( as a title)
print(name.upper())
print(name.lower())
print(x.count('a')) # be3ed kam "a" in x
print(x.split()) #  returns a list of values where string is split at the given character. Without a parameter the default split is at every space
print(name.find('a')) #  returns the index of the start of the first occurrence of substring within string.
print(name.islower())
print(name.isupper())
print(name.isalnum())
print(str(age).isdigit())
#--------------------------------

#if and else if
x = 10
if x> 50:
    print("bigger than 50")
else:
    print("not bigger than 50")
#-----------------------------

#pass:If we start a code block, there must be at least one line of indented code immediately following. If we try to run a file with a hanging code block, we'll get a syntax error. Luckily, Python has provided us with the pass statement for situations where we know we need the block statement, but we aren't sure what to put in it yet.
for val in name:
    pass #because we gave nothing to do, it will result an error so we put pass which returns a null operation; nothing happens
#-------------------------------

#Tuples
#Tuples - A type of data that is immutable (can't be modified after its creation) and can hold a group of values. Tuples can contain mixed data types
dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])		# output: Bruce
#dog[1] = 'dachshund'	# ERROR: cannot be modified ('tuple' object does not support item assignment)
#---------------------------------

#lists
#Lists - A type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data.
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']

#-------------------------

#Dictionaries
#Dictionaries - A group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values. When you're ready, you can find more built-in dictionary methods here.
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists
new_person['hobbies'] = ['climbing', 'coding']	# adds a key-value pair if the key doesn't exist
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}        

#------------------------
#common Functions:
print(type(2.63))		# output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>
#len function: !!!!
print(len(new_person))		# output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))	# output: 11

total = 35
user_val = "26"
# total = total + user_val		# output: TypeError
total = total + int(user_val)		# total will be 61

#print("Hello" + 42)			# output: TypeError
print("Hello" + str(42))		# output: Hello 42
#-------------------------
#For loops:
for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2

my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python

#ANOTHER WAY:
capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
     print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
for val in capitals.values():
     print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

count = 0
while count < 5:
    print("looping - ", count)
    count += 1

for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r

for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i
#---------------------------------------------------------------------

#Functions:
def add(a,b):	# function name: 'add', parameters: a and b
    x = a + b	# process
    return x	# return value: x

new_val = add(3, 5)    # calling the add function, with arguments 3 and 5
print(new_val)    # the result of the add function gets sent back to and saved into new_val, so we will see 8

#-------------------------------------------------------------------------
#functions basics 1
#1
print("first problem:")
def a():
    return 5
print(a())
#output:5

#2
print("2nd problem:")
def a():
    return 5
print(a()+a())
#output:10

#3
print("3rd problem:")
def a():
    return 5
    return 10
print(a())
#output: 5

#4
print("problem 4:")
def a():
    return 5
    print(10)
print(a())
#output:5

#5
print("5th problem:")
def a():
    print(5)
x = a()
print(x)
#output: 5 none

#6
print("problem 6:")
#def a(b,c):
 #   print(b+c)

#print(a(1,2) + a(2,3)) 
#output: underfined error because there is no retrun none+none = typeError

#7
print("problem 7:")
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
#output: 25

#8
print("problem 8:")
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7

print(a())
#output: 100 10

#9
print("problem 9:")
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
#output: 7 14 21

#10
print("problem 10:")
def a(b,c):
    return b+c
    return 10
print(a(3,5))
#output: 8

#11
print("problem 11:")
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
#output: 500 500 300 500

#12
print("problem 12:")
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
#output: 500 500 300 500

#13
print("problem 13:")
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
#output: 500 500 300 300

#14
print("problem 14:")
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
#output: 1 3 2

#15
print("problem 15:")
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
#output: 1 3 5 10





























