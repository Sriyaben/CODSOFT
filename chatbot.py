import random

# Define a list of predefined rules and responses
responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a computer program, but I'm here to help you!",
    "goodbye": "Goodbye! Have a great day!",
    "default": "I'm not sure how to respond to that. Can you please rephrase your question?"
}

# Function to generate a response based on user input
def chatbot_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check if the user input matches any predefined rules
    if user_input in responses:
        return responses[user_input]
    else:
        return responses["default"]

# Main loop for the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    else:
        response = chatbot_response(user_input)
        print("Chatbot:", response)
