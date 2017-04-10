# -*- coding: utf-8 -*-
"""
To improve on the 85% accuracy for classification using sklearn using RandomForestClassifier
Created on Mon Mar  6 18:24:20 2017

@author: Sunny
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


#read the reviews and their polarities from a given file
def loadData(fname):
    reviews=[]
    labels=[]
    f=open(fname)
    for line in f:
        review,rating=line.strip().split('\t')  
        reviews.append(review.lower())    
        labels.append(int(rating))
    f.close()
    return reviews,labels

rev_train,labels_train=loadData('reviews_train.txt')
rev_test,labels_test=loadData('reviews_test.txt')


#Build a counter based on the training dataset
counter = CountVectorizer()
counter.fit(rev_train)


#count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data

#train classifier

clf=RandomForestClassifier(n_estimators=1900,criterion="entropy",random_state=150,min_samples_split=160,max_features='log2')

#train all classifier on the same datasets
clf.fit(counts_train,labels_train)

#use hard voting to predict (majority voting)
pred=clf.predict(counts_test)

#print accuracy
print (accuracy_score(pred,labels_test))
