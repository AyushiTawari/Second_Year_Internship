"""
1)Python pgm to flatten tuple of list to tuple
2)Convert set into tuple and tuple into set.
3)Covert list of dictionary to tuple list.
4)Sort tuple list by nth element of tuple.
5)Find tuple indices from other tuple list.
6)Convert dictionary value list to dictionary list. 
"""
#1
print("Python program to flatten tuple of list to tuple")
tup=()
l=[]
while True:
    print("Add new list")
    while True:
        l+=[int(input("Enter "))]
        ch=input("Enter exit to stop this list")
        if ch.lower()=="exit":
            print(l)
            tup+=(l,)
            break
    l=[]
    ch=input("Enter exit to stop complete input")
    if ch.lower()=="exit":
        break
print("Input tuple is",tup)
tupnew=()
for i in tup:
    for j in i:
        tupnew+=(j,)
print("Output is",tupnew)

#2
print("Convert set into tuple and tuple into set.")
s=set()
tup=tuple()
while True:
    s.add(input("Enter element"))
    ch=input("Enter choice,exit to stop entering")
    if ch=="exit":
        break
print("Set is ",s)
tup=tuple(s)
print("Tupple is ",tup)
snew=set(tup)
print("Set is ",snew)

#3
print("Covert list of dictionary to tuple list.")
l=[]
dict={}
while True:
    print("Add new dictionary")
    while True:
        key=input("Enter key")
        value=input("Enter value")
        dict[key]=value
        ch=input("Enter exit to stop this dictionary")
        if ch.lower()=="exit":
            print(dict)
            l+=[dict]
            break
    dict={}
    ch=input("Enter exit to stop complete input")
    if ch.lower()=="exit":
        break
print("Input list is",l)
tup=()
for dictionary in l:
    lnew=[]
    for i in dictionary:
        lnew+=[i,dictionary[i]]
    tup+=(lnew,)
print("Output is",tup)


#4
print("Sort tuple list by nth element of tuple.")
l=[]
tup=()
x=int(input("No of elements in each tuple:"))
while True:
    for i in range(x):
        value=int(input("Enter value:"))
        tup+=(value,)
    print(tup)
    l.append(tuple(tup))
    tup=()
    ch=input("Enter exit to stop input:")
    if ch.lower()=="exit":
        break
print("Original list is:",l)
index=int(input("Enter place using which it should be sorted:"))
for i in range(len(l)-1):
    for j in range(len(l)-i-1):
        if l[j][index-1]<l[j+1][index-1]:
            l[j],l[j+1]=l[j+1],l[j]
print("Sorted list is:",l)

#5
print("Find tuple indices from other tuple list.")
def test():
    tup=()
    tl=[]
    print("Test_list")
    ch=int(input("Enter number of tuples to add"))
    for i in range(ch):
        while True:
            tup+=(int(input("Enter number:")),)
            ch=input("Enter exit to stop input in this tupple:")
            if ch.lower()=="exit":
                tl.append(tup)
                print(tup)
                break
        tup=()
    print("Test_list is",tl,"\n")
    return(tl)
def search():
    tup=()
    sl=[]
    print("Search_list")
    ch=int(input("Enter number of tuples to add"))
    for i in range(ch):
        while True:
            tup+=(int(input("Enter number:")),)
            ch=input("Enter exit to stop input in this tupple:")
            if ch.lower()=="exit":
                sl.append(tup)
                print(tup)
                break
        tup=()
    print("Test_list is",sl,"\n")
    return(sl)
tl=test()
sl=search()
l=[]
dic={}
for i in sl:
    if i in tl:
        dic[i]=tl.index(i)
        l+=[tl.index(i)]
print("The indices in test_list are:",l,"\n")
print("The dictionary as {tuple(in search_list) : index(in test_list)} is :",dic)

#6
print("Convert dictionary value list to dictionary list.")
dic={}
num=int(input("Enter no of elements in dictionary:"))
for i in range(num):
    l=[]
    key=input("\nEnter key")
    n=int(input("Enter number of elements in this list"))
    for j in range(n):
        x=int(input("Enter value:"))
        l+=[x]
    dic[key]=l
print("Original dictionary is:",dic)
dicnew={}
n=0
dicnew =[{} for n in range(len(dic))]
for i in dic:
    for key,value in dic.items():
        for val in value:
            dicnew[n][key]=val
            n+=1
        n=0
print("Modified dictionary is:",dicnew)
    
    
        
