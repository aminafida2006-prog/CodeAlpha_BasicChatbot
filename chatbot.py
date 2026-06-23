def get_response(user_input):
    user_input = user_input.lower().strip()

    # Greetings
    if user_input in ["hello", "hi", "hey", "hello there", "hi there"]:
        return "Hi there! 😊 How can I help you today?"

    # How are you
    elif user_input in ["how are you", "how are you?", "how r u", "how do you do"]:
        return "I'm doing great, thanks for asking! How about you? 😄"

    # User says they are fine
    elif user_input in ["i'm fine", "i am fine", "fine", "good", "i'm good", "i am good", "great", "doing well"]:
        return "That's wonderful to hear! 🌟 Is there anything I can help you with?"

    # What is your name
    elif user_input in ["what is your name", "what's your name", "who are you", "your name"]:
        return "I'm CodeBot 🤖 — your simple rule-based chatbot built in Python!"

    # What can you do
    elif user_input in ["what can you do", "help", "what do you do", "features"]:
        return ("I can chat with you! Try saying:\n"
                "  👉 hello\n"
                "  👉 how are you\n"
                "  👉 what is your name\n"
                "  👉 tell me a joke\n"
                "  👉 what time is it\n"
                "  👉 bye")

    # Joke
    elif user_input in ["tell me a joke", "joke", "say something funny", "make me laugh"]:
        return "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂"

    # Time
    elif user_input in ["what time is it", "time", "current time", "what's the time"]:
        import datetime
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"⏰ The current time is {now}."

    # Date
    elif user_input in ["what is today's date", "date", "today's date", "what day is it"]:
        import datetime
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"📅 Today is {today}."

    # Thank you
    elif user_input in ["thank you", "thanks", "thank you so much", "thanks a lot"]:
        return "You're welcome! 😊 Always happy to help!"

    # Goodbye
    elif user_input in ["bye", "goodbye", "see you", "see you later", "exit", "quit"]:
        return "Goodbye! 👋 It was nice chatting with you. Have a great day!"

    # Default response
    else:
        return "Hmm, I didn't quite understand that. 🤔 Type 'help' to see what I can do!"


def chatbot():
    print("=" * 45)
    print("        🤖 WELCOME TO CODEBOT!")
    print("     Your Simple Rule-Based Chatbot")
    print("=" * 45)
    print("Type 'bye' to exit the chat.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input == "":
            print("CodeBot: Please type something! 😊\n")
            continue

        response = get_response(user_input)
        print(f"CodeBot: {response}\n")

        # Exit condition
        if user_input.lower() in ["bye", "goodbye", "see you", "see you later", "exit", "quit"]:
            break


if __name__ == "__main__":
    chatbot()
