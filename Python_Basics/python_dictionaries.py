#List
#1.what is List
#1.List vs Array
#2.create
#3.Access
#4.Edit
#5.Add
#6.Delete
#7.operations
#8.Functions

#1.List vs Array

#1.array homogeneous list heterogeneous
#2.Arrays are faster(because data stored linearly in the memory)
#in list its not stored continuously (cause slower)
#3.Lists are more programmer friendly


#2.creating list

#l=[]
l=[1,2,4,5]#homogeneous list
l2=["hello",1,1.2,1+3,5+6j]#heterogeneous list

#Multi-dim lists
#2D
l3=[1,2,3,[4,5,6]]#heterogenus cuz integer and list in the list

#3D
l4=[[[1,2],[3,4],[5,6],[7,8]]]

l5=list("seena")#converts string to list
l6=list()#creates empty list


#Accessing List
l7=[1,2,3]
print(l7[0])#gives 1
#In 2D
l8=[1,2,3,[4,5,6]]

# collection = single "variable" used to store multiple values
# List   = [] ordered and changeable. Duplicates OK
# Set    = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple  = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "coconut"]

# Explore list methods and functions
# print(dir(fruits))         # Shows all methods for list
# print(help(fruits))        # Shows detailed help for list
# print(len(fruits))         # Returns number of elements
# print(min(fruits))
# print(max(fruits))
#print(l.sort()) permanent operation affects to list
#print(l.index[3]) # gives the position of 3 in the list
# print(sorted(fruits)) [23, 4342, 12313] #sorted is temporary operation
# print(sorted(fruits,reverse=True))      [12313, 4342, 23]
# print("pineapple" in fruits) # Checks for item presence membership operator

# List modification operations
# fruits[0] = "pineapple"    # Replace first element
# fruits.append("pineapple") # Add item at end
# fruits.remove("apple")     # Remove item
# fruits.insert(0, "pineapple") # Insert at specific position
# fruits.sort()              # Sort list
# fruits.reverse()           # Reverse list
# fruits.clear()             # Remove all elements
# print(fruits.index("apple")) # Find index of item
#extend will coverts the data into list add that to it individually
l=['hi', 1, 2, 3, 1]
l.extend("seena")
print(l)
#output ['hi', 1, 2, 3, 1, 's', 'e', 'e', 'n', 'a']

fruits.count("pineapple")    # Count occurrences of "pineapple"
print(fruits)                # Output the list

#list
#Delete
#del
#remove
#pop
#clear

l=[1,2,4,54,56,6,"hi"]
del l[0]#deletes the value at 0th index
del l#deletes the entire list
print(l)#not found

print(l.remove("hi"))

print(l.pop())#removes the last element

print(l.clear())#it won't delete the list but makes empty

print(l+l2)#concatination of list
print(l*3)#multiplication  of list [12313, 4342, 23, 12313, 4342, 23, 12313, 4342, 23]
sample="seena"
l=[]
for i in sample.split():
    l.append(i.capitalize())
print(" ".join(l))


sample="abc@gmail.com"
print(sample[:sample.find("@")])#abc
#remove duplicates
l1=[1,11,123,444,1]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)

t6=[1,21,234,234,56,45,5,32]
del t6[-1]
t6.remove(t6[t6.index(21)])
print(t6)#result [1, 234, 234, 56, 45, 5]







# Tuple: ()
# Ordered ✅, Unchangeable ❌, Duplicates ✅

fruits_tuple = ("apple", "orange", "banana", "apple")

# print(dir(fruits_tuple))
# print(help(fruits_tuple))
# print(len(fruits_tuple))
# print("banana" in fruits_tuple)

# print(fruits_tuple[1])         # Access by index
# print(fruits_tuple.count("apple"))
# print(fruits_tuple.index("banana"))

print("Tuple:", fruits_tuple)
#Tuples
#Create
#Access
#Edit
#Add
#Delete


#Create
t1=() #creating tuple
type(t1) #tuple

t1=(1,2,4)#homogenous tuple cuz same datatype(int)
t2=("hi",1,2,3.423,"hello")#heterogenous tuple
t2d=((1,2,3),(4,5,6))#2d tuple

#confusions while creating tuple
#1.
t4=("hi")
type(t4)#string type
#to overcome
t4=("hi",)#tuple
type(t4)#now it's a tuple


 #converting string to tuple()
t6=tuple("seena")
print(t6)#('s', 'e', 'e', 'n', 'a')

#converting list to tuple
t6=[1,21,234]
t6=([t6])
print(t6)#[[1, 21, 234]]
type(t6)#list

#Accessing tuples
print(t2[1])
print(t2[-1])
print(t2d[1][0])

#Tuple Editing
#tuples are immutable doesn't support item editing(assigning deleting etc)
t6[0] =1# TypeError: 'tuple' object does not support item assignment

#deleting tuple
del t6 #deletes tuple

#Operations
#concat
print(t2+t2d)#('hi', 1, 2, 3.423, 'hello', (1, 2, 3), (4, 5, 6))S
#we can use loops and membership operator "in"

#Functions in Tuple
t2=( 1,2,3.423 )
print(len(t2))
print(min(t2))
print(max(t2))
print(sum(t2))
sorted(t2,reverse=True)
#tuples are read only datatype




#set{}
# Set: {}
# Unordered ❌, Changeable ✅ (via add/remove), Duplicates ❌

fruits_set = {"apple", "orange", "banana", "apple"}

# print(dir(fruits_set))
# print(help(fruits_set))
# print(len(fruits_set))
# print("banana" in fruits_set)

# fruits_set.add("coconut")
# fruits_set.remove("apple")
# fruits_set.discard("grape")   # No error if item not found
# fruits_set.clear()

print("Set:", fruits_set)


#💯👿iimmpp
#SETS
#rules
#1.sets don't allow duplicates
#2.sets have no indexing/slicing
#3.sets don't allow multiple data types(eg list)
#4.set itself is a mutable datatype

#1.creating a set
s1={}
print(type(s1))#returns dictionary <class 'dict'> 👿👿
#to create an empty set
s1=set()
print(type(s1))#<class 'set'>

#proof that sets doesn't support mutable datatypes example list
s2={[1,2,3],"seena"}
print(s2)# unhashable type: 'list'

#and set allows immutable datatype that's tuple()
s3={(1,2,3),"seena"}
print(s3)#{'seena', (1, 2, 3)}
#💯💯sets have no indexing and we can't create multidimensional sets because set itself is a mutable  it will support mutable datatypes
#Hashing
s4={{1,2},{3,4}}
print(s4)# unhashable type: 'set'

#set object doesn't supports indexing
s4={1,2,3,43}
print(s4[0])#'set' object is not subscriptable

#Editing
#👿we can't edit set items
#example
#by converting set into list and editing the list and converting the same list into set this won't edit set but creates a new set
s5={1,2,3,4}
print(id(s5))
l=list(s5)
l[-1]=5
s5=set(l)
print(s5)
print(id(s5))
#output
# 2483463132480
# {2, 3, 4, 5}
# 2483463131136  address changed

#ADD
# 💯 we can add items into set by using .add() function
s1={1,2,3}
print(id(s1))
s1.add(5)
s1.add("seena")
print(id(s1))
#address are same 2483463129344
#                 2483463129344
print(s1) #{1, 2, 3, 'seena', 5}

#delete 💯
#1. del
#2.remove
#3.pop
s1={1,2,3,4,5,6,7,8,9,10}
s2={"hi" ,"hello"}

#1. del
del s2 # deletes the set s2
print(s2)#name 's2' is not defined

#👿we can't delete set items by indexing
del s1[0]#    'set' object doesn't support item deletion

#remove set{}
s1.remove(1)#removes the item 1 from set s1

#POP()
s1.pop()#removes the item from list s1 (deletion of last item in hashing)


#💯set operations
s1={1,2,3,4,5,6,7,8}
s2={11,22,33,44,55,66,77,88}
#1.👿set doesn't supports concatination
print(s1+s2)# unsupported operand type(s) for +: 'set' and 'set'

#👿 set doesn't supports scalar multiplication
print(s1*3)#unsupported operand type(s) for *: 'set' and 'int'

#💯3. supports iterations
for i in s1:
    print(i)
#💯4. supports membership operation
print(1 in s1)#True


#💯Functions on sets
#1.len
print(len(s1))

#2.min
print(min(s1))
#3.max
print(max(s1))

#4.sum
print(sum(s1))
#5. sorted
print(sorted(s1))
print(sorted(s1,reverse=True))

#6.union means it will give all elements present in two sets which are union
s1={1,2,3}
s2={4,5,6}
s1.union(s2)#{1, 2, 3, 4, 5, 6} #💯doesn't give duplicate value

#7.intersection gives the values present in both lists
s1={1,2,3}
s2={2,3,4}
s1.intersection(s2) #{2,3}

#8.difference  it gives the missing elements in the list when comparing
s1={1,2,3}
s2={2,3,4}
s1.difference(s2)#gives the missing element of s1 in s2
#output = {1}

#9. .symmetric_difference
s1={1,2,3}
s2={2,3,4}
s1.symmetric_difference(s2)#{1,4} checks both the lists and gives unpresented elements
#10 isdisjoint issubset issuperset
print(s1.isdisjoint(s2))#False
print(s1.issubset(s2))#False
print(s1.issuperset(s2))#False
s1.clear() #clears the data



# Dictionary: { key: value }
# Keys must be unique, values can be anything

student = {
    "name": "John",
    "age": 21,
    "marks": 87.5,
    "passed": True
}

# print(dir(student))
# print(len(student))
# print("age" in student)

# Access
# print(student["name"])
# print(student.get("marks"))

# Modify
# student["age"] = 22
# student["city"] = "Bangalore"

# Delete
# del student["passed"]
# student.pop("marks")
# student.clear()

# Keys & values
# print(student.keys())
# print(student.values())
# print(student.items())

print("Dictionary:", student)
#

#dictionaries RULES
#💯💯iiimmmmppp
# >>>R1: Dictionary has no indexing
# >>> # R2: Dictionary is a mutable types
# >>> # R3: Keys-> immutable, values -> they can be mutable
# >>> # R4: Keys should be unique
# >>> # Mutable -> List/Sets/Dictionary
# >>> # Immutable -> Strings/tuples/int/float/Boolean/complex


# >>> # Create
# >>> D = ()
# >>> D
# 30
#
# >>> D = ("Name":"Nitish", "Gender":"Male"}
# >>> D
# ('Name': 'Nitish', 'Gender': 'Male']
# >>> D1 ([1,2,3]: "Nitish"]
# Traceback (most recent call last):
# File "<pyshell#254>", line 1, in <module>
# D1 ([1,2,3]: "Nitish"]
# TypeError: unhashabletype:'list'


#1.creating dict
d1={"name" :"seena","age":19}

#💯creating 2d dict
d2={"name":"seena","age":19,"marks":{"m1":35,"dsa":90}}

#2.Accessing items in dict
print(d2["name"]) #seena
print(d2["marks"]["dsa"]) # 90
d1.get("name")#"seena"


#Editing dict
d2["name"]="srinivas"
print(d2) #{'name': 'srinivas', 'age': 19, 'marks': {'m1': 35, 'dsa': 90}}
d2["marks"]["m1"]=100
print(d2)#{'name': 'srinivas', 'age': 19, 'marks': {'m1': 100, 'dsa': 90}}

#Add new key-value pairs
d2["address"]="mandya"
d2["marks"]["eng"]=60
print(d2)#{'name': 'srinivas', 'age': 19, 'marks': {'m1': 100, 'dsa': 90, 'eng': 60}, 'address': 'mandya'}


#deleting dict
#del
del d2["address"]#{'name': 'srinivas', 'age': 19, 'marks': {'m1': 100, 'dsa': 90, 'eng': 60}}
#ADRESS DELETED

#clear() makes the dict empty
d2.clear()
print(d2)#{} empty dict


#💯Operations

#1.concatination
#❌not support d1+d2

#2.mul
#❌not support d1*2

#✅ dict supports iteration
d2={"name":"seena","age":19,"marks":{"m1":35,"dsa":90}}
for i in d2:
    print(f"{i} : {d2[i]}")
#output
# name : seena
# age : 19
# marks : {'m1': 35, 'dsa': 90}


#memership operation on dict
#✅IIIIMMMMPPP💯only deals with keys of dictionary
d2={"name":"seena","age":19,"marks":{"m1":35,"dsa":90}}
print("seena" in d2)#False

print("name " in d2 )#False ❌❌❌because of indentation in key

print("name" in d2)#True


#len
print(len(d2))#gives the nor of pairs of key:values
#output = 3

#min
print(min(d2)) # gives lexiographycally
d3={"name":"seena","age":19,"marks":{"m1":35,"dsa":90,"ada":"xcellent","daa":"excellent"}}
print(min(d2))#'age'

print(max(d2))#'name'

#"sorted"
sorted(d2)#['age', 'marks', 'name']

sorted(d2,reverse=True)#['name', 'marks', 'age']


#✅ some functions on dict
print(d2.keys())#dict_keys(['name', 'age', 'marks'])

print(d2.values())#dict_values(['seena', 19, {'m1': 35, 'dsa': 90, 'ada': 'xcellent'}])


# 🔚 Conclusion for List, Tuple, Set, Dictionary in Python
# 🟦 LIST
#
# ✅ Mutable: You can change, update, add, or delete elements.
#
# 📥 Ordered: Maintains the order in which elements were inserted.
#
# 🔢 Indexed: Supports indexing and slicing (list[0], list[-1], list[1:3]).
#
# ♻ Allows Duplicates: You can have repeated values.
#
# 📦 Defined using: []
# Example: my_list = [1, 2, 2, 3, "hello"]
#
#
# 🔹 Rules and Characteristics
#
# Dynamic in size.
#
# Heterogeneous (can store any data type).
#
# Can be nested: list = [1, [2, 3]]
#
# Common Methods: append(), extend(), insert(), remove(), pop(), sort(), reverse()
#
#
# ✅ Use When
#
# You need to maintain insertion order.
#
# You need frequent modifications (add/remove/update).
#
# You want to use indexing or slicing.





# 🟪 TUPLE
#
# ❌ Immutable: Cannot change after creation (elements fixed).
#
# 📥 Ordered: Keeps the insertion order.
#
# 🔢 Indexed: Supports indexing and slicing.
#
# ♻ Allows Duplicates.
#
# 📦 Defined using: ()
# Example: my_tuple = (1, 2, "hello")
#
#
# 🔹 Rules and Characteristics
#
# Faster than list (better for read-only data).
#
# Supports nesting and heterogeneous types.
#
# Can be used as keys in dictionaries (if the tuple itself is immutable).
#
# Common Methods: count(), index()
#
#
# ✅ Use When
#
# Data should not change (e.g., coordinates, constant values).
#
# You want performance benefits.
#
# You need hashable types (e.g., dict keys, set elements).





# 🟩 SET
#
# ✅ Mutable (but only the whole set — elements themselves must be immutable).
#
# ❌ Unordered: Does not maintain insertion order (as of Python < 3.7).
#
# ❌ No Indexing: You can't access elements using an index.
#
# 🚫 No Duplicates: Automatically removes duplicate entries.
#
# 📦 Defined using: {} or set()
# Example: my_set = {1, 2, 3}
#
#
# 🔹 Rules and Characteristics
#
# Only stores unique values.
#
# Good for set operations: union, intersection, difference.
#
# All elements must be hashable.
#
# Common Methods: add(), remove(), discard(), union(), intersection(), difference()
#
#
# ✅ Use When
#
# You need to remove duplicates.
#
# You need to perform mathematical set operations.
#
# You don't care about order or indexing.





# 🟨 DICTIONARY
#
# ✅ Mutable.
#
# 📥 Ordered (from Python 3.7+).
#
# 📌 Key-Value Pair: key: value structure.
#
# 🚫 No Duplicates in Keys: Keys must be unique and immutable (strings, numbers, tuples).
#
# 📦 Defined using: {key: value}
# Example: my_dict = {"name": "Srinivas", "age": 19}
#
#
# 🔹 Rules and Characteristics
#
# Fast lookups using keys.
#
# Keys must be hashable; values can be any type.
#
# Supports nesting: {"person": {"name": "Srinivas"}}
#
# Common Methods: get(), keys(), values(), items(), pop(), update()
#
#
# ✅ Use When
#
# You need to map unique keys to values (like a database row).
#
# Fast lookups and updates are needed.
#
# You want structured or nested data (like JSON).



# 🔁 Quick Comparison Table
#
# Feature	List	Tuple	Set	Dictionary
#
# Ordered	✅	✅	❌	✅ (Py 3.7+)
# Mutable	✅	❌	✅	✅
# Indexable	✅	✅	❌	✅ (by keys)
# Duplicates	✅	✅	❌	Keys ❌, Values ✅
# Syntax	[]	()	{}	{key: value}
# Use Case	General	Fixed data	Unique data	Key-Value Mapping




#
# 📌 Final Summary:
#
# Use a list when you need an ordered, modifiable collection.
#
# Use a tuple when you need a read-only and ordered collection.
#
# Use a set when you want unique items and need set operations.
#
# Use a dictionary when you want to associate keys with values.
