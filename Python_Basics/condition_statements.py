l=[1,2,3,4,5]
print(l[0:3:-1])
print(l[5])
print(l[0])
print(len(l))
for i in range(0,len(l)-1//2):
    other=len(l)-1-i
    temp=l[i]
    l[i]=l[other]
    l[other]=temp
print(l)
