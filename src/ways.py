import sys
import os
def get_item(title,subtitle,arg, autocomplete, code_bin):
    return {
        "type": "file",
        "title": title,
        "subtitle": subtitle,
        "arg": arg,
        "autocomplete": autocomplete,
        # "icon": {
        #     "path": "icons/dir.png"
        # },
        "variables": {
            "code_bin": code_bin,
        }
    }

def list_ways(path, name, apps: list):
    res_items_list = []
    res = {"items": res_items_list}
    for app in apps:
        way = get_item("Open %s with %s" %(name, app), path, path, path, app)
        res_items_list.append(way)

    return res


def main():

    path_string = sys.argv[1]
    if path_string is "":
        return ""

    ways = sys.argv[2:]
    path_name = os.path.basename(path_string)
    res_dict = list_ways(path_string, path_name, ways)
    print(res_dict)


if __name__ == '__main__':
    main()



