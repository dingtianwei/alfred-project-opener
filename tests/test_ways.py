from src import ways
import sys

if __name__ == '__main__':
    sys.argv.append("/a/b/c")
    sys.argv.append("code")
    sys.argv.append("iterm")

    ways.main()



