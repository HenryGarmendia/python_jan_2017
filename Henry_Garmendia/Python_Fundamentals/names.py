#ASSIGNMENT: NAMES

#Part 1
'''
Given the following list:

students = [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
Create a program that outputs:

Michael Jordan
John Rosales
Mark Guillen
KB Tonel
'''

#Part 2 -- OPTIONAL
'''
Now, given the following dictionary:

users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
'''

#Create a program that prints  the following format (including number of characters in each combined name):
'''
Students
1 - MICHAEL JORDAN - 13
2 - JOHN ROSALES - 11
3 - MARK GUILLEN - 11
4 - KB TONEL - 7
Instructors
1 - MICHAEL CHOI - 11
2 - MARTIN PURYEAR - 13
'''
# users = {
#     'Students': [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ],
#     'Instructors': [
#         {'first_name' : 'Michael', 'last_name' : 'Choi'},
#         {'first_name' : 'Martin', 'last_name' : 'Puryear'}
#     ]
# }

# for occupation in users:
#     print occupation
#     count=0
#     for name in users[occupation]:
#         count +=1
#         full_name= name['first_name']+ ' '+ name['last_name']
#         print str(count) + ' - ' + full_name.upper() + ' - ' + str(len(name['first_name'])+len(name['last_name']))

users = {
    'Students': [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}

# Loop that iterates through each item in the dictionary
for key, data in users.items():
    print key
    index=1
    # Loop that iterates through the list and prints the first and last name along with place in list and name length
    for value in data:
        length = len(value["first_name"])+len(value["last_name"])
        print "{} -".format(index), value["first_name"], value["last_name"], "- {}".format(length)
        index+=1








