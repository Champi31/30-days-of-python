# 1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
T = 'Thirty'
D = 'Days'
O = 'Of'
P = 'Python'
space = ' '
full_string = T + space + D + space + O + space + P
print (full_string)
# 2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
C = 'Coding'
F = 'For'
A = 'All'
Space = ' '
full_string2 = C + Space + F + Space + A
print ( full_string2)
# 3 Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
print (company)
print (len(company))
mayus = company.upper()
print (mayus)
minum = company.lower()
print (minum)
cap = company.capitalize()
tit = company.title()
swp = company.swapcase()
print (cap)
print (tit)
print (swp)
cut = slice(0, 6)
print (company[cut])
Cd = 'Coding'
print (company.index(Cd))
print (company.rindex(Cd))
print (company.rfind(Cd))
print (company.find(Cd))
print (company.replace('Coding', 'Python'))