import random
import os
os.system('clear')  # clear screen


def print_start():
    print('\033[1;1;1m' + "{}".format('I am thinking of a 3-digit number. Try to guess what it is.\n') +
          '\033[0m')
    print('Here are some clues:')
    print('{:^10}{:^20}'.format('When I say:', 'That means:'))
    print('{:^10}{:^20}'.format('Cold', 'No digit is correct.'))
    print('{:^10}{:^20}'.format('Warm', 'One digit is correct but in the wrong position.'))
    print('{:^10}{:^20}'.format('Hot', 'One digit is correct and in the right position.'))
    print('\033[1;30;1m' + "{}".format('I have thought up a number. You have 10 guesses to get it.\n') +
          '\033[0m')


def rand_num():
    num = []
    i = 0
    while i != 3:
        num1 = random.randint(0, 9)
        num.append(num1)
        i = len(set(num))
    num = set(num)
    num = list(num)
    if num[0] == 0:
        num[0] = num[1]
        num[1] = 0
    return num[0], num[1], num[2]


def check(x):
    i = 1
    while i != 11:
        user = input('Guess #%d:' % i)
        try:
            int(user)
            if len(user) != 3:
                print('Guess have to be 3 digit number')
                continue
        except ValueError:
            print('Guess have to be 3 digit number')
        user = list(user)
        while j != 3:
            user[j] = int(user[j])
            j += 1
        i += 1


print_start()
rand_num()
check(rand_num())
print (type(rand_num()))
