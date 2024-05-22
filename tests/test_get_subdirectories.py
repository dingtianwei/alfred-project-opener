from src import search
from pathlib import Path

if __name__ == '__main__':
    p = Path.joinpath(Path.home(),Path("~/Projects").expanduser())
    p2 = Path.joinpath(Path.home(), Path("~/go/src/github.com").expanduser())
    lp = [p,p2]
    print(lp)
    res = search.X.get_subdirectories(lp,2)
    print(res)
    print(len(res))
