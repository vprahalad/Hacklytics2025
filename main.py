from model import Model as SentenceModel  
from naturalnessAI import Model as NaturalnessModel 
from assignREAL import codeWordAssign

if __name__ == "__main__":
    # sentence generation
    sentence_model = SentenceModel() 
    secret_message = "I love coding." # replace with user inputted message
    word_dict, code_words = codeWordAssign(secret_message, wordsInRange)
    sentence = sentence_model.generate_sentence(code_words)  
    print("Generated Sentence:", sentence)
    
    # scoring the naturalness 
    naturalness_model = NaturalnessModel()
    score = naturalness_model.score_naturalness(sentence)  
    print("Naturalness Score:", score)  
