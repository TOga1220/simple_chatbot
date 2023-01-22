from chatbot.model import talk

def talk_programming_language():
    chat_bot = talk.LanguageChatModel()
    chat_bot.ask_favorite_language()
    chat_bot.goodbye()
    


