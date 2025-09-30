# def re(a,b):
#     if a<b:
#         print(a)
#         return re(a+1,b)
# re(1,6)
#factorial
# def fact(num):
#     if num==0:
#         exit()
#     if num ==1:
#         return 1
#     else:
#         return num*fact(num-1)
# print(fact(0))

#palindrome
def pal(text):
    if len(text)<=1:
        print("palindrome")
    else:
        if text[0] == text[-1]:
            pal(text[1:-1])
        else:
            print("not palindrome")
#fibonacci
def fib(num):
    if num==0 or num==1:
        return 1
    else:
        return fib(num-1) + fib(num-2)
print(fib(3))
#leetcode
class Solution(object):
    def fib(self, num):
        a, b = 0, 1
        if num == 0:
            return num
        if num == 1:
            return num
        for _ in range(0, num - 1):
            a, b = b, b + a
        return (b)
