empty_tuple = ()
siblings = ('Alba', 'Hugo')
siblings_2 = ('Alvaro', 'Irene')
family = siblings + siblings_2
print (family)
print (len(family))
parents = ('Antonio', 'Maribel')
family_members = parents + family
print (family_members)
del family_members
fruits = ('apple', 'pineapple', 'watermelon',)
vegetables = ('onion', 'garlic', 'cucumber')
animal_products = ('meat', 'milk', 'eggs')
food_stuff_tp = fruits + vegetables + animal_products
print (food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print (food_stuff_lt)
food_stuff_lt.remove('garlic')
print (food_stuff_lt)
cut_first_three_items = slice(0, 3)
cut_last_three_items = slice(5, 8)
print (food_stuff_lt[cut_first_three_items])
print (food_stuff_lt[cut_last_three_items])
del food_stuff_lt
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'sweden')
print ('Estonia' in nordic_countries)
print ('Iceland' in nordic_countries)