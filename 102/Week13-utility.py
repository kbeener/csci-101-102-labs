# Kristin Beener
# CSCI 102 - Section E
# Week 13 - Incremental Development

def print_output(string):
    output = print(f'OUTPUT {string}')


def load_file(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
        for i in lines:
            i = i.replace('\n','')
        print('OUTPUT',lines)

