#OPERATORS


# operators are used to perform operations on variables and values.python has following operators
# 1. ARITHMETIC OPERATION
# 2.COMPARISION Operator
# 3.LOGICAL Operator
# 4.BITWISE Operator
# 5.ASSIGNMENT Operator
# 6.IDENTIFY Operator
# 7.MEMBERSHIP Operator


#1) arithmetic operator
x=10
y=66
print(x+y)
print(x-y)
print(x*y)
print(x**y)
print(x/y)
print(type(x//y))#INTEGER DIVISION
print(x%y)

# 2) COMPARISION OPERATOR
print(x>=y)
print(x<=y)
print(x==y)
print(x!=y)

#3) logical operator
x=True
y=False
print(x or y)
print(x and y)
print(not x)
print(not y)

#4) bitwise operator
print(x & y)
print(x | y)
print(x >> 2)
print(x<<3)
print(~x)
print(type(~x))


#5)ASSIGNMENT Operator
a=33 #assigning
print(a)
a+=3 #a=a+3
a-=3
a*=3
a/=3



#😒😒😒😒 PYTHON WILL NOT SUPPORT(INCREMENT a++/++a and DECREMENT a--/--a) OPERATORS

#IMPORTANT
# 6)IDENTIFY Operator  checks whether the references variable have same "memory location or not"
a=3
b=3
print(a is b)
a="hello"
b="hello"
print(a is b)
a="hello-world"
b="hello-world"
print(a is b)
a=[1,2,3]
b=[1,2,3]
print(a is b)


# 7) MEMBERSHIP Operator ,to check whether the value present in that variable or not
x="mandya"
print("a" in x)

a=[1,2,3]
print(1 in a)
print(33 in a)

s=(1,2,3) #even in tuple sets and also in dictionary
print(1 in s)
print(5 in s)
print(5 not in s)
