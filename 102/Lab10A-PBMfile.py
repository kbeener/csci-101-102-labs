#Kristin Beener
#CSCI 102 - Section E
#Week 10 - Part A

#ask user for CSV name and PBM name
print('Provide the input CSV file name:')
csvname = input('CSVFILE> ')
print('Provide the output PBM file name:')
pbmname = input('PBMFILE> ')

#open the file and read it
import csv
output = ['P1']
with open(csvname) as csvfile:
    contents = csvfile.readlines()
    height = len(contents)
    width = 0
    for i in contents[0]:
        if i.isdigit():
            width += 1
    line2 = str(width) + ' ' + str(height)
    output.append(line2)
#replace the commas with spaces and the newlines with nothing
    for i in contents:
        i = i.replace(','," ")
        i = i.replace('\n','')
        output.append(i)
#write the contents of the list into a pbm file
with open(pbmname, 'w') as pbmoutput:
    for i in output:
        pbmoutput.write(i)
        pbmoutput.write('\n')
#check to see if the file has the correct contents
#print()
#with open(pbmname,'r') as file:
    #print(file.read())
    
