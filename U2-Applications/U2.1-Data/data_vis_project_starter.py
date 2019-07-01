'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below! 
tweettext = []
tweetstring = ""
for tweet in tweetData: 
    tweetstring += tweet['text']
    text = tweet['text']
    tweettext.append(text)
print(tweetstring)
    

# # Textblob sample:

polarity = []
subjectivity = []

word_dict = {}

tweetBlob = TextBlob(tweetstring)
for word in tweetBlob.words:
    word_dict[word.lower()] = tweetBlob.word_counts[word.lower()]
    print(word_dict)





for tweets in tweettext: 
    tb = TextBlob(tweets)
    # print(tb.sentiment)
    polarity.append(tb.polarity)
    subjectivity.append(tb.subjectivity)
pavg = sum(polarity)/len(polarity)
psub = sum(subjectivity)/len(polarity)

print(pavg)
print(psub)



import matplotlib.pyplot as plt


plt.hist(polarity, bins=[-1, -0.5, 0.0, 0.5, 1])
plt.xlabel('Values')
plt.ylabel('Number of Items')
plt.title('Histogram of Polarity')
plt.axis([-1.1, 1.1, 0, 150])
plt.grid(True)
plt.show()

plt.hist(subjectivity, bins=[-1, -0.5, 0.0, 0.5, 1])
plt.xlabel('Values')
plt.ylabel('Number of Items')
plt.title('Histogram of Subjectivity')
plt.axis([-1.1, 1.1, 0, 150])
plt.grid(True)
plt.show()


    