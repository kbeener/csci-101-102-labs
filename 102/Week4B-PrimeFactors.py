# Kristin Beener
# CSCI 102 - Section E
# Week 4B - PrimeFactorization

print('Enter a positive integer to generate its Prime Factors:')
pos_integer = int(input('INPUT> '))

i = 2
primefactors = []
while i <= pos_integer:
    if (pos_integer % i) == 0:
        primefactors.append(i)
        pos_integer = pos_integer // i
    else:
        i = i + 1

print('OUTPUT ', '*'.join(map(str,primefactors)))
          
print('Do you want to get Prime Factors for another input? (y/n)')
_continue = input('CONTINUE> ').lower()
while _continue[0] == 'y':
    print('-'*60)
    print('Enter a positive integer to generate its Prime Factors:')
    pos_integer = int(input('INPUT> '))

    i = 2
    primefactors = []
    while i <= pos_integer:
        if (pos_integer % i) == 0:
            primefactors.append(i)
            pos_integer = pos_integer // i
        else:
            i = i + 1
    print('OUTPUT ', '*'.join(map(str,primefactors)))
    print('Do you want to get Prime Factors for another input? (y/n)')
    _continue = input('CONTINUE> ').lower()
if _continue != 'yes' or _continue != 'y':
    print('-'*60)
    print('GoodBye!')
      
