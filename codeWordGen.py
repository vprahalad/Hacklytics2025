import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
import numpy as np

nltk.download('punkt')

def codeWordGen(csvFilepath):
    df = pd.read_csv(csvFilepath, usecols=[1])
    allWords = []
    wordsInRange = []
    for sentence in df.iloc[:, 0].dropna():
        allWords.extend(word_tokenize(sentence.lower()))
    wordFreq = Counter(allWords)
    freqs = list(wordFreq.values())
    bounds = np.mean(freqs)
    #Bounds = np.percentile(freqs, 50)
    # upperBound = freqs[int(n * 0.6)]

    for word, freq in wordFreq.items():
        if freq == int(bounds):
        #if freq >= Bounds and freq <= Bounds:
            wordsInRange.append(word)

    return wordsInRange

csvFilepath = "cleaned_data.csv"
#print(codeWordGen(csvFilepath))

