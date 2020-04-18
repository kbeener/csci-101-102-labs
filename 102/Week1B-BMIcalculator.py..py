# Kristin Beener
# CSCI 102 - Section E
# Week 1 - Part B
print('Input your weight, in pounds.')
weight = int(input('WEIGHT> '))
print('Input your height, in inches.')
height= int(input('HEIGHT> '))
m = weight * 0.454
h = height * 0.0254
user_bmi = round(m / (h**2),1)
print('Your Body-Mass Index is:')
print('OUTPUT', user_bmi)
