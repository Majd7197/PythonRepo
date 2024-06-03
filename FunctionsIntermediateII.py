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
def iterateDictionary(namesOfStudents):
    for i in namesOfStudents:
        print(namesOfStudents.key)

iterateDictionary(students)

 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

