# Kristin Beener
# CSCI 101 - Section C
# Python Lab 2
print('Input the five lists of characters to be encripted.')
list_1 = input('LIST1> ')
list_2 = input('LIST2> ')
list_3 = input('LIST3> ')
list_4 = input('LIST4> ')
list_5 = input('LIST5> ')
# first list of characters by using [] move last two characters to the beginning
_list_1 = list(list_1)
list1 = _list_1[-2:] + _list_1[0:3]

# second list removes the last character
_list_2 = list(list_2)
list2 = _list_2[:-1]

#third list only the second half of string
_list_3 = list(list_3)
list3len = int(len(list_3)/2)
list3 = _list_3[list3len:]

#fourth list swap 3rd character with 1st character
_list_4 = list(list_4)
_list_4[0], _list_4[2] = _list_4[2], _list_4[0]

# the last list is of characters for the tag
_list_5 = list(list_5)
listlen5 = int(len(_list_5)/2)
list5 = _list_5[0:listlen5]
list5_ = _list_5[-listlen5:]
#creating a list so that i can include the spacing in the final message
spacing_1 = [" ","ignore", "ignore"]
spacing = spacing_1[:1]

#add the encripted message together
encrpt_msg = list5 + spacing + list1 + list2 + list3 + _list_4 + spacing + list5_
newencrpt_msg = "".join(encrpt_msg)
print("The encripted message is:")
print("OUTPUT",newencrpt_msg)

