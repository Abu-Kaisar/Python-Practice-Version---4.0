'''Acronym Generator'''

acro = input("Tell Use The Full form:")
accro = ""

for i in acro.split():
    accro += i[0]
    
print(accro)
