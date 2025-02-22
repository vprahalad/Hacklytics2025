import pandas as pd
import nltk
import re
from nltk.tokenize import sent_tokenize
nltk.download('punkt')
nltk.download('punkt_tab')

def clean_text(text):
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'#\w+', '', text)
    text = re.sub('@[^\s]+','', text)
    return text.strip()

file_path = "/Users/rinibokil/Downloads/training.1600000.processed.noemoticon.csv"
df = pd.read_csv(file_path, nrows=10000)

# Ensure the correct column is being used for text data
df['cleaned_text'] = df.iloc[:, 0].astype(str).apply(clean_text)
df['tokenized_sentences'] = df['cleaned_text'].apply(sent_tokenize)

# Save the cleaned and tokenized data to a new CSV file
df.to_csv("cleaned_output.csv", index=False)
print("Cleaned and tokenized data saved to cleaned_output.csv")
