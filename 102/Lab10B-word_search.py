#Kristin Beener
#CSCI 102 - Section E
#Week 10 - Part B

import random
import os

#prompt user for information
print('Enter the length of the word you are looking for:')
length = int(input('LENGTH> '))
print('Number to initialize the random generator:')
seed = int(input('SEED> '))
random.seed(seed)
# find location of the os path and see why it can't find the file
#os.getcwd()
#print(os.getcwd())
#if os.path.exists('dictionary.txt'):
    #print('TRUE')
#read through the file and count the number of words of the specified length and append them to their own list
words = []
numwords = len(words)
with open('dictionary.txt','r') as dictfile:
    for i in dictfile:
        i = i.replace('\n', '')
        if len(i) == length:
            numwords += 1
            words.append(i)
#error implementation
if len(words) != 0:
    index = random.random() * len(words)
    randomword = words[int(index)]
    print(f'There are {numwords} words in the dictionary with length {length}')
    print(f'OUTPUT {numwords}')
    print(f'Here is one random word in the dictionary with length {length}')
    print(f'OUTPUT {randomword}')
else:
    print(f'ERROR: There is no word of length {length} in this file.')
    print('OUTPUT ERROR')
