#Kristin Beener
#CSCI101 - Section C
#Python Lab 9
import random
import string
specchar = string.punctuation
print('Would you like to print the number of times a specific word appears OR print the number of \nwords of a specific length? (1 or 2)')
choice = input('CHOICE> ')

#take users choice and go to specfic function
if choice == '1':
    print('Enter a word:')
    wordinput = input('WORD> ')
    wordlower = wordinput.lower()
    wordcount = 0
    with open('Declaration_of_independence.txt','r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                for c in specchar:
                    if c in word:
                        word = word.replace(c,'')
                if word == wordlower:
                    wordcount += 1
    print(f'The number of times {wordinput} appears in the document is: {wordcount}')
    print(f'OUTPUT {wordcount}')
elif choice == '2':
    print('Enter a length:')
    length = int(input('LENGTH> '))
    wordbank = []
    with open('Declaration_of_independence.txt','r') as file:
        for line in file:
            words = line.split()
            for word in words:
                for c in specchar:
                    if c in word:
                        word = word.replace(c,'')
                if len(word) == length:
                    wordbank.append(word)
    print('Number to initialize the random generator:')
    seed = int(input('SEED> '))
    random.seed(seed)
    index = random.random() * len(wordbank)
    if len(wordbank) == 0:
        print(f'The number of words in the document with length {length} is: {len(wordbank)}')
        print(f'OUTPUT {len(wordbank)}')
        print(f'No example random word of this length exists')
        print(f'OUTPUT ERROR')
    else:
        outputword = wordbank[int(index)]
        print(f'The number of words in the document with length {length} is: {len(wordbank)}')
        print(f'OUTPUT {len(wordbank)}')
        print(f'One example random word of this length is: {outputword}')
        print(f'OUTPUT {outputword}')
else:
    print('ERROR')

