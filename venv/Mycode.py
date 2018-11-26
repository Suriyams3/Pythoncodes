from math import *
# print("enter the range")
# x=int(input())
# print("prime numbers")
# flag =0
# for i in range(1,x):
#
#     for j in range (2,i-1):
#
#         if i%j==0:
#             flag+=1
#         j+=1
#     if flag == 0:
#         print(i)
#     flag=0
#     i+=1

#
# print ("enter the number")
# flag=0
# n=int(input())
# for k in range(2,n-1):
#     if n%k==0:
#         flag+=1
#     k+=1
# if flag==0:
#     print("the given number is prime")
# else:
#     print("the given number is composite")
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



