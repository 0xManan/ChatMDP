import openai

# Your OpenAI API key
openai.api_key = "YOUR_API_KEY"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        temperature=0.5
    )
    return response.choices[0].text

def main():
    print("Welcome to the chatbot, type 'exit' to leave.")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            print("Thank you for using our chatbot, have a good day!")
            break
        elif user_input.strip() == "":
            print("Please enter a valid input.")
            continue
        else:
            prompt = f"{user_input}\n"
            chatbot_response = generate_response(prompt)
            print("Chatbot: " + chatbot_response)

if __name__ == "__main__":
    main()
