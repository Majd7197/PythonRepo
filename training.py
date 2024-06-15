list1 = ["majd", "george","amjad"]
for k in list1:
    print (k)
    
for i in list1:
    for x in i:
        print (x)
print(list1[0][0])
list1.append("KHATTHOOORA")
print(list1)
list1.pop()
print(list1)
list1[0] = 1
print(list1)
tuple = ("majd","george")
print(tuple[0][0])

dictionary = {"car" : "BMW", "value": 1}
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
print(dictionary)
print(dictionary['car'])
print(dictionary['car'][0])
first_key = list(dictionary.keys())[0]
print(first_key)  # Output: car

for key,value in dictionary.items():
    print (key)
    
    
students = [{"student1":"Majd", "student2" : "george"}]

print(list(students[0].keys())[0])


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

for key,value in dojo.items():
    print(f"{key.upper()} {len(value)}")
    for j in value:
        print(j)
    print()
#print(f"{dojo.keys()}")
print(list(dojo.keys())[0].upper())

students1 = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for k in students:
        print(f"first name - {k['first_name']} , last name : {k['last_name']}")
   # print(f"{student[0]}")
iterateDictionary(students1) 

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
#first_name - Michael, last_name - Jordan
#f#irst_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel
