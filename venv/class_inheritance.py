# Python is an object oriented programming language.
# A Class is like an object constructor, or a "blueprint" for creating objects.

class MyClass:
 x = 5 #x is property of class
p1 = MyClass()
print(p1.x)
#__init__() function is the constructor of class that is executed when the object of class is created
class Person:


 def __init__(self, name, age):
  self.name = name
  self.age = age


p1 = Person("John", 36)
print(p1.name)
print(p1.age)

#we can create object so that class() save in a variable and then later on extract info from that variable like google cache we can directly access
#we can call directly class Person.name
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
#



class Person:
 def __init__(mysillyobject, name, age):
  mysillyobject.name = name
  mysillyobject.age = age

 def myfunc(abc):
  print("Hello my name is " + abc.name)


p1 = Person("John", 36)
p1.myfunc()
# Delete the age property from the p1 object:
# del p1.age
# Delete the p1 object:
# del p1
# All classes have a function called __init__(), which is always executed when the class is being initiated.class(blue print) created and initiated onn object making
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
# The __init__() function is called automatically every time the class is being used to create a new object.
#The __str__() function controls what should be returned when the class object is represented as a string.
#If the __str__() function is not set, the string representation of the object is returned:
class Person:
 def __init__(self, name, age):
  self.name = name
  self.age = age

 def __str__(self):
  return f"{self.name}({self.age})"


p1 = Person("John", 36)
print(p1)
#<__main__.Person object at 0x15039e602100> without str function object print string



