#   Kristin Beener
#   CSCI 102 - Section E
#   Week 12 - Parking Lot

import csv

def check_parking_lot(current_car, parking_lot, handicapped):
  
    for i in range(len(handicapped)):
        if handicapped[i] == current_car:
            handicapped[i] = 'EMPTY'
            #print(handicapped)
            return 'HANDICAPPED'
    for i in range(len(parking_lot)):
        for j in range(len(parking_lot[i])):
            if parking_lot[i][j] == current_car:
                parking_lot[i][j] = 'EMPTY'
                parking_lot[-1] = handicapped
                return 'PARKING'
    if current_car not in parking_lot:
        return 'None'
   
                

def park_handicapped(current_car, handicapped):
    handicapped_full = False
    for i in range(len(handicapped)):
        if handicapped[i] == 'EMPTY':
            handicapped[i] = current_car
            break
    
    for i in handicapped:
        if i == 'EMPTY':
            handicapped_full = False
            #print(handicapped)
            return handicapped_full
    #print(handicapped)
    #print(handicapped_full)
    return True
        #takes one more than it needs
    

def park(current_car, parking_lot):
    parked = False
    parking_lot_full = True
    for i in range(len(parking_lot)-1):
            for j in range(len(parking_lot[i])):
                if parking_lot[i][j] == 'EMPTY':
                    parking_lot[i][j] = current_car
                    parked = True
                    break
            if parked == True:
                break
    for i in range(len(parking_lot)):
         for j in range(len(parking_lot[i])):
             if parking_lot[i][j] == 'EMPTY':
                parking_lot_full = False
                return parking_lot_full
    #print(parking_lot_full)
    return True
                    
    


def run():

    parking_lot_full = False
    
    handicapped_full = False
    
    parking_lot = []
    
    parking_lot_size = 0
    
    with open('parking.csv', 'r') as f:
        csvreader = csv.reader(f, delimiter=',')
        for row in csvreader:
            parking_lot.append(row)
            parking_lot_size += len(row)
    
    
    handicapped = parking_lot[-1]
    
    while parking_lot_full == False:
        current_car = input('LICENSE PLATE> ')
        status = check_parking_lot(current_car, parking_lot, handicapped)
        if status == 'None':
            #entering
            if (current_car[0].lower() == 'h') and handicapped_full == False:
                handicapped_full = park_handicapped(current_car, handicapped)
                parking_lot[-1] = handicapped
                if handicapped_full == True:
                    for i in parking_lot:
                        for j in i:
                            if j == 'EMPTY':
                                 parking_lot_full = False
                    parking_lot_full = True
                    
            
                
            elif (current_car[0].lower() != 'h') or handicapped_full == True:  
                parking_lot_full = park(current_car, parking_lot)
                
                
    return parking_lot
        
            

###############################################################################
# #################### DO NOT MODIFY BELOW THIS LINE ######################## #
###############################################################################

parking_lot = run()

print('!PARKING LOT FULL!')
print('!WRITING RESULTS TO output.csv!')
with open('output.csv', 'w', newline='') as f:
    w = csv.writer(f)
    for row in parking_lot:
        w.writerow(row)
