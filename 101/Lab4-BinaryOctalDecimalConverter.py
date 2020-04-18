# Kristin Beener
# CSCI 101 - Section C
# Python Lab 4

binary = ['0', '1']
octal = ['0', '1', '2', '3', '4', '5', '6', '7']
decimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operations = ['1', '2', '3', '4', '5']
_BINARY = 0
_DECIMAL = 0
_OCTAL = 0



print('Welcome to the Binary-Octal-Decimal Converter')
continue_ = 'y'
while continue_[0]== 'y':
    print('=+'*21)
    print('Enter an option:\n1. Binary-Decimal Conversionn\n2. Decimal-Binary Conversion\n3. Octal-Decimal Conversion\n4. Decimal-Octal Conversion\n5. Quit')
    continue_ = 'y'
    num_input = input('OPTION> ')
    if num_input == '1':
        _BINARY = list(input('BINARY-STR> '))
        v = 0
        variable = True
        while v < len(_BINARY):
            if _BINARY[v] != '0' and _BINARY[v] != '1':
                variable = False
            v = v + 1
        if variable == False:
            print('ERROR: Input', ''.join(map(str,_BINARY)) ,'is NOT a binary number.')
            print('OUTPUT ERROR')
            print('Would you like to continue (y/n)?')
            continue_ = input('CONTINUE> ').strip().lower()
        else:
            _DECIMAL = 0
            i = 0
            while i <= len(_BINARY)-1:
                bin2dec = int(_BINARY[i]) * (2 ** i)
                _DECIMAL = _DECIMAL + bin2dec
                i += 1
            print('Binary', ''.join(map(str,_BINARY)),'is Decimal', _DECIMAL)
            print('OUTPUT',_DECIMAL)
            print('Would you like to continue (y/n)?')
            continue_ = input('CONTINUE> ').strip().lower()    
        
    elif num_input == '2':
        _DECIMAL = input('DECIMAL-STR> ')
        if _DECIMAL.isdigit():
            _DECIMAL = int(_DECIMAL)
            dec2bin =_DECIMAL
            _BINARY = []
            while dec2bin > 1:
                remainder = int(dec2bin % 2)
                dec2bin = dec2bin / 2
                _BINARY.append(remainder)
            _BINARY.reverse()
            _BINARY= ''.join(map(str,_BINARY))
    
            print('Decimal', _DECIMAL, 'is Binary', _BINARY)
            print('OUTPUT', _BINARY)
            print('Would you like to continue (y/n)?')
            continue_ = input('CONTINUE> ').strip().lower()
        
        else:
            print('ERROR: Input', _DECIMAL ,'is NOT a decimal number.')
            print('OUTPUT ERROR')
            print('Would you like to continue (y/n)?')
            continue_ = input('CONTINUE> ').strip().lower()

    elif num_input == '3':
        _OCTAL = input('OCTAL-STR> ')
        v = 0
        variable = True
        while v < len(_OCTAL):
            if _OCTAL[v] != '0' and _OCTAL[v] != '1' and _OCTAL[v] != '3' and _OCTAL[v] != '4' and _OCTAL[v] != '5' and _OCTAL[v] != '6' and _OCTAL[v] != '7':
                variable = False
            v = v + 1
        if variable == False:
            print('ERROR: Input', _OCTAL ,'is NOT a octal number.')
            print('OUTPUT ERROR')
            print('Would you like to continue (y/n)?')
            continue_ = input('CONTINUE> ').strip().lower()
        else:
            _OCTAL = int(_OCTAL)
            _octal = _OCTAL
            _DECIMAL = 0
            i = 0
            while (_octal != 0):
                oct2dec = (_octal % 10) * (8 ** i)
                _DECIMAL = _DECIMAL + oct2dec
                i += 1
                _octal = int(_octal / 10)
            print('Octal', _OCTAL ,'is Decimal', _DECIMAL)
            print('OUTPUT', _DECIMAL)
            print('Would you like to continue (y/n)?')
            continue_ = input('CONTINUE> ').strip().lower()
    

    elif num_input == '4':
        _DECIMAL = input('DECIMAL-STR> ')
        if _DECIMAL.isdigit():
            _DECIMAL = int(_DECIMAL)
            dec2oct = _DECIMAL
            _OCTAL = []
            while dec2oct > 1:
                remainder = int(dec2oct % 8)
                dec2oct = dec2oct / 8
                _OCTAL.append(remainder)
            _OCTAL.reverse()
            _OCTAL = ''.join(map(str,_OCTAL))
        
            print('Decimal', _DECIMAL,'is Octal', _OCTAL)
            print('OUTPUT', _OCTAL)
            print('Would you like to continue (y/n)?')
            continue_ = input('CONTINUE> ').strip().lower()
        else:
            print('ERROR: Input', _DECIMAL ,'is NOT a decimal number.')
            print('OUTPUT ERROR')
            print('Would you like to continue (y/n)?')
            continue_ = input('CONTINUE> ').strip().lower()
    elif num_input == '5':
        break
        
    else:
        print('ERROR: Please choose from [1-5]')
        print('OUTPUT ERROR')
        print('Would you like to continue (y/n)?')
        continue_ = input('CONTINUE> ').strip().lower()
        

    
print('OUTPUT Goodbye!')

    

    




