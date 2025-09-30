a=5
print("hi")
input("enter a=")
type(5)
int('5')#type conversion float str list tuple
abs(-4)# gives modulus value
pow(2,3) # 2 power 3
min(1,23,4)#gives minimum value
min(1,23,4)#gives maximum value
print(round(22/7))

divmod(5,2)# gives in tuple 1.x//y=integer division 2. x%y =remainder


#imp
# bin/oct/hex
print(bin(2))
print(hex(2))
print(oct(2))

#id gives memory address of variable
print(id(5))
print(id(a))


print(a)
print(ord('A'))
print(chr(65))
print(int("1000001",2))
print(int("1B",16))


#ord gives unicode of character
print(ord('A'))

#length
print(len([1,2,3,3]))

#sum gives sum of python datastructures note :ONLY WORKS WITH NUMERIC VALUES INSIDE THE ITERABLE
print(sum([1,2,4]))
print(sum({1,2,4}))
print(sum((1,2,4)))
#SUM OF DICTIONARY VALUES
data={'a':4,'b':37}
print(sum(data.values()))

#help gives data of inbuilt functions
help('print')
