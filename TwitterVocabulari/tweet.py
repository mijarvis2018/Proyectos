#Code from https://github.com/BBeese/TwitterBotVocabulary
import tweepy
from tweepy import OAuthHandler

import matplotlib.pyplot as plt
import numpy as np

def StringCleaning(s):
    string = ""
    for char in s:
        if (ord(char) > 122) or ((ord(char) < 97) and (char != "'")) or ("https://" in s):
            continue
        else:
            string = string + char
    return string



def main():

    appKey = "E5SKwYA3Wv8YjGyeNPeJSGyED"
    appSecret = "D300scxAWlRYfDYcsGBCGOFlfU9sTesljsyUoFgHU5gKy6TbuR"
    authToken = "932043916009930752-PSAfM2M3A0wW2zmIy0Ypwp1tiavKwt5"
    authSecret = "FCM7374gFpZwFuNoZb9qj32m7PuWiwXsc1skfF2YgURLf"

    auth = OAuthHandler(appKey, appSecret)
    auth.set_access_token(authToken, authSecret)

    api = tweepy.API(auth)
    screen_name = "@assamblea"

    alltweets = api.user_timeline(screen_name, count = 200, include_rts = True)
    #alltweets = api.user_timeline(screen_name = "@arivera", count = 200, include_rts = False)
    outtweets = [[tweet.text] for tweet in alltweets]

    wordDict = {}
    for tweets in outtweets:
        for words in tweets:
            words = words.lower().split()
            for word in words:
                 word = StringCleaning(word)
                 if word in wordDict:
                     wordDict[word] += 1
                 else:
                     wordDict[word] = 1

    wordList = []
    count = 0
    for key in wordDict:
        if (wordDict[key] <= 7) or (key == "") or (len(key) <= 5):
            continue
        else:
            appender = [key]
            wordList.append(appender)
            wordList[count].append(wordDict[key])# Puts dictionary values into 2d List
            count += 1

    wordList = sorted(wordList, key=lambda l:l[1], reverse = True) # sorts by values

    wordz = []
    valuez = []

    for i in range (len(wordList)):
            wordz.append(wordList[i][0])
            valuez.append(wordList[i][1])

    print(wordz)
    print(valuez)

    plt.bar(wordz, valuez)
    plt.xticks(range(len(wordz)), wordz)
    plt.show()

    #TWEEPY>CURSOR // JSON LIBRARY TO GET MORE THAN 200 TWEETS
    #Why arent the y values plotting correctly!?!?!?!??!?!?
    #Completely abandon what im trying to do, use dataframe in pandas or numpy

main()
