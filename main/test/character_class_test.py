"""
Testing creation and features of character object
"""

import character_class as char

#creation

person_1 = char.Character(25)
print(person_1)

#cash features

person_1.withdraw_cash(10)
a = (person_1.get_cash()) #expected 15
if person_1.get_cash() > 30: #expected False
    person_1.withdraw_cash(30)
else:
    person_1.deposit_cash(5)
b = (person_1.get_cash()) #expected 20


person_1.deposit_cash(5)
c = (person_1.get_cash()) #expected 25

print('calculated:', a,b,c)
print('expected: 15, 20, 25')

#house features

#item features

#trait features





























#
