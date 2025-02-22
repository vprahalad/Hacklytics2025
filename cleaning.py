import pandas as pd
import nltk
import re
from nltk.tokenize import sent_tokenize
nltk.download('punkt')

def clean_text(text):
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'#\w+', '', text)
    text = re.sub(r'@\w+', '', text)         
    return text.strip()

file_path = "Users/leela/Downloads/training.1600000.processed.noemoticon.csv"
df = pd.read_csv(file_path)
column_name = 'F'
df['cleaned_text'] = df[column_name].astype(str).apply(clean_text)
df['tokenized_sentences'] = df['cleaned_text'].apply(sent_tokenize)
df.to_csv("cleaned_output.csv", index=False)