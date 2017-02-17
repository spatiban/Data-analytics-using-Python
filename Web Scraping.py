# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 19:04:15 2017

@author: Saketh Patibandla
"""
from bs4 import BeautifulSoup
import re
import time
import requests

def getCritic(review):
    
    critic='No Name'# initialize critic 
    criticChunk=review.find('a',{'href':re.compile('/critic/')})
    if criticChunk: critic=criticChunk.text#.encode('ascii','ignore')
    return critic
    
def getRating(review):
            
            rating='No rating' #intialize rating
            rotten = review.find('div',{'class':re.compile('rotten')})
            fresh = review.find('div',{'class':re.compile('fresh')})               
            
            if rotten: rating = 'Rotten'
            elif fresh: rating = 'Fresh'
            else: rating = 'No rating'
            
            return rating

def getSource(review):

    source='No Source'
    SourceChunk=review.find('em',{'class':'subtle'})    
    if SourceChunk: source=SourceChunk.text
    return source
     
     
def getDate(review):

    date='No Date'# initialize critic 
    DateChunk=review.find('div',{'class':'review_date'})
    if DateChunk: date=DateChunk.text#.encode('ascii','ignore')
    return date    

def getTextLen(review):
    
     text='No text'     
     textChunk=review.find('div',{'class':'the_review'})
     if textChunk: text=textChunk.text#.encode('ascii','ignore') 
     return len(text)
     
def run(url):

    pageNum=2 # number of pages to collect
	
    for p in range(1,pageNum+1): # for each page 
        print('\n')
        print ('page',p)
        print('\n')
        html=None

        if p==1: pageLink=url # url for page 1
        else: pageLink=url+'?page='+str(p)+'&sort=' # make the page url
		
        for i in range(5): # try 5 times
            try:
                #use the browser to access the url
                response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content # get the html
                break # we got the file, break the loop
            except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
                print ('failed attempt',i)
                time.sleep(2) # wait 2 secs
				
		
        if not html:continue # couldnt get the page, ignore
        
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') # parse the html 

        reviews=soup.findAll('div', {'class':re.compile('review_table_row')}) # get all the review divs (here soup gets up all the divs that have review_table_row as the class attribute)

        for review in reviews:
            print('\n')
            print(getCritic(review))
            print(getRating(review))
            print(getDate(review))
            print(getSource(review))
            print('the length of the text is ',getTextLen(review),' characters')
            
           
		
        time.sleep(2)	# wait 2 secs 


if __name__=='__main__':
    url='https://www.rottentomatoes.com/m/space_jam/reviews/'
    run(url)