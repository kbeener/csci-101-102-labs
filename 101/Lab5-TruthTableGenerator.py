# Kristin Beener
# CSCI 101 - Section C
# Python Lab 5

rows = ['a b | ', '=' * 10, '0 0 | ', '0 1 | ', '1 0 | ', '1 1 | ']
OR = ['OR','', '0 |', '1 |', '1 |','1 |']
AND = ['AND','', '0 |', '0 |', '0 |','1 |']
XOR = ['XOR','', '0 |', '1 |', '1 |','0 |']
NOR = ['NOR','', '1 |', '0 |', '0 |','0 |']
NAND = ['NAND','', '1 |', '1 |', '1 |','0 |']
num_options = ['1', '2', '3', '4', '5', '6']

j = 0
continue_ = 'y'
while continue_[0] == 'y':
    print()
    print('Truth Table Generator | Round#', j)
    print('=+'*21)
    print('Enter an option:\n1. OR Gate\n2. AND Gate\n3. XOR Gate\n4. NOR Gate\n5. NAND Gate\n6. Quit')
    num_input = input('OPTION> ')
    
    if num_input not in num_options:
        print('ERROR: Please choose from [1-6]')
        print('OUTPUT ERROR')
        j +=1
        continue
        
    for i in range(len(rows)):
        if num_input == '1':
            print(f'{rows[i]}{OR[i]}')
            
        elif num_input == '2':
            print(f'{rows[i]}{AND[i]}')
            
        elif num_input =='3':
            print(f'{rows[i]}{XOR[i]}')
            
        elif num_input == '4':
            print(f'{rows[i]}{NOR[i]}')
            
        elif num_input == '5':
            print(f'{rows[i]}{NAND[i]}')
           
    if num_input == '6':
        break
        
    continue_ = input('CONTINUE> ')
    j += 1
    
print('OUTPUT Goodbye!')
print('=+'*21)
