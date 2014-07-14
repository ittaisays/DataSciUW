import sys

def getSentiment(tweetText,sentDict):
    textList=tweetText.split()
    value=0    
    for item in textList:
       if item in sentDict:
           value=value+sentDict[item]
    return value
    
def makeSentiment(tweetText,sentDict,newDict,value):
    textList=tweetText.split()
    for item in textList:
       if item not in sentDict:
           if item in newDict:
               newDict['item']=newDict['item'].append(value)
           else:
               newDict['item']=[value]
           
    return value

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
