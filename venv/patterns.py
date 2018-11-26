from math import *
print("enter the height")
n=int(input())

print("Right angled triangle")
for j in range (1,n):
    for i in range(0,j):
        print("*",end=" ")
        i+=1
    print()
    j+=1

print ("Diamond")

a=0
b=2*n-3
l=0
x,y=0,0
for y in range(0,n):
    for x in range(0,2*n):
        if x==ceil((a + b) / 2) + y or x == ceil((a + b) / 2) - y or x in range(ceil((a+b)/2)-y,ceil((a+b)/2)+y):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print()
    x+=1
y+=1
for y in range(n-2,-1,-1):
    for x in range(0,2*n):
        if x==ceil((a + b) / 2) + y or x == ceil((a + b) / 2) - y or x in range(ceil((a+b)/2)-y,ceil((a+b)/2)+y):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print()
    x+=1
l=0
print("numbered triangle")
for y in range(0,n):
    for x in range(0,2*n):
        if x==ceil((a + b) / 2) + y or x == ceil((a + b) / 2) - y or x in range(ceil((a+b)/2)-y,ceil((a+b)/2)+y):
            print(l,end=" ")
            l+=1
        else:
            print(" ",end=" ")
    print()
    x+=1


k=0
print("right angled triangle with numbers")

for j in range(1,n):
    for i in range(0,j,1):
        print(k, end=" ")
        k += 1
    print()
    j += 1

print("hollow triangle")
k=0
for y in range(0,n-1):
    for x in range(0,2*n):
        if (x==ceil((a + b) / 2) + y or x == ceil((a + b) / 2) - y):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    x+=1
y+=1
for k in range(0,2*n):
    if k==ceil((a + b) / 2) + y or k in range(ceil((a + b) / 2) - y,ceil((a + b) / 2) + y):
        print("*", end=" ")
    else:
        print(" ", end=" ")
print()
print("Half diamond")
for j in range(1, n):
    for i in range(0, j):
        print("*", end=" ")
        i += 1
    print()
j += 1
for j in range(n, -1, -1):
    for i in range(0, j):
        print("*", end=" ")
        i += 1
    print()
pass
k=1
print("SORTING AND BINARY SEARCH")
print("enter n")
lst=[]
n=int(input())
tmp=0
for i in range(0,n,1):
    k=int(input())
    lst.append(k)
for x in range(0,len(lst),1):
    for y in range(x+1,len(lst),1):
        if lst[x]>lst[y]:
            tmp=lst[x]
            lst[x]=lst[y]
            lst[y]=tmp

print(lst)

print("enter the search number")
se=int(input())
pos=0
l=0
u=len(lst)-1
m=floor((l+u)/2)

for i in range(l,m+1,1):
    if se>lst[m]:
        l=m
        m = floor((m + u) / 2)
        print(m)
    if se<lst[m]:
        m = floor((l + m) / 2)
    if se==lst[u]:
        m=u
        print(m)


if(se==lst[m]):
    print("number found at position {}".format(m))



