from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


bot = ChatBot(
    'Q and A!',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///qna.sqlite3'
)

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "I am doing very well, thank you for asking.",
    "Good morning! How are you doing?",
    "Do you like hats?"
]

trainer = ListTrainer(bot)

trainer.train(conversation)

while True:
    try:
        bot_input = bot.get_response(input("user: "))
        print("bot:", bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break

