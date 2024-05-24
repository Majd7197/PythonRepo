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