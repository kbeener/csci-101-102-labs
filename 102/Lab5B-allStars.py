# Kristin Beener
# CSCI 102 - Section E
# Week 5B - It's Full of Stars

coneinput = input('INPUT> ')
sym = '* '
# add spaces between characters using ' '.join(list(coneinput)) and add underscores with str.replace(' ','_')
for i in range(len(coneinput)):
    coneinput = coneinput.replace(' ','_')
coneinput = list(coneinput)
print(' '*(len(coneinput)-1) + sym)
i = 2
while i < len(coneinput)-1:
    print(' '*(len(coneinput)-i)+ sym * i)
    i += 1
print(' '* 1 + sym * (len(coneinput)-1))
print(sym * len(coneinput))   
print(' '.join(coneinput))


    
