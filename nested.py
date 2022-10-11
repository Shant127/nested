x = [ [5,2,3], [10,8,9] ]

students = [
    {'first_name':  'Michael', 'last_name' : 'Bryant'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


x [1][0]=15
print(x)





#Get values from a list of dictionaries

def iterate_dictionary2(key, list_of_dicts):
    # iterate over fist of dictionaries
    #for i in range(len(list_of_dicts)):
        #print(list_of_dicts[i][key])
    for dict in list_of_dicts:
        print(dict[key])


students = [
    {'first_name': 'Micheal', 'last_name': 'Bryant'},
    {'first_name': 'john', 'last_name': 'Rosales'},
    {'first_name': 'mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Guillen'},
]


#iterate_dictionary2('first_name', students)



"""
Iterate Through a Dictionary with List Values
Create a function printInfo(some_dict) that given a dictionary whose values are all lists,
prints the name of each key along with the size of its list, 
and then prints the associated values within each key's list

"""


dojo = {
    'locations': [
        'San Jose', 
        'Seattle', 
        'Dallas', 
        'Chicago', 
        'Tulsa', 
        'DC', 
        'Burbank'
    ],
    'instructors': [
        'Michael', 
        'Amy', 
        'Eduardo', 
        'Josh', 
        'Graham', 
        'Patrick', 
        'Minh',
        'Devon',
    ]
}

def print_info(dict_input):
    for key in dict_input.keys():
        print(f'{len(dict_input[key])}{key}')
        for element in dict_input[key]:
            print(element)


print_info(dojo)

# output:

#7 LOCATIONS
#San Jose
#Seattle
#Dallas
#Chicago
#Tulsa
#DC
#Burbank
    
#8 INSTRUCTORS
#Michael
#Amy
#Eduardo
#Josh
#Graham
#Patrick
#Minh
#Devon
