print ([])
compra = ['patatas', 'avichuels', 'cebolla', 'pepino', 'brocoli', 'lechuga', 'garbanzo']
print (compra)
print (len(compra))
print (compra[0])
print (compra[3])
print (compra[-1])
mixed_data_types = ['Ulises', '16', '1.72', 'single', 'Jerez']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print (it_companies)
print (len(it_companies))
print (it_companies[0])
print (it_companies[3])
print (it_companies[-1])
it_companies[3] = 'Android'
print (it_companies)
it_companies.insert(7, 'IT')
print (it_companies)
it_companies.sort()
print (it_companies)
it_companies.reverse()
print (it_companies)
first_three_items = it_companies[0:3]
print (first_three_items)
last_three_times = it_companies[6:8]
print (last_three_times)
print (it_companies[3:4])
it_companies.remove('Oracle')
print (it_companies)
it_companies.remove('Google')
print (it_companies)
it_companies.remove('Amazon')
print (it_companies)
print (it_companies.clear())
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
Added = ['Python', 'SQL']
front_end.extend(Added)
front_end.extend(back_end)
print ('Full_stack:', front_end)
