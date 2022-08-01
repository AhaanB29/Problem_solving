# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 15:34:49 2022

@author: Ahaan Banerjee
"""

n=int(input())
for i in range (n):
    rings=int(input())
    L=input().split(" ")
    num=[]
    for a in L:
        num.append(int(a))
    for i in range(len(num)):
        func=input().split(' ')
        string=func[1]
        for j in string:
            if j=='D':
                if num[i]==9:
                    num[i]=0
                else:
                    num[i]+=1
            else:
                if num[i]==0:
                    num[i]=9
                else:
                    num[i]-=1
    for k in num:
        print(k,end=' ')
    print("\n")