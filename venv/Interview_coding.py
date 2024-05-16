"""Camel Case - In the camel case, each word or abbreviation in the middle of begins with a capital letter. There is no intervention of whitespace. For example - nameOfStudent, valueOfVaraible, etc.
Pascal Case - It is the same as the Camel Case, but here the first word is also capital. For example - NameOfStudent, etc.
Snake Case - In the snake case, Words are separated by the underscore. For example - name_of_student, etc."""
a,b,c=1,2,3
print(a,b,c)


x=100
def func():
   y=20
   print(x)
   print(y)

func()
print(x)
#print(y)
c = 1+3j
print("The type of c", type(c))
print(" c is a complex number", isinstance(1+3j,complex))

tons = list(range(10,20))
print(tons[0:8])
print(tons[8:])
tons[3]=100
print(tons)


tons1 = tuple(range(5))
#tons1[3]=100
print(tons1)
print(tons1[4])

d = {1:'Jimmy', 2:'Alex', 3:'john', 4:'mike'}
print("2nd name is " + d[4])
print(d.keys())
print(d.values())

#Removal Spaces in array
list=["   apple", "banana    "]
fruits=[]
for word in list:
    correct= word.strip()
    fruits.append(correct)
print(fruits)

#Removal Duplicate
list2=["apple", "banana","apple",1,1 ]
fruits2=[]
for word in list2:
   if word in fruits2:
       continue
   else:
       fruits2.append(word)
print(fruits2)


#Max Number
arr = [3, 7, 2, 8, 5, 9, 1, 4]
max_num = arr[0]  # Assume the first element is the maximum
for num in arr:
    if num > max_num:
        max_num = num
print("Maximum number in the array:", max_num)

#desending order sort array
arr = [3, 7, 2, 8, 5, 9, 1, 4]
sorted_arr_descending = []
while arr:  # Continue until arr is not empty
    max_num = arr[0]  # Assume the first element is the maximum
    for num in arr:
        if num > max_num:
            max_num = num
    sorted_arr_descending.append(max_num)
    arr.remove(max_num)  # Remove the maximum element from the original array
print("Array sorted in descending order:", sorted_arr_descending)

#factorial
n=4
factorial= 1
for i in range (1,n+1):
    factorial=factorial* i
    print(factorial)

#missing number
s = [1, 2, 5, 6,9,10]
num = 1
for i in s:
    if i == num:
        print("Number", i, "is present")
        num += 1
    else:
        while num < i:
            print("Number", num, "is missing")
            num += 1
        print("Number", i, "is present")
        num = i + 1





#palindrome
letter = "abaaba"
start=0
end= len(letter)-1
for i in letter:
  if letter[start] ==letter[end]:
    print(letter[start],letter[end],"paliundrome")
    start=start+1
    end=end-1
  else:
      print("letter not palindrom",letter[start],letter[end])
      break


#reverse letter same of actual
name="maham"
endig=len(name)-1
ar=[]
arri=""
for i in name:
    arri =arri + name[endig]
    ar.append(name[endig])
    print(name[endig])
    endig=endig-1
print(ar)
print(arri)
if name == arri:
    print("same")
else:
    print("not same")

#fabconni series
sum=0
n1=0
n2=1
for i in range(0,10):
    print(sum)
    n1=n2
    n2=sum
    sum= n1 + n2

#even
nm= 9
#nm= int(input("Enter nm"))
if nm%2 !=0 and nm>=0:
    print("Number is odd and positive")
elif  nm%2==0:
    print("Number is even ")
elif nm<0:
    print("Numver is negative")
else:
    print("Not a number")

#prime Numbers
nm1=5
#nm1 = int(input("Enter number"))
if num <=1:
    print("Not a prime number")
else:
    for i in range(2,nm1):
        if nm1%i==0:
            print("not prime")
            break3

        else:
            print("prime")
#circle and triangle
r = 2.5
print("Area of Circle", 3.14*r*r )
l=3
w=5
print("Area of triangle", 1/2*(l+w))

"""In many ways, a tuple is like a list. Tuples, like lists, also contain a collection of items from various data types. A parenthetical space () separates the tuple's components from one another.
Because we cannot alter the size or value of the items in a tuple, it is a read-only data structure."""
