import pickle

chars = {"jin", "sun", "jack", "kate", "sawyer", "juliet"}
charData = {}
for char in chars:
    charData[char] = [[], {}]
for i in range(1, 16):
    print(str(i))
    mergeDict = pickle.load(open("charData" + str(i)+ ".p", "rb"))
    for char in chars:
        # Append sentiment scores
        charData[char][0].extend(mergeDict[char][0])
        for word in mergeDict[char][1].keys():
            charData[char][1][word] = charData[char][1].get(word, 0) + mergeDict[char][1][word]


pickle.dump( charData, open( "charData.p", "wb" ) )

