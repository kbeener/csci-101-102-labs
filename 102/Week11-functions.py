#################################################
######## Kristin Beener                 #########
######## Week 11 - Function Definitions #########
######## CSCI102 Section - E            #########
#################################################

# Imports
import math

################################################
########   Function 1 : print_output   #########
################################################

def print_output(string):
    output = print(f'OUTPUT {string}')
    return output
    
################################################
########   Function 2 : triangle_area  #########
################################################

def triangle_area(height,width):
    area = '{:.2f}'.format((height * width) * 0.5)
    return print_output(area)

################################################
########  Function 3 : feet_to_meters  #########
################################################

def feet_to_meters(feet):
    meters = '{:.3f}'.format(feet/3.2808)
    return print_output(meters)

################################################
########   Function 4 : polar_coords   #########
################################################

def polar_coords(x,y):
    tor = '{:.1f}'.format(math.sqrt(((x**2)+(y**2))))
    totheta = '{:.1f}'.format(math.degrees(math.atan((y/x))))
    r = 'r:' + ' ' + str(tor)
    theta = 'theta:' + ' ' + str(totheta)
    
    print_output(r)
    print_output(theta)
    #what do I do as a return statement?????

################################################
######## Function 5 : is_prime         #########
################################################

def is_prime(integer):
    if integer > 1:
        for i in range(2,integer//2):
            if (integer % i) == 0:
                return print_output(False)
            else:
                return print_output(True)
    else:
        return print_output(False)
        

################################################
######## Function 6 : euros_to_dollars #########
################################################

def euros_to_dollars(cost):
    dollars = cost*1.08
    dollarsdown = '{:.2f}'.format(math.floor(dollars*(10**2))/(10**2))
    return print_output(dollarsdown)





    
