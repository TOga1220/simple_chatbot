import os
import string
from pathlib import Path
path = Path(__file__).resolve().parent.parent

def get_template(file_name):
    with open(os.path.join(path, f"template/{file_name}")) as f:
        contents = f.read()
        contents = contents.rstrip(os.linesep)
        contents = '{splitter}{sep}{contents}{sep}{splitter}{sep}'.format(
          contents=contents, splitter="=" * 40, sep=os.linesep)
        return string.Template(contents)
        