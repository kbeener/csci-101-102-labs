#Kristin Beener
#CSCI 102 - Section E
#Week 9 - Part B
import random

kevin = 0
stacy = 0
vowels = ['A','E','I','O','U']

print('Would you like to provide your own string or generate a random one? (1 or 2)')
choice = int(input('CHOICE> '))

if choice == 1:
    print('Enter a string for the game:')
    string = input('STRING> ')
    for i in range(len(string)):
        if string[i] in vowels:
            kevin = kevin + len(string) - i
        else:
            stacy = stacy + len(string) - i
else:
    print('Number to initialize the random generator:')
    myseed = int(input('SEED> '))
    random.seed(myseed)
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    string = ''
    for i in range(0,6):
        index = random.random() * len(alphabet)
        string += alphabet[int(index)]
    for i in range(len(string)):
        if string[i] in vowels:
            kevin = kevin + len(string) - i
        else:
            stacy = stacy + len(string) - i
if stacy > kevin:
    print(f'With the string {string}, Kevin\'s score is {kevin} and Stacy\'s score is {stacy}')
    print('Stacy wins!')
    print('OUTPUT ', kevin)
    print('OUTPUT ', stacy)
    print('OUTPUT Stacy')
elif stacy < kevin:
    print(f'With the string {string}, Kevin\'s score is {kevin} and Stacy\'s score is {stacy}')
    print('Kevin wins!')
    print('OUTPUT ', kevin)
    print('OUTPUT ', stacy)
    print('OUTPUT Kevin')
else:
    print(f'With the string {string}, Kevin\'s score is {kevin} and Stacy\'s score is {stacy}')
    print('It\'s a tie!')
    print('OUTPUT ', kevin)
    print('OUTPUT ', stacy)
    print('OUTPUT Draw')
