import random

responses = {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thank you!", "I'm doing well, how about you?", "All good!"],
    "what is your name": ["I'm a chatbot.", "You can call me ChatBot.", "My name is AI Assistant."],
    "bye": ["Goodbye!", "See you later!", "Bye-bye!"],
    "default": ["I'm not sure how to respond to that.", "Could you please rephrase your question?"]
}

def get_response(user_input):

    user_input = user_input.lower()

    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])

    return random.choice(responses["default"])

print("ChatBot: Hi! I am ChatBot. How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("ChatBot: Goodbye!")
        break
    else:
        response = get_response(user_input)
        print("ChatBot:", response)
