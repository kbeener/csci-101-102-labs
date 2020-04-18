#Kristin Beener
#CSCI 102 - Section E
#Week 7 - Hangman

print('Welcome to Simple Hang Man')
print('Enter a secret word:')
secretword = input('WORD> ')
print('Enter the number of guesses allowed:')
num = int(input('NUM> '))
i = num
guessedchar = []
revield = []
solved = False
while i > 0 and solved == False: #code should stop when i == 0 
    print('Please enter a character:')
    char = input('CHAR> ')
    if char in secretword: #and char not in guessedchar
        revield = []
        i -= 1
        guessedchar.append(char)
        for c in range(len(secretword)):
            if secretword[c] in guessedchar:
                revield.append(secretword[c] + ' ')
            else: 
                revield.append('_'+ ' ')
        guessedword = ''.join(revield)
        if '_' not in guessedword:
            print('OUTPUT Congratulations! You guessed the secret word!')
            print(f'{i} guesses remaining')
            print(f'OUTPUT Secret word: {" ".join(secretword)}')
            solved = True
            break
        else:
            print('OUTPUT Success! You guessed a character in the word!')
            print(f'{i} guesses remaining')
            print(f'Characters guessed: [ {", ".join(guessedchar)} ]')
            print('OUTPUT Secret word: ', guessedword)
            print()
            solved = False
  
    elif char not in secretword:
        i -= 1
        if i == num-1:  
            guessedchar.append(char)
            guessedword = ''.join(revield)
            print('OUTPUT Boo! You guessed incorrectly')
            print(f'{i} guesses remaining')
            print(f'Characters guessed: [ {", ".join(guessedchar)} ]')
            print('OUTPUT Secret word:',' _ ' * len(secretword))
            print()
        elif i == 0:
            continue
        elif '_'  not in revield:
            guessedchar.append(char)
            print('OUTPUT Boo! You guessed incorrectly')
            print(f'{i} guesses remaining')
            print(f'Characters guessed: [ {", ".join(guessedchar)} ]')
            print('OUTPUT Secret word:',' _ ' * len(secretword))
            print()   
        else:
            guessedchar.append(char)
            guessedword = ''.join(revield)
            print('OUTPUT Boo! You guessed incorrectly')
            print(f'{i} guesses remaining')
            print(f'Characters guessed: [ {", ".join(guessedchar)} ]')
            print('OUTPUT Secret word:', guessedword)
            print()
    else:
        #tell user they already guessed that number and do not decrease number of guesses
        print('You already guessed that character! Try again.')
        print() 

else:
    if i == 0:
        print('OUTPUT You ran out of guesses! Better luck next time!')
        print(f'OUTPUT Secret word: {" ".join(secretword)}')   
    #else:
        #print('OUTPUT Congratulations! You guessed the secret word!')
        #print(f'{i} guesses remaining')
        #print(f'OUTPUT Secret word: {" ".join(secretword)}')
