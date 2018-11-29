import pickle
import math
import matplotlib.pyplot as plt
import numpy as np

chars = {"jin", "sun", "jack", "kate", "sawyer", "juliet"}
charData = pickle.load(open("charData.p", "rb")) 


'''
# Sentiment Calculations
sentimentAvg = {}
for char in chars:
    sentimentAvg[char] =  sum(charData[char][0])/len(charData[char][0])
for char in chars:
    sentimentAvg[char] -= 0.09
pickle.dump( sentimentAvg, open( "sentimentAvg.p", "wb" ) )
sentimentAvg = pickle.load(open("sentimentAvg.p", "rb")) 
'''
'''
# Word frequency calculations
'''
wordFreq = []
for char in chars:
    sorted_x = sorted(x.items(), key=operator.itemgetter(1))
#plt.bar(range(len(sentimentAvg)), list(sentimentAvg.values()), align='center')
#plt.xticks(range(len(sentimentAvg)), list(sentimentAvg.keys()))

#plt.title("Simple Plot")


#plt.show()
