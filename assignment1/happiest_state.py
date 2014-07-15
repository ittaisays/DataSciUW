# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 15:28:40 2014

@author: Ittai
"""
import sys
import json
import operator

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


def getSentiment(tweetText,sentDict):
    textList=tweetText.lower().split()
    value=0    
    for item in textList:
       if item in sentDict:
           value=value+sentDict[item]
    return value
  
def makeSentDict(scores,sentFile):
    for line in sentFile:
        term,score=line.split("\t")
        scores[term]=int(score)           

def averageSentiments(dictionary):
	for item in dictionary.keys():
		dictionary[item]=average(dictionary[item])

def average(listName):
	value=0
	for i in range(len(listName)):
		value=value+listName[i]
	return (value/len(listName))

		
def tweetToStateSentiment(tweetText,state,sentDict,newDict):
	value=getSentiment(tweetText,sentDict)
	stateShort=state[-2:]	
	if stateShort in states:	
		if stateShort in newDict:
			newDict[stateShort].append(value)
		else:
			newDict[stateShort]=[value]

def processTweetList(allTweets2,scores,stateDict):
	for i in range(len(allTweets2)):
		if allTweets2[i].get('coordinates',0)!=0:
			if allTweets2[i]['coordinates']!=None:
				tweetToStateSentiment(allTweets2[i].get('text',"0"),allTweets2[i]['user']['location'],scores,stateDict)


def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	scores={}
	makeSentDict(scores,sent_file)	
	allTweets=[]
	for line in tweet_file:
		allTweets.append(json.loads(line))
	englishTweets=[]
	for i in range(len(allTweets)):
		if allTweets[i].get('place',0)!=0:
			if allTweets[i]['place']!=None:
				if allTweets[i]['place'].get('country_code','no')=='US':
					englishTweets.append(allTweets[i])
	stateDict={}
	processTweetList(englishTweets,scores,stateDict)
	averageSentiments(stateDict)
	sortedDict=sorted(stateDict.iteritems(), key=operator.itemgetter(1),reverse=True)
	print sortedDict[0][0]





if __name__ == '__main__':
    main()
				
				

			