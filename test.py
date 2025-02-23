import openai
from dotenv import load_dotenv
import os


load_dotenv()

class Model:
    def __init__(self):
        self.client = openai  
        self.prompt_engineering = (
            "On a scale from 0 to 1, rate how natural the following Tweet sounds. "
            "A score of 0 is very unnatural and 1 is very natural.\n\n{sentence}\n\nScore:"
        )

    def score_naturalness(self, sentence):
        prompt = self.prompt_engineering.format(sentence=sentence)

        response = self.client.chat.completions.create(
            model="gpt-4",  
            messages=[
                {"role": "system", "content": "You are an AI that rates the naturalness of sentences."},
                {"role": "user", "content": prompt},
            ],
        )

        score_text = response.choices[0].message.content.strip()

        try:
            score = float(score_text.split()[0])  
        except ValueError:
            score = 0.0

        return round(score, 2)


if __name__ == "__main__":
    model = Model()
    
