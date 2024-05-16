print("My name is maham")
'''name = input("Enter name")
if name == "Maham":
    print("Hello Maham")
else:
    print("Hello others ")'''

'''hi
hi'''
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(type(x) , "  ", y, " ",z)
o= -25
print(type(o))

import random

print(random.randrange(1, 1000))
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(thislist[1])
print(thislist[-1])
#-1 refers to the last item, -2 refers to the second last item etc.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#Note: The search will start at index 2 (included) and end at index 5 (not included).
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#0-3 index -->:4
print(thislist[2:])
#2-end-->2:
print(thislist[-4:-1])
#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist[0])
#To add an item to the end of the list, use the append() method:
#To insert a list item at a specified index, use the insert() method.
thistuple = ("apple", "banana", "cherry")
print(thistuple)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
set1 = {"abc", 34, True, 40, "male"}
print(set1)
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
#key value pair
num = int(input("Ennter marks"))
if num < 60:
    print("Fail")
elif num >= 60 and num <70:
    print("C")
elif num >= 70 and num <80:
    print("B")
elif num >= 80 and num <90:
    print("A")
elif num >= 90 and num<= 100:
    print("A+")
else:
     print("Out of range number")
#command / for commenting multiple line

for i in range (0,10):
    i=i+1
    if (i==5):
        break
    print(i)
#fn + f9 is used to open debugger mode and then just run this command
for x in range(2, 6):
  print(x)
#while loop is used kab tk (Value define)
#for loop is used kha tk (Value define )