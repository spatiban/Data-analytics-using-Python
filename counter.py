# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 12:23:33 2017

@author: Sunny
"""
#Homework 1 - Word Counter
#Function Definition
def run(path):
    File= open(path,'r') #To open a file and read
    array=[] #Defining an array
    dictionary={} #Defining a dictionary

    for line in File:
        freq=line.lower().strip().split(' ') 
        
        for word in freq:
            array.append(word)
    dictionary = {a:array.count(a) for a in array} #Allotting in the dictionary from the array
    return max(dictionary, key= dictionary.get) #Sorting and returning from the dictionary

print(run('textfile_1')) # Since file exists in the same folder, it reads otherwise use different syntax

#For textfile, use print(run(txtfile.txt))