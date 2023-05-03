from nltk.chat.util import Chat
from nltk.chat.util import reflections


pairs = [
    # Greetings
    [
        r"hi|hello|hey|yo",
        ["Hello!", "Hi there!", "Hey!", "Yo!"]
    ],
    [
        r"how are you ?|how are you doing ?",
        ["I'm doing well, thank you for asking.", "I'm good, thanks!", "I'm feeling great!"]
    ],
    [
        r"what's up|what is up|what's new|what is new",
        ["Not much, just chatting with you!", "Just hanging out here. How about you?"]
    ],
    [
        r"good (morning|afternoon|evening|night)",
        ["Good %1!"]
    ],

    # Personal information
    [
        r"what's your name ?|what are you called ?",
        ["My name is ChatBot."]
    ],
    [
        r"what's my name ?|what am I called ?",
        ["I'm sorry, I don't know your name. What should I call you?"]
    ],
    [
        r"my name is (.*)",
        ["Hello, %1! How can I assist you?", ]
    ],
    [
        r"where are you from ?",
        ["I was created by a team of developers using Python and NLTK."]
    ],
    [
        r"what do you do ?|what's your purpose ?|what's your function ?",
        ["I'm a chatbot! I can chat with you and answer questions you might have."]
    ],


    # Jokes
    [
        r"tell me a joke|say something funny",
        ["Why don't scientists trust atoms? Because they make up everything!"]
    ],

    # Farewells
    [
        r"bye|goodbye|see you|take care",
        ["Goodbye!", "See you later!", "Take care!"]
    ],
    [
        r"thanks|thank you",
        ["You're welcome!", "No problem.", "Anytime!"]
    ]
]


def startChat():
    print('Welcome to chatbot!')
    chat = Chat(pairs, reflections)
    return chat.converse()


startChat()
