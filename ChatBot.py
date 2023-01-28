import openai

class ChatGPT:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key

    def chat(self, prompt):
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = completions.choices[0].text
        return message

# Instantiate the ChatGPT class with your API key
chat = ChatGPT(API_KEY)

# Use the chat() function to generate a response to a prompt
response = chat.chat("Hello, how are you?")
print(response)
