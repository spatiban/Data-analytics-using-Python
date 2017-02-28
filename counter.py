# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 12:23:33 2017

@author: Sunny
"""
#Homework 1 - Word Counter
#Function Definition
def run(path):
    File= open(path,'r') #To open a file and read
    a=[] #Defining a list
    d={} #Defining a dictionary

    for line in File:
        words=line.lower().strip().split(' ') 
        
        for word in words:
            a.append(word)
    d = {x:a.count(x) for x in a} #Allotting in the dictionary from the array
    return max(d, key= d.get) #Sorting and returning from the dictionary
    File.close()
print(run('textfile')) # Since file exists in the same folder, it reads otherwise use different syntax

#For textfile, use print(run(txtfile.txt))