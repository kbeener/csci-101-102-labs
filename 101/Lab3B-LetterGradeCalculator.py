# Kristin Beener
# CSCI 101 - Section C
# Python Lab 3B

firstname = input('FIRSTNAME> ')
scholars = input('SCHOLARS> ')
weight1 = float(input('WEIGHT1> '))
weight2 = float(input('WEIGHT2> '))
grade1 = int(input('GRADE1> '))
grade2 = int(input('GRADE2> '))
print()
print('=+' * 21)

#do calculations
total_grade = (weight1 * float(grade1)) + (weight2 * float(grade2))

print('Current Grade Percentage of', firstname, 'is:')
print('OUTPUT', "{0:.2f}%".format(total_grade))

#set grading scale and find grade

minimum_grade_scale = [90, 80, 70, 60]

print('Current Letter Grade of', firstname, 'is:')
    
if total_grade >= 90.00:
    print('OUTPUT A')
    
elif total_grade == 80.00:
    print('OUTPUT B')

elif total_grade == 70.00:
    print('OUTPUT C')

elif total_grade == 60.00:
    print('OUTPUT D')

else:
    print('OUTPUT F')

#set scholarship status

print('Updated Scholar Status:')

namelist = scholars.split()

if firstname in namelist and total_grade >= 80.00:
    print('OUTPUT Current')
    
elif firstname in namelist and total_grade == 70.00:
    print('OUTPUT Probation')

elif firstname in namelist and total_grade <= 60.00:
    print('OUTPUT Terminated')
    
elif firstname not in namelist and total_grade == 90.00:
    print('OUTPUT New')

else:
    print('OUTPUT None')

print('=+' * 21)





