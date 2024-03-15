
#1
x=int(input("Enter number"))
y=int(input("Enter number"))
print("Sum is ",x+y)

#2
if x>y:
    print("Max is ",x)
else:
    print("Max is ",y)

#3
fact=1
num=int(input("Enter number"))
for i in range(1,num+1):
    fact*=i
print(fact)

#4
r=int(input("enter interest rate"))
p=int(input("enter amount"))
t=int(input("enter time"))
print((p*r*t)//100)

#5
r=int(input("enter interest rate"))
p=int(input("enter amount"))
t=int(input("enter time"))
a=p*(1+(r/100))**t
ptint(a)

#6
num=input("enter number")
sum=0
l=len(num)
for i in num:
    i=int(i)
    sum+=i**l
if sum==int(num):
    print("Armstrong")
else:
    print("Not armstrong")

#7
import math
r=int(input("Enter radius"))
print("Area is ",math.pi*(r**2))
#8
def prime(n):
    count=0
    for i in range(2,n):
        if n%i==0:
            count+=1
    if count==0:
        print(n)
a=int(input("Enter upper bound"))
b=int(input("Enter upper bound"))
for i in range(a,b+1):
    prime(i)
    
#9
num=int(input("Enter number"))
count=0
for i in range(2,num):
    if num%i==0:
        count+=1
if count!=0:
    print("Not a prime number")
else:
    print("Prime number")

#10 
def fib(n):
    fib=[0,1]
    for i in range(n):
        fib+=[fib[-1]+fib[-2]]
        print(fib[i],end=',')
fib(int(input("Enter number")))





