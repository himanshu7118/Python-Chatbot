import chatterbot
from flask import Flask
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

chatbot = ChatBot('Bot')

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.english')

@app.route('/')
def home():
    while True:
        query = str(input("You:"))
        print("bot:",chatbot.get_response(query))
        if "exit" in query:
            break

if __name__ == "__main__":
    app.run(debug=True)


