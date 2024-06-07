#Problem 1:Update Values in Dictionaries and Lists
print("Problem 1: Update Values in Dictionaries and Lists")
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

sports_directory['basketball'][1] = "Bryant"
sports_directory['soccer'][0] = "Andres"
print(sports_directory)

z[0]['y'] = 30
print(z)

#Problem 2: Update Values in Dictionaries and Lists
print("Problem 2:Update Values in Dictionaries and Lists")
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(list):
    for student in list:
        print(f"first_name - {student['first_name']}, last_name - {student['last_name']}")
    
iterateDictionary(students) 
print("Problem 3:Get Values From a List of Dictionaries")

def iterateDictionary2(key_name, some_list):
    for k in some_list:
        print(k[key_name])

iterateDictionary2('first_name', students)


def printInfo(some_dict):
    for key, value_list in some_dict.items():
        print(f"{key} ({len(value_list)})")
        for value in value_list:
            print(f"- {value}")
        print()  # For better readability with a blank line between keys

# Example dictionary
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# Call the function with the example dictionary
printInfo(dojo)

print(dojo.keys())



