def efficiencyCalc(code_words, sentence):
    sentenceList = sentence.split()
    efficiency = len(code_words) / len(sentenceList)
    return efficiency
