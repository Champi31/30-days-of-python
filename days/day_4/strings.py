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
print (company.replace('Coding', 'Everyone'))
print (company.split())
companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print (companies.split())
print (company[0])
print (company[-1])
print (company[10])
PFE = 'Python For Everyone'
print (''.join(w[0] for w in PFE.split()))
print (''.join(w[0] for w in company.split()))
print (company.index('C'))
print (company.index('F'))
company1 = 'Coding For All People'
print (company.rfind('I'))
sentences = 'You cannot end a sentence with because because because is a conjuntion'
because1 = 'because'
print (sentences.find(because1))
because3 = 'because'
print (sentences.rindex(because3))
all_because = sentences[0:30]
all_because1 = sentences[54:71]
print (all_because + all_because1)