# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 15:24:20 2022

@author: Ahaan Banerjee
"""

n=int(input())
for i in range(n):
    l=int(input())
    s=input()
    dist=[]
    for a in s:
        if a not in dist:
            dist.append(a)
    num= (len(dist)*2 +(len(s)-(len(dist))))
    print(num)
    