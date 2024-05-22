from src import search
from pathlib import Path
from functools import reduce

if __name__ == '__main__':
    p = Path.joinpath(Path.home(),Path("~/Projects").expanduser())

    res = search.X.dir_reducer([],p)
    print(res)

    # x = search.X("~/.alfred_project_opener.json")
    # print(x())
