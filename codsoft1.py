def simple_chatbot(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Rule 1: Greetings
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    # Rule 2: Weather inquiry
    elif "weather" in user_input:
        return "I'm sorry, I'm just a simple chatbot and don't have real-time weather information."

    # Rule 3: Farewell
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"

    # Default rule if no match is found
    else:
        return "I'm not sure how to respond to that. Can you ask me something else?"

# Main loop for the chatbot
while True:
    # Get user input
    user_input = input("You: ")

    # Exit the loop if the user types 'exit'
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    # Get the chatbot's response based on the rules
    bot_response = simple_chatbot(user_input)

    # Print the chatbot's response
    print("Chatbot:", bot_response)
