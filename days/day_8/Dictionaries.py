dog = {}
dog['name'] = 'kuro'
dog['color'] = 'black'
dog['breed'] = 'Alaska malamut'
dog['legs'] = 4
dog['age'] = 1
print (dog)
students_dct = {
    'Firts_name':'Ulises',
    'Last_name':'Plata',
    'Gender':'Male',
    'Age':16,
    'Marital_Status':'Single',
    'Skills':['Play the guitar', 'English', 'Programation'],
    'Country':'Spain',
    'City':'Jerez',
    'Adress':{
    'Street':'San Telmo',
    'zipcode':'11408'
    }
}

print (students_dct)
print (len(students_dct))
print (students_dct['Skills'])
print (type(students_dct['Skills']))
print (students_dct.keys())
print (students_dct.values())
students_lst = students_dct.items()
print (students_dct)
print (students_lst)
students_dct.popitem()
del students_dct['Marital_Status']
print (students_dct)
del dog