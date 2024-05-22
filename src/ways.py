import sys
import os
import json
code_bin_icon_map = {
    "iTerm": "icons/iterm2_dir.png",
    "PyCharm": "icons/pycharm_dir.png",
    "IntelliJ IDEA": "icons/idea_dir.png",
    "Visual Studio Code": "icons/vscode_dir.png",
    "GoLand": "icons/goland_dir.png",
    "WebStorm": "icons/webstorm_dir.png"

}
def get_item(title,subtitle,arg, autocomplete, code_bin,code_bin_icon):
    return {
        "type": "file",
        "title": title,
        "subtitle": subtitle,
        "arg": arg,
        "autocomplete": autocomplete,
        "icon": {
            "path": code_bin_icon
        },
        "variables": {
            "code_bin": code_bin,
        }
    }

def list_ways(path, name, apps: list):
    res_items_list = []
    res = {"items": res_items_list}
    for app in apps:
        icon = code_bin_icon_map.get(app, "icons/default.png")
        way = get_item("Open %s with %s" %(name, app), path, path, path, app,icon)
        res_items_list.append(way)

    return res


def main():

    path_string = sys.argv[1]
    ways = sys.argv[2:]
    path_name = os.path.basename(path_string)
    res_dict = list_ways(path_string, path_name, ways)
    print(json.dumps(res_dict,indent=2))


if __name__ == '__main__':
    main()

