"""
The script visits the profile of a given twitter user, scrolls down the screen twice to load more tweets,
and then write the text and number of likes for each tweet to a file.
"""


from selenium import webdriver
import time


url='https://twitter.com/cristiano'

#open the browser and visit the url
#-----------------------------------------
#Windows
#driver = webdriver.Chrome('chromedriver.exe')
#Mac
driver = webdriver.Chrome('./chromedriver')
#--------------------------------------------
driver.get(url)

#scroll down twice to load more tweets
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

#find all elements with a class that ends in 'tweet-text'
tweets=driver.find_elements_by_css_selector("[data-item-type=tweet]")


#write the tweets to a file
fw=open('tweets.txt','w',encoding='utf-8')
for tweet in tweets:
    txt,retweets,favorites,replies,date_Value='N/A','N/A','N/A','N/A','N/A'
    
    try: txt=tweet.find_element_by_css_selector("[class$=tweet-text]").text
    except: print ('no text')     

    try:
        retweetElement=tweet.find_element_by_css_selector("[class$=js-actionRetweet]")
        retweets=retweetElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text                                      
    except:
        print ('no retweets')
    try:
        favoritesElement=tweet.find_element_by_css_selector("[class$=js-actionFavorite]")
        favorites=favoritesElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text
    except:
        print ('no favorites')
    try:
        repliesElement=tweet.find_element_by_css_selector("[class$=js-actionReply]")
        replies=repliesElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text
    except:
        print('no replies')
    try:
        date_Element=tweet.find_element_by_css_selector("[class$=time]")
        date_Value=date_Element.find_element_by_css_selector('[data-long-form="true"]').text
    except:
        print('no date')
       
    fw.write(txt.replace('\n',' ')+'\t'+str(retweets)+'\t'+str(favorites)+'\t'+str(replies)+'\t'+str(date_Value)+'\n'+'\n'+'\n')


fw.close()


driver.quit()#close the browser
