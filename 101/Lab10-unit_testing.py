# Kristin Beener
# CSCI 101 - Section C
# Python Lab 10

def multiply(a,b,output):
    product = a * b
    if output == product:
        return True
    else:
        return False
    
def bounds_checking(lower,upper,length):
    if lower < 0:
        return False
    elif upper > length:
        return False
    elif upper < lower:
        return False
    else:
        return True
    
def decimal_points(floatnum):
    splitnum = str(floatnum).split('.')
    decimal= splitnum[1]
    if len(decimal) == 3:
        return True
    else:
        return False
    
def list_sorted(inputlist):
    if inputlist == sorted(inputlist):
        return True
    else:
        return False
    
def reversed_list(list1,list2):
    newlist1 = list1[::-1]
    if newlist1 == list2:
        return True
    else:
        return False
    
def num_ohs(n,list2d):
    count = 0
    for i in list2d:
        for j in i:
            if j == 'o' or j == 'O':
                count += 1
    if count == n:
        return True
    else:
        return False
    
def check_cs(string):
    listcs = []
    for i in string:
        if i == 'c' or i == 's':
            listcs.append(i)
    if listcs[0] != 'c':
        return False
    elif 's' not in listcs:
        return False
    else:
        return True
    
