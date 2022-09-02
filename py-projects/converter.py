import math
from xdrlib import ConversionError

def dist(a, b):
    return ( a * b)

ref = ['meters', 'inches', 'feet', 'yards', 'miles', 'kilos']

meters = 1.0

inchs = 0.0254

feet = 0.3048

yards = 0.9144 

miles = 1609.34

kilos = 1000.0

user_units = input(f'\nWhat Measurement do you want to Use:\n{ref}: ').lower()

units_dist = float(input(f'\nWhat is the distance in {user_units}: \n'))

user_convert = input(f'\nWhat do you want to convert {user_units} to?:\n{ref}: \n').lower()
print(meters)
if user_units:
    a = dist(units_dist, float(user_units))
    if user_convert:
        conversion = a / user_convert
        print(conversion)

print(f'{conversion}')



# print(f'{round(user*feet, 1)} feet')
# meters = ref[0]
# meters = 1

# inchs = ref[1]
# inchs = 0.0254

# feet = ref[2]
# feet = 0.3048

# yards = ref[3]
# yards = 0.9144 

# miles = ref[4]
# miles = 1609.34

# kilos = ref[5]
# kilos = 1000

# if ref[0] in user_units:
#     a = dist(units_dist, meters)
#     if ref[5] in user_convert:
#         len_kilos = a / kilos
#         print(f'\n{units_dist} {user_units} is {len_kilos} kilos\n')