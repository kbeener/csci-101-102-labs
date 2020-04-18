#Kristin Beener
#CSCI 101 - Section C
#Python Lab 7
continue_ = 'y'
while continue_[0] =='y':
    print()
    print('Simple Image Compression:')
    print('=+'*21)
    print('Enter an option:\n1. Encode Image\n2. Decode Image\n3. Display Image\n4. Quit')
    option = input('OPTION> ')

    
    if option == '1':
        print()
        print('OPTION 1: ENCODE IMAGE')
        string2encode = input('ORIGINAL-STR> ')
        prevchar = string2encode[0]
        encoded = []
        count = 0
        if string2encode.isupper() or string2encode.islower():
            for char in string2encode:
                if char != prevchar:
                    encoded.append(str(count))
                    encoded.append(prevchar)
                    count = 1
                    prevchar = char
                else:
                    count += 1
                    prevchar = char
            encoded.append(str(count))
            encoded.append(prevchar)
            print(f"OUTPUT {''.join(encoded)}")
            print('Would you like to continue (y/n)?')
            continue_ = input('CONTINUE> ').strip().lower()
        else:
            print('ERROR: Number compression not supported.')
            print('OUTPUT ERROR')
            print('Would you like to continue (y/n)?')
            continue_ = input('CONTINUE> ').strip().lower()
                
    elif option == '2':
        print()
        print('OPTION 2: DECODE IMAGE')
        string2decode = input('ENCODED-STR> ')
        decoded = ''
        count = ''
        if string2decode.isupper() or string2decode.islower():
             for j in string2decode:
                if j.isdigit():
                    count += j
                if j.isalpha():
                    decoded += j * int(count)
                    count = ''  
        else:
            print('ERROR: Number compression not supported.')
            print('OUTPUT ERROR')
            print('Would you like to continue (y/n)?')
            continue_ = input('CONTINUE> ').strip().lower()
        print(f'OUTPUT {decoded}')
        print('Would you like to continue (y/n)?')
        continue_ = input('CONTINUE> ').strip().lower()
          
    elif option == '3':
        print()
        print('OPTION 3: DISPLAY IMAGE')
        image = input('IMAGE> ')
        if image.isupper() or image.islower():
            row = int(input('ROW> '))
            column = int(input('COLUMN> '))
            print()
            output = []
            for i in range(0,len(image),column):
                rowcontent = image[i] * column
                output.append(rowcontent)
            for i in output:
                print(i)
            print()
            print(f'OUTPUT {output}')
            print('Would you like to continue (y/n)?')
            continue_ = input('CONTINUE> ').strip().lower()
        else:
            print('ERROR: Number compression not supported.')
            print('OUTPUT ERROR')
            print('Would you like to continue (y/n)?')
            continue_ = input('CONTINUE> ').strip().lower()
        
    elif option == '4':
        break
    
    else:
        print('ERROR: Please choose from [1-4]')
        print('OUTPUT ERROR')
        print('Would you like to continue (y/n)?')
        continue_ = input('CONTINUE> ').strip().lower()
        
print('OUTPUT Goodbye!')
print('=+'*21)

