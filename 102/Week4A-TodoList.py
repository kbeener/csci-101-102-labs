# Kristin Beener
# CSCI 102 - Section E
# Week 4A - Todo List


print('Welcome to the TODO List tracker! Please enter the tasks that you need to do this week. To stop entering tasks, enter "DONE" (without quotation marks).')

number_of_tasks = 0

lots_to_do = 7

not_much_to_do = 4

task = input('TASK> ')


while task != 'DONE':
    number_of_tasks = number_of_tasks + 1
    task = input('TASK> ')
    
if number_of_tasks > lots_to_do:
    print('You have', number_of_tasks, 'tasks to do. You have lots to do! You better get to work!')
    print('OUTPUT', number_of_tasks)
    print('OUTPUT BUSY')
elif number_of_tasks < not_much_to_do:
    print('You have', number_of_tasks, "tasks to do. You don't have much to do, enjoy a break!")
    print('OUTPUT', number_of_tasks)
    print('OUTPUT FREE')
else:
    print('You have', number_of_tasks, 'tasks to do. You have a moderate amount of work to do.')
    print('OUTPUT', number_of_tasks)
    print('OUTPUT MODERATELY')
