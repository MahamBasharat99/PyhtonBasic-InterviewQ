# Keyword Arguments
# You can also send arguments with the key = value syntax.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Email", child2 = "Tobias", child3 = "Linus")

#Arbitrary Arguments, *args
#If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is ", kids)
my_function("Emil", "Tobias", "Linus","Ali","Maham")

def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Email", "Tobias", "Linus")

# Arbitrary Keyword Arguments, **kwargs
# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])
  print(kid)
my_function(fname = "Tobias", lname = "Refsnes", surname="Basharat",address="xyz")

# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
#command + forward slash is used to multiline comment
#function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
#Python also accepts function recursion, which means a defined function can call itself.
#its decrement -1 everytime
#Use the len() method to return the length of an array (the number of elements in an array).
# Python has a set of built-in methods that you can use on lists/arrays.
# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
# Python Classes/Objects
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects.

#Recursive function
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


