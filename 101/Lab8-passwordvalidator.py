#Kristin Beener
#CSCI 101- Section C
#Python Lab 8
import random
import string

letters = string.ascii_letters 
digits =  string.digits
specchar = string.punctuation
valid = True

print('Would you like to check your own password or a random one? (1 or 2)')
choice = input('CHOICE> ')

if choice == '1':
    print('Enter a password to validate:')
    password = input('PASSWORD> ')
    print(f'Validating the password {password}')
    if len(password) >= 8:
        digit = 0
        char = 0
        for i in password:
            if i.isdigit():
                digit += 1
            if i in specchar:
                char += 1
        if (char and digit) < 1:
            print(f'The password {password} is an invalid password')
            valid = False
        else:
            valid = True
            
    else:
        print(f'The password {password} is an invalid password')
        valid = False
           
elif choice == '2':
    print('Number to initialize the random generator:')
    myseed = int(input('SEED> '))
    password = ''
    random.seed(myseed)
    for i in range(0,8):
        index = random.random() * len(letters)
        password += letters[int(index)]
    for i in range(0,2):
        index = random.random() * len(digits)
        password += digits[int(index)]
    for i in range(0,2):
        index = random.random() * len(specchar)
        password += specchar[int(index)]
    print(f'Validating the password {password}')
    valid = True
else:
    print('ERROR')
    
#calculate the score if the password is valid
if valid == True:
    alpha = 0
    num = 0
    punct = 0
    vowel = 0
    upper = 0
    lower = 0
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    for i in range(len(password)):
        if password[i].isalpha():
            alpha += 1
            if password[i].isupper():
                upper += 1
                if password[i] in vowels:
                    vowel += 1
            else:
                lower += 1
                if password[i] in vowels:
                    vowel += 1
        elif password[i].isdigit():
            num += 1
        else:
            punct += 1
    x = upper - lower
    score = (alpha*4) + (num*5) + (punct*6) - (vowel*3) + (x*2)
    #print(score) testing for bugs
    
    if score < 20:
        output = 'Weak+'
        print(f'The password {password} is a {output} password')
        print(f'OUTPUT {output}')
    elif (20 <= score < 40):
        output = 'Weak'
        print(f'The password {password} is a {output} password')
        print(f'OUTPUT {output}')
    elif (40 <= score < 60):
        output = 'Good'
        print(f'The password {password} is a {output} password')
        print(f'OUTPUT {output}')
    elif (60 <= score < 80):
        output = 'Strong'
        print(f'The password {password} is a {output} password')
        print(f'OUTPUT {output}')
    else:
        output = 'Strong+'
        print(f'The password {password} is a {output} password')
        print(f'OUTPUT {output}')
else:
    print('OUTPUT INVALID')

    
    
        
    
