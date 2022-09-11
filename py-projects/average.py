import math

nums = []
done = ['stop', 'done', 'quit']
print('\nLETS FIND YOU THE AVG!!')
while True:
    player = str(input('\nEnter a "NUMBER" or "STOP": ')).lower()
    if player in done:
        break            
    nums.append(int(player))
avg = sum(nums) / len(nums)
print(f'\nNumber {nums}, \ntotals: {sum(nums)},\naverages: {round(avg, 1)}\n')