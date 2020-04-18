#Kristin Beener
#CSCI 102 - Section E
#Week 8 - Part A
print('What size 2D list would you like to create?')
n = int(input('N> '))
print()
#should the n input be less than 10?????
if n <= 10 and n >= 0:
    origlist = []
    for i in range(n):
        innerlist = []
        for j in range(n):
            j = 1 + j + (i * n)
            innerlist.append(j)
        origlist.append(innerlist)
    print('The original list is:')
    print('[', end=" ")
    for i in origlist:
        print(i,end=",\n")
    print(']')
    print()

    #first way to reverse
    copylist = origlist[:]
    revlist = []
    newlist = []
    reversedlist = []
    for k in range(len(copylist)):
        revlist = []
        for j in range(len(copylist[k])-1,-1,-1):
            revlist.append(copylist[k][j])
        newlist.append(revlist)
    for i in range(len(copylist)-1,-1,-1):
        reversedlist.append(newlist[i])
    print('The reversed list is:')
    print('[', end=" ")
    for i in reversedlist:
        print(i,end=",\n")
    print(']')
    print()

    #second way to reverse
    copylist2 = origlist[:]
    for k in copylist2:
        k.reverse()
    copylist2.reverse()
    print('The reversed list is:')
    print('[', end=" ")
    for i in copylist2:
        print(i,end=",\n")
    print(']')
    print()
else:
    print('Error')

    
        

        
    
