#1.Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
print("\nPython program to calculate the product, multiplying all the numbers in a given tuple.")
tup=(4, 3, 2, 2, -1, 18)
print("Input is:",tup)
product=1
for i in tup:
    product*=i
print("Product is:",product)

#2.Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
print("\nPython program to calculate the average value of the numbers in a given tuple of tuples.")
maint=((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
print("Input is:",maint)
l=[]
x=len(maint[0])
for j in range(x):
    sum=0
    for k in range(len(maint)):
        sum+=maint[k][j]
    avg=sum/len(maint)
    l+=[avg]
print("The average is",tuple(l))
    
