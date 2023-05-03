
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os


bot = ChatBot('Bot')
trainer = ListTrainer(bot)

for files in os.listdir('data/'):
    data = open('data/'+files, 'r', encoding='utf-8').readlines()

    trainer.train(data)

while True:
    question = input('>>')
    answer = bot.get_response(question)
    print(answer)


