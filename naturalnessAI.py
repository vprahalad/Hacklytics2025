import openai
openai.api_key = 'key'
def scoreNaturalness(sentence):
    prompt = f"On a scale from 0 to 1, rate how natural the following Tweet sounds. A score of 0 is very unnatural and 1 is very natural.\n\n{text}\n\nScore:"
     response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=10,
        n=1,
        stop=None,
        temperature=0.0 
    )

    score = response.choices[0].text.strip()
    return score
