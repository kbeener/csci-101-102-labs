#Kristin Beener
#CSCI 102 - Section E
#Week 9 - Part A
import random
print('Number to initialize the random generator: ',end='')
myseed = int(input())
random.seed(myseed)
num2guess = random.randint(1,100)
guess = 0
print('Enter a number between 1 and 100: ',end='')
guess = int(input())
while guess != num2guess:
    if guess > 100:
        print('OUTPUT Please Enter a number between 1 and 100')
    elif guess < 1:
         print('OUTPUT Please Enter a number between 1 and 100')
    elif guess >= (num2guess + 50):
        print('OUTPUT You\'re cold!')
    elif guess >= (num2guess + 25) and guess < (num2guess + 50):
        print('OUTPUT You\'re lukewarm!')
    elif guess >= (num2guess + 15) and guess < (num2guess + 25):
        print('OUTPUT You\'re getting warm!')
    elif guess >= (num2guess + 5) and guess < (num2guess + 15):
        print('OUTPUT You\'re getting hot!')
    elif guess < (num2guess + 5):
        print('OUTPUT You\'re so close!')
    print('Enter a number between 1 and 100: ',end='')
    guess = int(input())
print('OUTPUT Congrats! You won!')
    
