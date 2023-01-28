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


def main():
    API_KEY = "YOUR_API_KEY_HERE"
    chat = ChatGPT(API_KEY)
    while True:
        user_input = input("You: ")
        response = chat.chat(user_input)
        print("Chatbot: ", response)
        
if __name__ == "__main__":
    main()
