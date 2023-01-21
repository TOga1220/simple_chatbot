import string
import os
from pathlib import Path

class ChatModel(object): 
    def __init__(self, name):
        self.name = name
        
    def hello(self):
        path = Path(__file__).resolve().parent.parent
        with open(os.path.join(path, "template/first.txt")) as f:
            t = string.Template(f.read())
        contents = t.substitute(name=self.name)
        print(contents)
    