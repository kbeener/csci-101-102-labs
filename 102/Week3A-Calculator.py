# Kristin Beener
# CSCI 102 - Section E
# Week 3A - Calculator 

operand_one = 0.0
operand_two = 0.0

_sum = 0.0
_difference = 0.0
_product = 0.0
_quotient = 0.0
_remainder = 0.0

print('Welcome to our 101 Calculator!')

print('Input the first operand.')
operand_one = float(input('FIRST> '))
                    
print('Input the second operand.')
operand_two = float(input('SECOND> '))

print()

print('Choose one of the following operations:')
print('  1 - addition')
print('  2 - subtraction')
print('  3 - multiplication')
print('  4 - division ')

operation = input('OPERATION> ')

if operation == '1':
    _sum = operand_one + operand_two
    print('result: ', "{0:.6f}".format(_sum))
                    
elif operation == '2':
    _difference = operand_one - operand_two
    print('result: ', "{0:.6f}".format(_difference))
                    
elif operation == '3':
    _product = operand_one * operand_two
    print('result: ', "{0:.6f}".format(_product))
                    
elif operation == '4':
    _quotient = operand_one // operand_two
    _remainder = operand_one % operand_two
    print('quotient: ', round(_quotient))
    print('remainder: ', round(_remainder))
                    
print('Thank you for using our calculator.')
