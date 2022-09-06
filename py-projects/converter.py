import math

def dist(a, b):
    return ( a * b)

ref = ['meters', 'inches', 'feet', 'yards', 'miles', 'kilos'] # user reference of what they can convert
choice = [] # used to store the inputs of the user for later use
change = []

user_units = input(f'\nWhat Measurement do you want to Use:\n{ref}: ').lower() # user input for intial measurement

units_dist = float(input(f'\nWhat is the distance in {user_units}: \n')) # user input for distance 

user_convert = input(f'\nWhat do you want to convert {user_units} to?:\n{ref}: \n').lower() # users measurement wanted to be converted too

choice.append(user_units) 
change.append(user_convert)

# Using the User_units input and matching it with the ref and then changing the out put to equal the what it would be if converted to meters
# to complete the formula

if user_units == 'meters':
    user_units = 1.0
elif user_units == 'inches':
    user_units = 0.0254
elif user_units == 'feet':
    user_units = 0.3048
elif user_units == 'yards':
    user_units = 0.9144
elif user_units == 'miles':
    user_units = 1609.34
elif user_units == 'kilos':
    user_units = 1000.0

# Using the User_convert input and matching it with the ref and then changing the out put to equal the what it would be if converted to meters
# to complete the formula

if user_convert == 'meters':
    user_convert = 1.0
elif user_convert == 'inches':
    user_convert = 0.0254
elif user_convert == 'feet':
    user_convert = 0.3048
elif user_convert == 'yards':
    user_convert = 0.9144
elif user_convert == 'miles':
    user_convert = 1609.34
elif user_convert == 'kilos':
    user_convert = 1000.0

a = dist(units_dist, user_units)  # using the Function to get the distance * referance
len_kilos = a / user_convert # dividing the initial distance by the distance of the converted number

print(f'\n{units_dist} {"".join(choice)} is {round(len_kilos, 3)} {"".join(change)}\n')