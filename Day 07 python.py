import random
import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [r"my name is (.*)", ["Hello %1, nice to meet you!"]],
    [r"hi|hello|hey", ["Hello!", "Hey there!", "Hi!"]],
    [r"what is your name?", ["I'm a Python chatbot, here to help you learn!"]],
    [r"how are you?", ["I'm just a bunch of code, but thanks for asking!"]],
    [r"quit", ["Goodbye!"]]
]

def chatbot_simple():
    print('hi, i am your chatbot! pleast type "quit" to exit')
    chat = Chat(pairs, reflections)
    chat.converse()

chatbot_simple()