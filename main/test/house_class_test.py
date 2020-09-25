"""
Testing creation and features of house object
"""

import sys
sys.path.append("..")
import house_class as house_module

#creation
print('--TESTING CREATION--')
house_1 = house_module.House('Large House', 'White', 3)
print('calculated:', house_1)
print('expected: House(Large House, White, 3, 100')
print('')

#upgrade feature
print('--TESTING UPGRADE FEATURE--')
house_2 = house_module.House('Old House', 'Blue', 2)
house_3 = house_module.House('Cool House', 'Red', 1)
#house 3
print('~HOUSE LEVEL 1')
house_3.upgrade()
print('calculated:', house_3)
print('expected: House(Cool House, Red, 2, 20)')
house_3.upgrade()
print('calculated:', house_3)
print('expected: House(Cool House, Red, 3, 40)')
house_3.upgrade()
print('calculated:', house_3)
print('expected: calculated: House(Cool House, Red, 3, 40)')

#house 2
print('~HOUSE LEVEL 2')
house_2.upgrade()
print('calculated:', house_2)
print('expected: House(Old House, Blue, 3, 80)')
house_2.upgrade()
print('calculated:', house_2)
print('expected: House(Old House, Blue, 3, 80)')

#house 1
print('~HOUSE LEVEL 3')
house_1.upgrade()
print('calculated:', house_1)
house_1.upgrade()
print('expected: House(Large House, White, 3, 100)')
print('')

#get features
print('--TESTING GET FEATURES--')








































#
