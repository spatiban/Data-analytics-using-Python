# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 19:10:50 2017

@author: Sunny
"""

"""
A script that compares the input word with a webpage and returns the number of times it occurs in the webpage
"""

import re
from nltk.corpus import stopwords
import requests
from operator import itemgetter



def run(url,abc): 

    success=False# become True when we get the file

    for i in range(5): # try 5 times
        try:
            #use the browser to access the url 
            response=requests.get(url,headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })    
            success=True # success
            break # we got the file, break the loop
        except:# browser.open() threw an exception, the attempt to get the response failed
            print ('failed attempt',i)
     
    # all five attempts failed, return  None
    if not success: return None
    
    text=response.text# read in the text from the file
    freq=0
    sentences=text.split('.') # split the text into sentences 
    abc=abc.lower() #lowercase the word
    for sentence in sentences: # for each sentence 

        sentence=sentence.lower().strip() # lower case and strip	
        sentence=re.sub('[^a-z]',' ',sentence) # replace all non-letter characters  with a space
		
        words=sentence.split(' ') # split to get the words in the sentence 
        
        for word in words: # for each word in the sentence 
           if word=='':continue # ignore empty words 
           if word==abc: # update the frequency of the word
               freq=freq+1
            
    return(freq)
            

if __name__=='__main__':
    print(run('http://tedlappas.com/wp-content/uploads/2016/09/textfile.txt','Is'))
