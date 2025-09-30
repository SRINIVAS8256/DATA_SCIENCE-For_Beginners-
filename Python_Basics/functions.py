# # # # def iseven(num):
# # # #     return num%2 ==0
# # # #
# # # # def search(target,arr):
# # # #     for i in range(0,len(arr),1):
# # # #         if arr[i]==target:
# # # #             return "at index",i
# # # #     return "not found"
# # # # print(search(273567,[1,2,3,4,5,6,77,2,7]))
# # #
# # # l=[1,2,3,4,5]
# # # for i in range(0,len(l)//2):
# # #     other=len(l)-1-i
# # #     temp=l[i]
# # #     l[i]=l[other]
# # #     l[other]=temp
# # # print(l)
# # # i=2
# # arr=[1,2,3,4,4]
# # def dup(arr):
# #     return len(arr) == len(set(arr))  # True if no duplicates, False otherwise
# # print(dup(arr))
# # print(2000%10)
# # print((4+5)*5**(4-2))
# # print()
# def digitsSum(N):
#     ##Your code here
#     ans=0
#     while(N>0):
#         rem=N%10
#         ans=ans+rem
#         N=N//10
#     return ans
# print(digitsSum(56))
# m=10
# print(3*m)
# def main():
#     print("function")
#     str = "dogesgdogedoge"
#     print(doge_count(str))
#     my()
#
# def doge_count(str):
#     return str.count("doge")
# def my():
#     print("hello")
# main()
#
# a=10
# if (a==10 and a<11):
#     print(a)
#
#
#
# a=int(input("value of a = ?"))
# if(a>=90):
#     print("a")
# elif(a>=80):
#     print("b")
# else:
#     print("c")
#
# s={21,34,1}
# list_s=list(s)
# print(list_s[2])
# i={13,12,43,5,7,56,7,68789}
# print(sorted(i))

# x = frozenset({"apple", "banana", "cherry"})
# a=list(x)
# print(a[2])
# def main():
#     even()
#
# def even():
#     for i in range(100):
#         print(i)
#         i = i + 1
#
#
# # main()
# def even():
#     for i in range(2, 100, 3):  # Step by 2
#         print(i)
# even()
def even():
    i = 2
    if i%2 == 0:
        return "even"
    else:
        return "odd"

print(even())



def duplicate(l1):
    l2=[]
    for i in l1:
        if i not in l2:
            l2.append(i)
    print(l2)
duplicate([1,2,3,3,3,3,1,1])


#IIIIMMMPPPP 💯💯


#def (a,b)here a and b are parameters💯

#💯 (1,2) are arguments

#1.DEFAULT ARGUMENT
#2.POSITIONAL ARGUMENT
#3.KEYWORD ARGUMENT
#4.ARBITARY ARGUMENT


#Default argument
def power(a=1,b=1):
    return a**b
print(power(2,3))#8

#2.POSITIONAL ARGUMENT
#arguments will assign parallally with respect to parameters
#or
#we can use positional arguments

print(power(b=2,a=3))#9
z=2
c=3
print(power(z,c))#8

print(power(z=2,c=3))# power() got an unexpected keyword argument 'z'

#3.Keyword argument
#priority is greater than positional

#4.ARBITARY ARGUMENT
