def efficiencyCalc(code_words, sentence):
    sentenceList = sentence.split()
    efficiency = len(code_words) / len(sentenceList)
    return efficiency
def efficiencyWarning(efficiency):
    if efficiency < 0.2:
        warning = "WARNING: This code has an efficiency score of less than 20% and may have too many filler words in comparison to code words. Try again?"
    elif efficiency > 0.4:
        warning = "WARNING: This code has an efficiency score of greater than 40%. This means that there may be too many code words and not enough filler words in the sentence. Try again?"
        
    
