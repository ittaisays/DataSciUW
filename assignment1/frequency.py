# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 12:20:45 2014

@author: Ittai
"""

import sys
import json

def addCount(tweetText,countDict):
    textList=tweetText.lower().split()
    for item in textList:
       if item in countDict:
           countDict[item]=countDict[item]+1
       else:
		countDict[item]=float(1)
										
    
def getTotalCount(someDict):
	value=0	
	for term in someDict.keys():
		value=value+someDict[term]
	return value

def convertToTF(dictionary):
	total=getTotalCount(dictionary)	
	for term in dictionary.keys():
		dictionary[term]=dictionary[term]/total
	


def main():
    tweet_file = open(sys.argv[1])
    allTweets=[]
    for line in tweet_file:
        allTweets.append(json.loads(line))
    newDict={}
    for tweet in allTweets:
        addCount(tweet.get('text',"0"),newDict)
    convertToTF(newDict)
			
#    englishTweets=[]
#    for i in range(len(allTweets)):
#        if allTweets[i].get('lang','no')=='en':
#            englishTweets.append(allTweets[i])
    for key in newDict.keys():
        print key, newDict[key]
								
    


if __name__ == '__main__':
    main()
