print('Day 2: 30 Days of python programming')
first_name = 'Ulises'
last_name = 'Plata' 
full_name = 'Ulises Plata Piñero'
country = 'Spain'
city = 'Jerez de la Frontera'
age = '16'
year = '2006'
is_married = False
is_true = 'The birds can flying'
is_light_on = 'Yes'
hoobie, favorite_food, horoscope = 'Play de guitar', 'Pork cheek', 'Aries'

print (type(first_name))
print (type(last_name))
print (type(full_name))
print (type(country))
print (type(city))
print (type(age))
print (type(year))
print (type(is_married))
print (type(is_true))
print (type(is_light_on))
print (type(hoobie))
print (type(favorite_food))
print (type(horoscope))

print (len(first_name))
print (len(first_name), len(last_name))

num_one = 5
num_two = 4
total=(num_one + num_two) 
diff=(num_one - num_two)
product=(num_one*num_two)
division=(num_one/num_two)
remainder=(num_one%num_two)
exp=(num_one**num_two)
floor_division=(num_one//num_two)

square_of_radius = (30*30)
area_of_circle = (3.1416 * square_of_radius)
radius = int(input('give me the radius of a circle'))
print(area_of_circle)

fname = input("what is your first name? ")
lname = input("what is your last name ")
country = input("what country are you from ")
Age = input("how old are you? ")

print ('Hello, my name is', fname, lname, 'I am from', country, 'and i am', Age, 'years old')