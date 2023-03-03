import random
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ch = (random.sample(num, 4))
chstr = ''.join(ch)
while True:
    val = input()
    if chstr == val:
        print('OK')
        break
    if len(val) != 4:
        print('input 4 numbers.')
        continue
    answer = ''
    for i in range(4):
        if (chstr[i] == val[i]):
            answer += chstr[i]
        else:
            answer += 'X'
    print('->' + answer)
