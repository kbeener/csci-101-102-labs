# Kristin Beener
# CSCI 102 - Section E
# Week 2 - Lab - RecieptGenerator

# ask for all the inputs

comp_name = input("Enter company name: ")
comp_street = input("Enter company street address: ")
comp_csz = input("Enter company city/state/zip: ")
cashier_name = input("Enter cashier name: ")
item_1 = input("Purchased item 1 name: ")
item_1_price = float(input("Purchased item 1 price: "))
item_2 = input("Purchased item 2 name: ")
item_2_price = float(input("Purchased item 2 price: "))
item_3 = input("Purchased item 3 name: ")
item_3_price = float(input("Purchased item 3 price: "))
fav_msg = input("Enter your favorite ending message: ")

# now format the receipt
print()
print("{0:^35}".format("RECEIPT GENERATOR"))
print("="*35)
print("{0:^35}".format(comp_name))
print("{0:^35}".format(comp_street))
print("{0:^35}".format(comp_csz))
print("*"*35)
print("{0:^35}".format("Your cashier was: " + cashier_name))
print("{0:^35}".format("Welcome Valued Customer"))
print("*"*35)
print("{0:>13}{1:>18}".format("Item Name","Item Price"))
print()
print(f"{item_1:>16}        ${item_1_price:.2f}")
print(f"{item_2:>16}        ${item_2_price:.2f}")
print(f"{item_3:>16}        ${item_3_price:.2f}")
print()
print("*"*35)
print("{0:^35}".format(f"Total Cost of Order: {item_1_price + item_2_price + item_3_price:.2f}"))
print("*"*35)
print("{0:^35}".format(fav_msg))
print("="*35)
