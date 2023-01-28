import openai_secret_manager
import openai
import textwrap
import os
import pandas as pd
from tqdm import tqdm

# Let's setup the API key
assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secrets("openai")

openai.api_key = secrets["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"]

try:
    prompt = input("Enter the prompt for the model: ")
    num_tokens = int(input("Enter the number of tokens to generate: "))
    model = input("Enter the model to use(text-davinci-002 or text-curie-001):")
    temperature = float(input("Enter temperature (default is 0.5):"))
    stop = input("Enter the stop token(if any): ")
    n = int(input("Enter the number of completions to generate: "))
    filename = input("Enter the filename to save the output:")
    if stop=="":
        stop = None
    data = []
    for i in tqdm(range(n)):
        completions = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=num_tokens,
            n=1,
            stop=stop,
            temperature=temperature,
        )
        message = completions.choices[0].text
        message = textwrap.fill(message,width=80)
        data.append({'generated_text': message, 'prompt': prompt, 'model': model, 'stop':stop, 'temperature': temperature})
    if filename:
        df = pd.DataFrame(data)
        if not os.path.exists(filename):
            df.to_csv(filename)
        else:
            df.to_csv(filename, mode='a', header=False)
    print(message)
except Exception as e:
    print("Error Occured:",e)
