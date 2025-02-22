import openai
from dotenv import load_dotenv
import os

# Load environment variables (if using API keys stored in .env)
load_dotenv()

class Model:
    def __init__(self):
        self.client = openai  # Correct initialization for openai client
        self.prompt_engineering = (
            "On a scale from 0 to 1, rate how natural the following Tweet sounds. "
            "A score of 0 is very unnatural and 1 is very natural.\n\n{sentence}\n\nScore:"
        )

    def score_naturalness(self, sentence):
        # Prepare the prompt for naturalness scoring
        prompt = self.prompt_engineering.format(sentence=sentence)

        # Make API request
        response = self.client.chat.completions.create(
            model="gpt-4",  # Use the correct model
            messages=[
                {"role": "system", "content": "You are an AI that rates the naturalness of sentences."},
                {"role": "user", "content": prompt},
            ],
        )

        # Extract and return the score from the response
        score_text = response.choices[0].message.content.strip()

        try:
            score = float(score_text.split()[0])  
        except ValueError:
            score = 0.0

        return round(score, 2)


# Example usage
if __name__ == "__main__":
    model = Model()
    
    # Example sentence for scoring
    sentence = "The stock market is flower."
    
    score = model.score_naturalness(sentence)
    print("Naturalness Score:", score)
