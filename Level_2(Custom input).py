#1
print("\nPython program to flatten tuple of list to tuple.")
tup=([5,8,10],[1,2],[99,98,97])
print("Input is:",tup)
tupnew=()
for i in tup:
    for j in i:
        tupnew+=(j,)
print("Output is",tupnew)

#2
print("\nConvert set into tuple and tuple into set.")
s={10,67,97,101}
print("Set is ",s)
tup=tuple(s)
print("Tupple is ",tup)
snew=set(tup)
print("Set is ",snew)

#3
print("\nCovert list of dictionary to tuple list.")
l=[{'ayu':10,'ash':11},{'dev':1},{'kiara':99,'meena':100,'raj':101}]
print("Input list is",l)
tup=()
for dictionary in l:
    lnew=[]
    for i in dictionary:
        lnew+=[i,dictionary[i]]
    tup+=(lnew,)
print("Output is",tup)


#4
print("\nSort tuple list by nth element of tuple.")
l=[(1,2,3),(98,101,95),(10,22,345),(0,3,4)]
print("Original list is:",l)
index=int(input("Enter place using which it should be sorted:"))
for i in range(len(l)-1):
    for j in range(len(l)-i-1):
        if l[j][index-1]<l[j+1][index-1]:
            l[j],l[j+1]=l[j+1],l[j]
print("Sorted list is:",l)

#5
print("\nFind tuple indices from other tuple list.")
tl=[(1,2),(9,10),(8,16),(4,8)]
sl=[(1,2),(8,16),(8,64)]
print("Test list is:",tl)
print("Search list is:",sl)
l=[]
dic={}
for i in sl:
    if i in tl:
        dic[i]=tl.index(i)
        l+=[tl.index(i)]
print("The indices in test_list are:",l,"\n")
print("The dictionary as {tuple(in search_list) : index(in test_list)} is :",dic)

#6
print("\nConvert dictionary value list to dictionary list.")
dic={'ayu':[1,2,3],'ash':[9,8],'abhi':[1]}
print("Input dictionary is:",dic)
n=0
dicnew =[{} for n in range(len(dic))]
for i in dic:
    for key,value in dic.items():
        for val in value:
            dicnew[n][key]=val
            n+=1
        n=0
print("Modified dictionary is:",dicnew)
