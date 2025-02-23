import openai
from dotenv import load_dotenv
import os

# Load environment variables (if using API keys stored in .env)
load_dotenv()

class Model:
    def __init__(self):
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Load API key
        self.prompt_engineering = (
            "Your task is to construct a natural-sounding Tweet using the given words "
            "in the order they appear in the input list, though the words from  the "
            "input list can be separated by other words. Do not use the given words more times than the given words "
            "appear in the input list. Ensure the sentence fits in the character limit "
            "and sounds like a normal Tweet. Ensure the ratio of code words to total words in the generated Tweet is " 
            "within 0.2 to 0.4."
        )

    def generate_sentence(self, code_words):
        # Convert list of words into a string for the prompt
        words_string = ", ".join(code_words)

        # Make API request
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": self.prompt_engineering},
                {"role": "user", "content": f"Code words: {words_string}"},
            ],
        )

        return completion.choices[0].message.content.strip()

# Example usage
if __name__ == "__main__":
    model = Model()
    
    # Example list of code words
    code_words = values
    
    sentence = model.generate_sentence(code_words)
    print("Generated Sentence:", sentence)
