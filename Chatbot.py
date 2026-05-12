# ChatBot

class ChatBot:

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello! I am {self.name}, your friendly chatbot. How can I assist you today?"

    def respond(self, user_input):

        if "hi" in user_input.lower():
            return "Hi there! How can I help you?"

        elif "how are you" in user_input.lower():
            return "I'm just a bot, but I'm doing great! Thanks for asking."

        elif "what is your name" in user_input.lower():
            return f"My name is {self.name}."

        elif "thank you" in user_input.lower():
            return "You're welcome!"

        elif "bye" in user_input.lower():
            return "Goodbye! Have a great day!"

        else:
            return "I'm not sure how to respond to that. Can you please rephrase?"


bot = ChatBot("KP Bot")
print(bot.greet())

while True:
    user_input = input("You: ")
    print("Bot:", bot.respond(user_input))
    if user_input.lower() == "bye":
        break