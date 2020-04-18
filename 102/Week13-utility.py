# Kristin Beener
# CSCI 102 - Section E
# Week 13 - Incremental Development

def print_output(string):
    output = print(f'OUTPUT {string}')


def load_file(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace('\n','')
    return lines

    
def update_string(string1,string2,indexint):
    stringchar = []
    for char in string1:
        stringchar.append(char)
    stringchar[indexint] = string2
    outputstr = ''.join(stringchar)
    #are we supposed to call print_ouput or just print the output
    #return print_output(outputstr)


def find_word_count(input_list,word):
    count = 0
    words = []
    for i in input_list:
        words.append(i.split())
    for i in words:
        for newwords in i:
            if newwords == word:
                count += 1
    return count


def score_finder(list1,list2,string):
    for i in range(len(list1)):
        if list1[i].lower() == string.lower():
            stroutput = list1[i] + ' got a score of ' + str(list2[i])
        else:
            stroutput = 'player not found'
    print('OUTPUT',stroutput)
    #return print_output(stroutput)??
           
    
def union(list1,list2):
    newlist = list1 + list2
    no_duplicates = []
    for i in newlist:
        if i not in no_duplicates:
            no_duplicates.append(i)
    return no_duplicates


def intersect(list1,list2):
    duplicates = []
    for i in list1:
        if i in list2:
            duplicates.append(i)
    return duplicates
    
