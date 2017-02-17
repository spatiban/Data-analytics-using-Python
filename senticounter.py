# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:43:08 2017

@author: Sunny
"""

#function that loads a lexicon of positive words to a set and returns the set
def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex
    
def run(path):

    poswords={} #Dictionary to return the count
    posLex=loadLexicon('positive-words.txt') #load the positive lexicons
    fin=open(path)

    for line in fin: # for every line in the file (1 review per line)
        R_line=line.lower().strip().split(' ')
        Review_Set=set() #Adding all the words in the review to a set
        
        for word in R_line: #Check if the word is present in the line
            Review_Set.add(word)  #As it is a set, only adds one time
            
        for word in Review_Set:
            if word in posLex:
                if word in poswords:
                    poswords[word]=poswords[word]+1
                else:
                    poswords[word] = 1
                    
    fin.close()
    return poswords

if __name__ == "__main__": 
    print(run('textfile_2'))