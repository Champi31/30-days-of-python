it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print (len(it_companies))
it_companies.add('Twitter')
print (it_companies)
it_companies.update(['Infosys', 'Flipkart'])
print (it_companies)
it_companies.discard('Apple')
print(it_companies)
print ('El método discard no crea una excepción cuando falta un elemento en el set')
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = A.union(B)
print (C)
print (A.intersection(B))
print (A.issubset(B))
print (A.isdisjoint(B))
C_1 = A.union(B)
C_2 = B.union(B)
print (C_1)
print (C_2)
print (A.symmetric_difference(B))
del A, B, C, C_1, C_2
