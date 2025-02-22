import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
import numpy as np

nltk.download('punkt')
def codeWordGen(csvFilepath):
    df = pd.read_csv(csvFilepath)
    allWords = []
    for sentence in df.dropna():
        allWords.extend(word_tokenize(sentence.lower()))
    wordFreq = Counter(allWords)
    freqs = list(wordFreq.values())
    meanFreq = np.mean(freqs)
    stdDev = np.std(freqs)
    wordsInRange = [word for word, freq in wordFreq.items() if meanFreq - stdDev <= freq <= meanFreq + stdDev]
    return wordsInRange
csvFilepath = "cleaned_data.csv"
print(codeWordGen(csvFilepath))