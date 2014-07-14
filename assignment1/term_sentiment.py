import sys
import json

def getSentiment(tweetText,sentDict):
    textList=tweetText.lower().split()
    value=0    
    for item in textList:
       if item in sentDict:
           value=value+sentDict[item]
    return value
    
def makeSentiment(tweetText,sentDict,newDict):
    value=getSentiment(tweetText,sentDict)
    textList=tweetText.lower().split()
    for item in textList:
       if item not in sentDict:
           if item in newDict:
               newDict[item].append(value)
           else:
               newDict[item]=[value]


def average(listName):
	value=0
	for i in range(len(listName)):
		value=value+listName[i]
	return (value/len(listName))

def averageSentiments(dictionary):
	for item in dictionary.keys():
		dictionary[item]=average(dictionary[item])

def makeSentDict(scores,sentFile):
    for line in sentFile:
        term,score=line.split("\t")
        scores[term]=int(score)           

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores={}
    makeSentDict(scores,sent_file)
    allTweets=[]
    for line in tweet_file:
        allTweets.append(json.loads(line))
    newDict={}
    for tweet in allTweets:
        makeSentiment(tweet.get('text',"0"),scores,newDict)
#    englishTweets=[]
#    for i in range(len(allTweets)):
#        if allTweets[i].get('lang','no')=='en':
#            englishTweets.append(allTweets[i])
    averageSentiments(newDict)
    for key in newDict.keys():
        print key, newDict[key]
								
    


if __name__ == '__main__':
    main()
