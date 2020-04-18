#Kristin Beener
#CSCI 101 - Section C
#Create Project

#there is a bug that causes some songs to be printed twice at a random order
import random

def list_sorting(songlist,option):

        sortedlist = []
        while songlist:
            minnum = songlist[0][option]
            firstele = songlist[0]
            for j in songlist:
                if j[option] < minnum:
                    minnum = j[option]
                    firstele = j
            sortedlist.append(firstele)
            songlist.remove(firstele)
        return sortedlist
    
def remove_duplicates(songlist):
    finallist = []
    for i in songlist:
        if i not in finallist:
            finallist.append(i)
    return finallist


print()
print("Welcome to Rolling Stone's Top 500 Random Song Generator")
print('*'*40)

#obtain user preferences
print('How many songs would you like?')
numrecs = int(input('Number: '))
print()

print('Please input a number to generate a random list.')
seed = int(input('Number: '))
print()

print('How would you like the songs to be listed? \n1.Number\n2.Artist\n3.Title\n4.Year\nPlease eneter a number 1-4.')
sorting = input('Choice: ')
print()

#open txt file of songs and read each line and save as a list
with open('Createprojectsongs.txt') as songs:
    allsongs = songs.readlines()
   
#choose random songs and save them to be sorted
songrecslist = []
random.seed(seed)
for i in range(0,numrecs):
    index = random.random() * len(allsongs)
    songrecslist.append(allsongs[int(index)])
    
#seperate the songs into their catagories
for i in range(len(songrecslist)):
    songrecslist[i] = songrecslist[i].split('/')
#start the sorting process
if sorting == '1':
    option = 0
    for i in songrecslist:
            i[option] = int(i[option])
    output = list_sorting(songrecslist,option)
elif sorting == '2':
    option = 1
    output = list_sorting(songrecslist,option)
elif sorting == '3':
    option = 2
    output = list_sorting(songrecslist,option)
elif sorting == '4':
    option = 3
    for i in songrecslist:
            i[option] = int(i[option])
    output = list_sorting(songrecslist,option)
    for i in output:
        i[3] = str(i[3])
else:
    print('please enter a number 1-4')

#print out the songs as a string replacing uneccessary newlines with ''

print('Here are the recommendations!')
print('*'*40)

print()
finallist = remove_duplicates(output)
for i in finallist:
    i[3] = str(int(i[3]))
    i[0] = str(i[0])
    print(f'Number: {i[0]}    Artist: {i[1]}    Title: {i[2]}    Year: {i[3]}')
    print()



