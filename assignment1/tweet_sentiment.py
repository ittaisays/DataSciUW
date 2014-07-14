import sys
import json

def getSentiment(tweetText,sentDict):
    textList=tweetText.lower().split()
    value=0    
    for item in textList:
       if item in sentDict:
           value=value+sentDict[item]
    return value
        

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores={}
    for line in sent_file:
        term,score=line.split("\t")
        scores[term]=int(score)
    allTweets=[]
    for line in tweet_file:
        allTweets.append(json.loads(line))
#
    englishTweets=[]
    for i in range(len(allTweets)):
        if allTweets[i].get('lang','no')=='en':
            englishTweets.append(allTweets[i])

    for tweet in allTweets:
        print getSentiment(tweet.get('text',"0"),scores)


if __name__ == '__main__':
    main()
