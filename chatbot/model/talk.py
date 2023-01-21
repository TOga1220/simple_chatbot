import string
import os
from pathlib import Path

DEFAULT_NAME = "chatbot_man"
path = Path(__file__).resolve().parent.parent

class ChatModel(object): 
    def __init__(self, name=DEFAULT_NAME, user_name=None):
        self.name = name
        self.user_name = user_name
        
    def hello(self):
        while True:
            with open(os.path.join(path, "template/hello.txt")) as f:
                text_file = string.Template(f.read())
            user = input(text_file.substitute({'name': self.name}))
            self.user_name = user
            break
        
class LanguageChatModel(ChatModel):
    def __init__(self, name=DEFAULT_NAME):
        super().__init__(name=name)
        
    def _hello_decorator(func):
        def wrapper(self):
            print('--start--')
            if not self.user_name:
                self.hello()
            print('--end--')
            return func(self)
        return wrapper
     
    @_hello_decorator    
    def ask_user_favorite(self):
        while True:
            with open(os.path.join(path, "template/ask.txt")) as f:
                text_file = string.Template(f.read())
            language = input(text_file.substitute({'user_name':  self.user_name}))
            break
    
            
