from chatbot.model.rank import RankModel
from chatbot.view.talk import get_template
 
DEFAULT_NAME = "chatbot_man"

class ChatModel(object): 
    def __init__(self, name=DEFAULT_NAME, user_name=None):
        self.name = name
        self.user_name = user_name
        
    def hello(self):
        while True:
            text_file = get_template("hello.txt")
            user = input(text_file.substitute({'name': self.name}))
            self.user_name = user
            break
        
class LanguageChatModel(ChatModel):
    def __init__(self, name=DEFAULT_NAME):
        super().__init__(name=name)
        self.rank_model = RankModel()

        
    def _hello_decorator(func):
        def wrapper(self):
            if not self.user_name:
                self.hello()
            return func(self)
        return wrapper

    @_hello_decorator
    def recommend_language(self):
        new_recommend = self.rank_model.get_most_popular()
        if not new_recommend:
            return None
        text_file = get_template('recommend.txt')
        print(text_file.substitute({
            'user_name':  self.user_name,
            'new_recommend': new_recommend
            }))
        

    @_hello_decorator    
    def ask_favorite_language(self):
        while True:
            text_file = get_template("ask.txt")
            language = input(text_file.substitute({'user_name':  self.user_name}))
            self.rank_model.save(language)
            break

        
    @_hello_decorator
    def goodbye(self):
        text_file = get_template("goodbye.txt")
        print(text_file.substitute({'user_name': self.user_name}))
