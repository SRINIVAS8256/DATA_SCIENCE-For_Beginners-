#THERE ARE VARIOUS TYPES OF LITERALS THEY ARE
# 1) NUMERIC LITERAL
from typing import LiteralString
#
# 2) STRING Literal
# 3) BOOLEAN LITERAL
# 4) SPECIAL LITERAL


#1)NUMERIC LITERAL



a=0b1010#binary literal
b=100  #decimal literal
c=0o310 #octal literal
d=0x12c #hexadecimal mliteral


#FLOAT LITERAL

print(int(5e2))
float_1=10.5
float_2=1.5e2
float_3=1.5e-3

# complex literal
x=3.14j
print(a,b,c,d)
print(float_1,float_2,float_3)
print(x,x.imag,x.real)



# 2) STRING LITERALS

string="this is python"
strings="this is python"
char="c"
multiline_str="""this is a multiline string with more than one line code"""""
unicode=u"\U0001f600\U0001F606\U0001F923"
raw_str=r"raw \n string"
print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)


# 3) BOOLEAN LITERAL
a=True+4
b=False+4
print("a:",a)
print("b:",b)


# 4) SPECIAL LITERAL
a=None#uses to declare variables
print(a)
