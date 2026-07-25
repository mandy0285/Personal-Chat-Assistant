#Rule based Personal Chat Assistant

import datetime
import time

chatbotname = "Alex"

Name = input("Please enter your name: ")

current_time = datetime.datetime.now()

if 5 <= current_time.hour <= 11:
    print(f"Good Morning {Name}!")
elif 11 <= current_time.hour < 17:
    print(f"Good Afternoon {Name}!")
elif 17 <= current_time.hour < 20:
    print(f"Good Evening {Name}!")
else:
    print(f"Good Night {Name}!")


print(f"\nWelcome to your Personal Chat Assistant!. My name is {chatbotname}'s")
print("\n I am here to help you with your basic queries. \n Please type 'bye' to end the chat.\n")

#chatbot memory creation using dictionary responses
responses = {
    "hi": "Hello! How can I assist you today?",
    "hello": "Hi there! What can I do for you?",
    "how are you": "I'm just a program, but I'm here to help you!",
    "what is your name": "I am your Personal Chat Assistant.",
    "what can you do": "I can answer your basic queries and assist you with information.",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I don't understand that. Can you please rephrase?",
    "motivate me": "Believe in yourself! You can achieve anything you set your mind to.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!"
}

#Method/funtion to get response from the chatbot
def get_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]

    return responses["default"]

#Take user input and respond accordingly
while True:
    userInput = input("How can I help you? ")
    response = get_response(userInput)
    print(f"{chatbotname}: ", response)

    if userInput.lower() == "bye":
        break
