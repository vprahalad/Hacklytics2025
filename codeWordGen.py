import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
import numpy as np

#nltk.download('punkt')

def codeWordGen(csvFilepath):
    df = pd.read_csv(csvFilepath, usecols=[2])
    allWords = []
    for sentence in df.iloc[:, 0].dropna():
        allWords.extend(word_tokenize(sentence.lower()))
    wordFreq = Counter(allWords)
    freqs = list(wordFreq.values())
    lowerBound = np.percentile(freqs, 30)
    upperBound = np.percentile(freqs, 60)
    wordsInRange = [word for (word, freq) in wordFreq.items() if int(lowerBound) <= freq <= int(upperBound)]
    #wordsInRange = [word for word, freq in wordFreq.items() if ]
    return len(wordsInRange)

csvFilepath = "cleaned_data.csv"
print(codeWordGen(csvFilepath))

