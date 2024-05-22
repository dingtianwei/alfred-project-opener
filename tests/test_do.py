from src import search
from pathlib import Path

if __name__ == '__main__':
    x = search.X("~/.alfred_project_opener.json")
    print(x.do("MKK"))
