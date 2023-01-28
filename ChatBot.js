const openai = require("openai");

openai.apiKey = "YOUR_API_KEY";

async function generateResponse(prompt, temperature = 0.5, maxTokens = 2048, stop = null, engine = "text-davinci-002") {
  const completions = await openai.Completion.create({
    engine: engine,
    prompt: prompt,
    temperature: temperature,
    maxTokens: maxTokens,
    stop: stop,
    n: 1,
  });

  let message = completions.choices[0].text;
  return message.trim();
}

async function main() {
  console.log("Welcome to the chatbot, type 'exit' to leave.");
  // Prime the model with some context
  let primingText = "Hello, I am a chatbot. How can I help you today?";
  console.log("Chatbot: " + primingText);
  while (true) {
    let userInput = await new Promise((resolve) => {
      process.stdin.once("data", function (data) {
        resolve(data.toString().trim());
      });
    });
    if (userInput.toLowerCase() === "exit") {
      console.log("Thank you for using our chatbot, have a good day!");
      break;
    } else if (userInput === "") {
      console.log("Please enter a valid input.");
      continue;
    } else {
      let prompt = `${primingText}\n${userInput}\n`;
      let chatbotResponse = await generateResponse(prompt);
      console.log("Chatbot: " + chatbotResponse);
      primingText = `${primingText}\n${userInput}\n${chatbotResponse}\n`;
    }
  }
}

main();
