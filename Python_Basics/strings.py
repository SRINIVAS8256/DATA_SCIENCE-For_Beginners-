#strings are sequence of unicode
#print('\u0C89')
#utf unicode transformation format


#strings are unicode by default


# creating strings
# accessing strings
# adding chars to strings
# editing strings
# deleting strings
# operations on strings
# string function



#Creating Strings

#types of indexing
#1. positive
#2.negative
a="srinivas"
print(a[0:3:2])
print(a[-1])
n=len(a)*-1
print(n)
print(a[-1:n-1:-1])
l=[1,2,3]
for i in range(len(a)-1,-1,-1):
    print(a[i],end=" ")
print(list(a))
#strings are immutable
a="seena"
print(a[0])

#string deletion
del a #delets the object a
# print(a) # not found
a="single"
del a[0]#'str' object doesn't support item deletion

#Operations on string

# arithmetic operation
# relational operation
# logical operation
# loops on strings
# membership operations


# arithmetic operation

print("hello"+"-"+"world") #string concatination

print("#"*50)  #string multiplication


# relational operation
print("hello" == "world")#equal to

print("hello" != "world")#not equal to

print("single" > "seena") #True ,Lexiographically on the basis of dictionary word

print("single" < "seena") #False

# logical operation
#IIIMMP
#IN STRINGS NON EMPTY STRINGS=1(TRUE) AND EMPTY =0(FALSE)

print("" and "") #empty
print("hello" and "") #empty
print("hello" and "world")#priority always for 2 world
print("hi" and "bye")#bye cause of priority e
print("seena" and "hello")# hello
print("" or "")
print(not "hello") #false
print("hi " or "a")#hi priority always for 1
print(" " or "hi") #empty space also counts
print(" " and "hi") #gives " " because space also counts

#loops in strings

c="hello world"
for i in c:
    print(c ,end="") # hello world

# membership operations
print("h" in c)#true
print("H" in c)#false
print("world" not in c)# false





#String functions

#common functions
#iiiiimmmmmmpppppp
#len   max   min  sorted
c="srinivas" #cuz python is dynamically typed language
print(len(c))
print(max(c))
print(min(c))
print(sorted(c))


#iiimmmp
# 1. Capitalize/ Title /Upper/Lower/Swapcase
c="sRinivAs dr"
print(c.capitalize()) #Srinivas dr
print(c.title()) #Srinivas Dr
print(c.upper())#SRINIVAS DR
print(c.lower())#srinivas dr
print(c.swapcase())#SrINIVaS DR  swaps upper to lower and lower to upper

#2. COUNT
print(c.count("s")) # 2 cuz only 2 s present in object c

#3.Find/Index
#IN THIS IT WILL GIVE THE INDEX OF THE VALUE
c="srinivas"
print(c.find("s"))#gives 0 index


print(c.find("sri"))#return 0

print(c.find("sfg")) #return -1 cuz can't find("not present")
# even we can use index
#eg
print(c.index("s"))

#4. endswith/startswith
c="its raining"
print(c.endswith("ing")) #True
print(c.endswith("rain")) #False
#start with
print(c.startswith("its"))#True
print(c.startswith("ts"))#False


#iiimmmppp
#5. format string (FSTRING)

print("hello my name is {} and i am {}".format("srinivas",19))
a=input("enter ur name")
b=int(input("age ="))
print("hello my name is {1} and i am {0}".format(a,b)) # 1 and 0 are index { } are like blanks
#we need to enter values by f string and even we can access that by index
a=input("enter ur name")
b=int(input("age ="))
#iiimmmppp
print(f"hello my name is {a} and i am {b}")#even we can access f string like this

#6.
#isalnum
#isalpha
#isdecimal
#isdigit
#isidentifier

#isalnum   means an object contains both alphabets and numbers
c="seena"
print(c.isalnum()) #false
c="seena7"
print(c.isalnum())#True
c="seena 7"
print(c.isalnum())#False because we have space here even space also counts

#isalpha means checks whether the object contains alphabets or not
c="seena"
print(c.isalpha())#True
c="see na"
print(c.isalpha())#False cuz of space

#isdigit checks whether the object contains digits(nums) or not
c="23"
print(c.isdigit()) #True
c=23
print(c.isdigit()) #False cause int is an object has no attributes
c="23.34"
print(c.isdigit())#False

c="23.23"
print(c.isdecimal())#True

#we have many .is functions
#isidentifier
print("helloworld".isidentifier())#True
print("hello world".isidentifier())#False cuz of space
print("hello_world".isidentifier())#True

#7. split() it divides the strings , it will make  a list[]
c="i am srinivas dr"
print(c.split())#['i', 'am', 'srinivas', 'dr']
print(c.split("a")) #['i ', 'm sriniv', 's dr']
print(c.split("x")) # gives normal list


#8.  join()    it will join the strings in the list
c=['who', 'is', 'the', 'prime', 'minister', 'of', 'india']
print("/".join(c)) #who/is/the/prime/minister/of/india

#9.replace()
c="i am srinivas"
print(c.replace("srinivas","seena"))# i am seena

#10.strip() it removes starting and ending space in astring
c="       hi i am seena      "
print(c.strip()) #hi i am seena
