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
    print_output(outputstr)

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
            
    
