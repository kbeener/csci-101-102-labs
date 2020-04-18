#Kristin Beener
#CSC1 101 - Section C
#Python Lab 6

continue_ = 'y'
while continue_[0] == 'y':
    print()
    print('Review Search & Sort:')
    print('=+'*21)
    print('Enter an option:\n1. Enter a new list\n2. Deploy Binary Search\n3. Deploy Selection Sort\n4. Quit')
    option = input('OPTION> ')
    if option == '1':
        print()
        print('OPTION 1: ENTER A NEW LIST')
        print('How many items are in this list?')
        nlist = input('LIST_SIZE> ')
        if nlist.isdigit():
            nlist = int(nlist)
            newlist = []
            for c in range(nlist):
                print('ITEM',c, end='')
                item = input('> ')
                if item.isdigit():
                    item = int(item)
                    newlist.append(item)
                else:
                    print(f'ERROR: {item} is not a valid integer!')
                    print('OUTPUT ERROR')
                    break
        else:
            print(f'ERROR: {nlist} is not a valid integer!')
            print('OUTPUT ERROR')
    elif option == '2':
        print()
        print('OPTION 2: BINARY SEARCH')
        print(f'Input list: {newlist}')  
        if len(newlist) == 0:
            print('ERROR: Empty list! Please select option (1) to reenter a list')
            print('OUTPUT ERROR') 
        else:
            i = 1
            is_sorted = True
            while i < len(newlist):
                if newlist[i-1] > newlist[i]:
                    is_sorted = False
                i += 1
            if is_sorted == True:      
                i = 0
                target = int(input('BINARY-SEARCH-TARGET> '))
                low = 0
                high = len(newlist)-1
                while low <= high:
                    mid = low + (high - low) // 2
                    if target == newlist[mid]:
                        i += 1
                        print(f'Target value {target} found at index {mid}')
                        print('OUTPUT', mid)
                        print(f'Total number of comparisons: {i}')
                        print('OUTPUT', i)
                        break   
                    elif target < newlist[mid]:
                        high = mid - 1
                        i += 1
                    else:
                        low = mid + 1 
                        i += 1
                else:       
                    print(f'Target {target} NOT found in list.')
                    print('OUTPUT NOTFOUND')
                    print(f'Total number of comparisons: {i}')
                    print('OUTPUT', i)
            else:
                print('ERROR: List unsorted! Please select option (3) to sort the list.')
                print('OUTPUT ERROR')                            
    elif option == '3':
        print()
        print('OPTION 3: SORT THE LIST')
        for e in range(len(newlist)):
            low = e
            for f in range(e+1, len(newlist)):
                if newlist[f] < newlist[low]:
                    low = f
            if low != e:
                newlist[e], newlist[low] = newlist[low], newlist[e]
        print(f'OUTPUT {newlist}')
    elif option == '4':
        break
    else:
        print('ERROR: Please choose from [1-4]')      
    print('Would you like to continue (y/n)?')
    continue_ = input('CONTINUE> ').strip().lower()
print('OUTPUT Goodbye!')
print('=+'*21)

        

        
    
        
