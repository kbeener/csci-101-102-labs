#Kristin Beener
#CSCI 102 - Section E
#Week 8 - Part B
print('What are your author names?')
names = input('NAMES> ')
short = []
for i in range(len(names)):
    if names[i].isalpha():
        if names[i].isupper():
            short.append(names[i])
print(f"OUTPUT {''.join(short)}")
