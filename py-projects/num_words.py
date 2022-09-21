import math
import string

ones_dic = {0:' ', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',
 7:'seven', 8:'eight', 9:'nine'}

tens_dic = {0:' ', 1:'ten', 2:'twenty', 3:'thirty', 4:'fourty', 5:'fifty', 6:'sixty',
7:'seventy', 8:'eighty', 9:'ninety'}

teen_dic = {11:'eleven', 12:'twelve', 13:'thriteen', 14:'fourteen', 15:'fifteen',
16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}

yes = True

while yes:
    user = int(input('Enter a Number to become a word 1-999: '))

    if user in range(1, 10):
        ones = user%10
        print(ones)

    elif user == 10:
        print('ten')
    
    elif user in range(11, 20):
        print(teen_dic.get(user))

    elif user in range(20,100):
        tens = user//10
        ones = user%10
        print(tens_dic.get(tens), ones_dic.get(ones))

    elif user in range(100,1000):
        num_hundreds =  user //100
        num_tens = user%100
        num_ones = user%10

        if num_tens == 0:
            print(f'\n{ones_dic.get(num_hundreds)} hundred\n')
        
        elif num_tens == 10:
            fix_ten = num_tens-num_ones
            fix_ten = fix_ten//10
            print(f'\n{ones_dic.get(num_hundreds)} hundred {tens_dic.get(fix_ten)}\n')

        elif num_tens in range(1, 10):
            print(f'\n{ones_dic.get(num_hundreds)} hundred {ones_dic.get(num_ones)}\n')

        elif num_tens in range(11,20):
            print(f'\n{ones_dic.get(num_hundreds)} hundred {teen_dic.get(num_tens)}\n')

        elif num_tens in range(20, 100):
            fix_ten = num_tens-num_ones
            fix_ten = fix_ten//10
            print(f'\n{ones_dic.get(num_hundreds)} hundred {tens_dic.get(fix_ten)} {ones_dic.get(num_ones)}\n')
        
    else:
        print('\nPlease enter a number within the correct range\n')

        

    



    yeah = ['yes', 'y', 'yeh', 'sure', 'si']
    no = ['no','nah','nope', 'nay']
    again = str(input('check more? ( Yes or No ) : '))
    if again in yeah:
        yes = True    
    else:
        print('BYE!')
        break
