# Kristin Beener
# CSCI 102 - Section E
# Week 5A - Reverse Only Letters

continue_ = 'y'
while continue_[0] == 'y':
    print('Enter a string with letters to reverse.')
    S = input('STRING> ')
    revS = []
    letters= []

    for c in S:
        if c.isalpha():
            letters.append(c)
    i = 0
    while i < len(S):
        if S[i].isalpha():
            revS.append(letters.pop())
            i += 1
        else:
            revS.append(S[i])
            i += 1
    print('OUTPUT',''.join(revS))
    continue_ = input('Do you want to reverse another string? (y/n) ').strip().lower()
    print('-'*50)
print('Goodbye!')
            
    


    
            
            
        
    
