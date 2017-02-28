# -*- coding: utf-8 -*-
"""
1) Reports all the sequences of words that follow, 'not' <any word> <Positive/Negative word> <Noun> format.
2) Takes any dictionary with alphabets as keys and integers as values and prints the alphabets with the 3 highest integer references.
3) Reports the three words from the text that occur the most number of times using frequency as key.

Created on Mon Feb 27 19:04:02 2017

@author: Sunny
"""

import nltk
from nltk.util import ngrams
import re
from nltk.tokenize import sent_tokenize
from nltk import load
from operator import itemgetter
    
def processSentence(sentences,posLex,negLex,tagger):
    
    result=[]
    pos_neg = posLex | negLex
    for sentence in sentences:
       sentence=re.sub('[^a-zA-Z\d]',' ',sentence)#replace chars that are not letters or numbers with a spac
       sentence=re.sub(' +',' ',sentence).strip()#remove duplicate spaces
       
       #tokenize the sentenence
       terms = nltk.word_tokenize(sentence.lower())   
       POStags=['NN'] # POS tags of interest 		
       POSterms=getPOSterms(terms,POStags,tagger)
       nouns=POSterms['NN']
       #anyword=text
       result+=four_grams(pos_neg,terms, nouns)
     
    return result 

def four_grams(posneg,terms, nouns):
    result=[]
    fourgrams = ngrams(terms,4) #compute 2-grams
    for pn in fourgrams:
        if pn[0]=='not'  and pn[2] in posneg and pn[3] in nouns:             
            result.append(pn)   
    return result

# return all the terms that belong to a specific POS type
def getPOSterms(terms,POStags,tagger):
	
    tagged_terms=tagger.tag(terms)#do POS tagging on the tokenized sentence

    #Using dictionary for JJ and RB where each value is a set
    POSterms={}
    for tag in POStags:POSterms[tag]=set()

    #for each tagged term
    for pair in tagged_terms:
        for tag in POStags: # for each POS tag 
            if pair[1].startswith(tag): POSterms[tag].add(pair[0])#Pair[1] is the tag

    return POSterms
    
def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex
    
def run(file_path):
    
    #To create a tagger
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)
    
    #Reading the input
    f=open(file_path)
    text=f.read().strip()  
    f.close()    
    #To tokenize sentences
    sentences=sent_tokenize(text)
    print ('Number OF sentences: ',len(sentences))
    
    #To load all the positive and negative words
    posLex=loadLexicon('positive-words.txt')
    negLex=loadLexicon('negative-words.txt')
    
    four_word=processSentence(sentences,posLex,negLex,tagger)
    return four_word
    
    
def getTop3(D):
    top3 = []
    
    sortedByValue = sorted(D.items(),key=itemgetter(1),reverse=True)
    top3Dict = sortedByValue[0:3]
    
    for key,value in top3Dict:
        top3.append(key)
        
    return top3
    
#To store the words with frequency into a dictionary and return the top 3 words
def count(path):
    File= open(path,'r') #To open a file and read
    l1=[] #Defining a list
    d1={} #Defining a dictionary

    for line in File:
        words=line.lower().strip().split(' ') 
        
        for word in words:
            l1.append(word)
    d1 = {a:l1.count(a) for a in l1} #Allotting in the dictionary from the list
    return(getTop3(d1))
    File.close()       
             
if __name__=='__main__':
	
    print (run('input.txt'))
    dic = {'a':109, 'b':845, 'c': 2329,'d':534,'e':615, 'f':840}
    diclist=getTop3(dic)
    print (diclist)
    d2=count('input.txt')
    print(d2)
