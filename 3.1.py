#600851475143
import math
sqrt=math.sqrt#开根，运算量减小一个数量级

def func(x):
    m=int(sqrt(x)+1)
    for i in range(2,m):
        if x%i==0:
            return 0
    return 1 #省略了else


num=600851475143
n=sqrt(num)+1#一个数的因数在1到它的平方根之间
n=int(n)
result=0
for i in range(2,n):#while
    if num%i==0:
        if func(i):
            result=i
print(result)