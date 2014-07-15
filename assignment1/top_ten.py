# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 13:37:51 2014

@author: Ittai
"""
import sys
import json
import operator

def addCount(tweetText,countDict):
    hashtag=tweetText.lower()
    if hashtag in countDict:
	countDict[hashtag]=countDict[hashtag]+1
    else:
	countDict[hashtag]=float(1)

def tallyTags(listOfTweets,countDict):
	for i in range(len(listOfTweets)):
		if listOfTweets[i].get('entities',0)!=0:		
			if listOfTweets[i]['entities']['hashtags']!=[]:
			    for j in range(len(listOfTweets[i]['entities']['hashtags'])):
			        addCount(listOfTweets[i]['entities']['hashtags'][j]['text'],countDict)
									
									

def main():
	tweet_file = open(sys.argv[1])
	allTweets=[]
	for line in tweet_file:
		allTweets.append(json.loads(line))
	countDict={}
	tallyTags(allTweets,countDict)
#    englishTweets=[]
#    for i in range(len(allTweets)):
#        if allTweets[i].get('lang','no')=='en':
#            englishTweets.append(allTweets[i])
	sortedDict=sorted(countDict.iteritems(), key=operator.itemgetter(1),reverse=True)
	for i in range(10):
		print sortedDict[i][0],sortedDict[i][1]
    

if __name__ == '__main__':
    main()
