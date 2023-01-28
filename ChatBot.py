import openai

openai.api_key = "YOUR_API_KEY"

def generate_response(prompt, temperature=0.5, max_tokens=2048, stop=None, engine="text-davinci-002"):
    completions = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        stop=stop,
        n=1
    )

    message = completions.choices[0].text
    return message.strip()

def main():
    print("Welcome to the chatbot, type 'exit' to leave.")
    # Prime the model with some context
    priming_text = "Hello, I am a chatbot. How can I help you today?"
    print("Chatbot: " + priming_text)
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            print("Thank you for using our chatbot, have a good day!")
            break
        elif user_input.strip() == "":
            print("Please enter a valid input.")
            continue
        else:
            prompt = f"{priming_text}\n{user_input}\n"
            chatbot_response = generate_response(prompt)
            print("Chatbot: " + chatbot_response)
            priming_text = f"{priming_text}\n{user_input}\n{chatbot_response}\n"

if __name__ == "__main__":
    main()
