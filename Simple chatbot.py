import nltk
from nltk.chat.util import Chat, reflections


nltk.download('punkt')

# Define custom reflections for the chatbot
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
}

# Define chatbot responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1! How can I help you today?",]
    ],
    [
        r"what is your name",
        ["I am a basic chatbot. You can call me ChatBot.",]
    ],
    [
        r"how are you",
        ["I'm doing well, thank you!", "I'm just a computer program, so I don't have feelings, but I'm here to help.",]
    ],
    [
        r"(.*) (good|great|well|fine)",
        ["That's wonderful to hear!", "I'm glad to hear that.",]
    ],
    [
        r"(.*) (not good|bad|sad)",
        ["I'm sorry to hear that. How can I assist you?", "I hope things get better for you.",]
    ],
    [
        r"quit",
        ["Goodbye! If you have more questions, feel free to ask.", "See you later!"]
    ],
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Function to start the chat
def start_chat():
    print("ChatBot: Hello! How can I assist you today?")
    print("Type 'quit' to end the conversation.")

    # Start the conversation loop
    while True:
        user_input = input("You: ")

        # Exit the loop if the user types 'quit'
        if user_input.lower() == 'quit':
            print("ChatBot: Goodbye! If you have more questions, feel free to ask.")
            break
            

        # Get and print the chatbot's response
        response = chatbot.respond(user_input)
        print(f"ChatBot: {response}")

start_chat()
