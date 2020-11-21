# -*- coding: utf-8 -*-
# s = str(input('Gimme the string bitch: '))
# slist = list(s.lower())
# news = []
# def solution(a):
#     for i in range(len(a)):
#         if i==0 or i == len(a)-1:
#             news.append(a[i])
#         elif (a[i]!=a[i-1] or a[i]!=a[i+1]):
#             news.append(a[i])
#     return print(''.join(news))

# print(solution(slist))        
    
# a = list(str(input('Gimme the string bitch: ')).lower())
# n = int(input('n= '))
# count = 0
# s = []

# for i in range(len(a)):
#     if len(s)==0:
#         s.append(a[i])
#     else:
#         if (a[i]==s[-1] and count!=n-1):
#             count+=1
#             s.append(a[i])
#         elif (a[i]!=s[-1]):
#             s.append(a[i])
#             count=0
# print(''.join(s))
            

# arr= [-4,3,-9,0,4,1]
# n=len(arr)
# p,ng,z=0,0,0
# for i in arr:
#     if i>0:
#         p+=1
#     elif i==0:
#         z+=1
#     else:
#         ng+=1
# print('{:.6f}\n{:.6f}\n{:.6f}'.format(p/n,ng/n,z/n))
# n=6
# for i in range(n):
#     print((n-i-1)*' '+(i+1)*'#')

# arr=[1,2,3,4,5]
# def miniMaxSum(arr):
#     arr.sort()
#     maxsum,minsum=0,0
#     for i in range(1,len(arr)):
#         maxsum+=arr[i]
#     for i in range(0,len(arr)-1):
#         minsum+=arr[i]
#     print(minsum,maxsum)

# miniMaxSum(arr)
b=[3,2,3,1]
a=max(b)
print(b.count(a))
    



















