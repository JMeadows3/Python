import math
import string

ones_dic = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',
 7:'seven', 8:'eight', 9:'nine'}

one_ten = {10:'ten',110:'hundred ten',210:'hundred ten',310:'hundred ten',410:'hundred ten',510:'hundred ten',
610:'hundred ten',710:'hundred ten',810:'hundred ten',910:'hundred ten'}

tens_dic = {2:'twenty', 3:'thirty', 4:'fourty', 5:'fifty', 6:'sixty',
7:'seventy', 8:'eighty', 9:'ninety'}

teen_dic = {11:'eleven', 12:'twelve', 13:'thriteen', 14:'fourteen', 15:'fifteen',
16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}

yes = True

while yes:
    
    user = input('Enter a Number to become a word 1-999: ')
