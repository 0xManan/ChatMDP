import openai

# Use the API key from your OpenAI account
openai.api_key = "YOUR_API_KEY"

# Store previous conversation in a list
conversation = []

while True:
    # Take user input
    user_input = input("You: ")
    conversation.append(user_input)

    # Define the prompt that you want to generate text for
    prompt = (f"{' '.join(conversation)}")

    # Use the `Completion` API to generate text
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # The `completions` variable will now contain the generated text
    generated_text = completions.choices[0].text
    print("AI: ", generated_text)
    conversation.append(generated_text)
