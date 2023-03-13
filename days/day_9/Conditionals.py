age = int(input('How old are you? '))
if age >= 18:
    print('You are old enough to learn to drive.')
diference_age = str(18 - age)
if age < 18:
    print ('You need more ' + diference_age + ' years to learn to drive')
Enter_your_age = int(input('Enter your age '))
The_creator_age = 30
younger_than = str(The_creator_age - Enter_your_age)
older_than = str(Enter_your_age - The_creator_age)
if Enter_your_age < The_creator_age:
    print ('You are ' + younger_than + ' years younger than me')
elif Enter_your_age > The_creator_age:
    print ('You are ' + older_than + ' years older than me')
Number_1 = int(input('Enter the first number'))
Number_2 = int(input('Enter the second number'))
if Number_1 < Number_2:
    print (Number_1, 'Is smaller than', Number_2)
if Number_1 > Number_2:
    print (Number_1, 'Is greater than', Number_2)
if Number_1 == Number_2:
    print (Number_1, 'as greater as', Number_2, )
calification = int(input('Enter your calification '))
if calification == 0 or calification <= 49:
    print ('Your test grade is F')
elif calification >= 50 and calification <= 59:
    print ('Your test grade is D')
elif calification >= 60 and calification <= 69: 
    print ('Your test grade is C')
elif calification >= 70 and calification <= 89:
    print ('Your test grade is B')
elif calification >= 90 and calification <=100:
    print ('Your test grade is A')
else:
    print ('Enter your real calification')
season = input('Enter the seasson ').capitalize()
if season == 'December' or season == 'January' or season == 'February':
    print ('The season is winter')
elif season == 'March' or season == 'April' or season == 'May':
    print ('The season is spring')
elif season == 'June' or season == 'July' or season == 'August':
    print ('The season is summer')
elif season == 'September' or season == 'October' or season == 'November':
    print ('The season in autum')
else:
    print ('Enter the correct month')
fruits = ['banana', 'orange', 'mango', 'lemon']
name_of_the_fruit = input('Enter a fruit ')
exist_the_fruit_in_the_list = name_of_the_fruit in fruits
if exist_the_fruit_in_the_list == False:
    fruits.append(name_of_the_fruit)
    print (fruits)
else:
    print ('This fruits alredy exist in the list')