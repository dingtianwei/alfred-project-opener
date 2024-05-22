#!/usr/bin/env python3
import sys
import os
import json
from functools import reduce
from pathlib import Path

CONFIG_FILE = os.getenv("alfred_project_opener_config", "~/.alfred_project_opener.json")

code_icon_map = {
    "iTerm": "icons/iterm2_dir.png",
    "PyCharm": "icons/pycharm_dir.png",
    "IntelliJ IDEA": "icons/idea_dir.png",
    "Visual Studio Code": "icons/vscode_png.png",
    "GoLand": "icons/goland_dir.png",
    "WebStorm": "icons/webstorm_dir.png"

}

default_icon="icons/default_dir.png"

class X:
    def __init__(self, config_file_path):
        self.cfg = self.get_config(config_file_path)
        self.all_projects = []
        self.res_projects = []
        self.keywords_filter_list = self.cfg.get("keywords_filter_list", [])
        self.endwith_filter_list = self.cfg.get("endwith_filter_list", [])
        self.name_filter_list = self.cfg.get("name_filter_list", [])

    @classmethod
    def parse_path_list(cls, path_list):
        res = []
        for item in path_list:
            item_strip = item.strip()
            if item_strip == "":
                continue
            p = Path.joinpath(Path.home(), Path(item_strip).expanduser())
            if cls.is_dir(p):
                res.append(p)
        return res

    @staticmethod
    def get_config(config_file_path):
        res = {}
        p = Path.joinpath(Path.home(), Path(config_file_path.strip()).expanduser())
        if p.exists():
            with p.open() as f:
                res = json.load(f)
        return res

    @staticmethod
    def is_dir(item_path: Path):
        res = False
        if item_path.is_dir():
            res = True
        elif item_path.is_symlink() and item_path.resolve().is_dir():
            res = True
        return res

    # Get subdirectories of from a directory list
    @classmethod
    def dir_reducer(cls, res_list: list, item: Path):
        p: Path
        for p in item.iterdir():
            if cls.is_dir(p):
                res_list.append(p)
        return res_list

    @classmethod
    def get_subdirectories(cls, directory_list, level=0):
        if not directory_list:
            return []
        if level == 0:
            return directory_list
        res = reduce(cls.dir_reducer, directory_list, [])
        level -= 1
        return cls.get_subdirectories(res, level)

    def get_all_projects_origin(self):
        for i in range(3, -1, -1):
            deep_path_list_key = "deep%d_list" % i
            deep_path_list_value = self.cfg.get(deep_path_list_key, [])
            deep_path_list = self.parse_path_list(deep_path_list_value)
            self.all_projects.extend(self.get_subdirectories(deep_path_list, i))
        return self.all_projects

    @staticmethod
    def search_name(p, name_search_list):
        if not name_search_list:
            return True
        if not name_search_list:
            return False
        return all([name in p.name for name in name_search_list])

    @staticmethod
    def filter_keyworkd(p, keywords_filter_list):
        return not any([keywords in str(p) for keywords in keywords_filter_list])

    @staticmethod
    def filter_endwith(p, endwith_filter_list):
        return not any([str(p).endswith(endwith) for endwith in endwith_filter_list])

    @staticmethod
    def fileter_name(p, name_filter_list):
        return not any([name in p.name for name in name_filter_list])

    def get_res_projects(self, name_search_list):
        for p in self.all_projects:
            if p in self.res_projects:
                continue
            name_search_res = self.search_name(p, name_search_list)
            keywords_filter_res = self.filter_keyworkd(p, self.keywords_filter_list)
            endwith_filter_res = self.filter_endwith(p, self.endwith_filter_list)
            name_filter_res = self.fileter_name(p, self.name_filter_list)
            if all([name_search_res,
                    keywords_filter_res,
                    endwith_filter_res,
                    name_filter_res]):
                self.res_projects.append(p)
        return self.res_projects

    def search(self, name_search_list):
        self.get_all_projects_origin()
        self.get_res_projects(name_search_list)
        return self.res_projects

def get_item(project_name,project_path,project_code_bin, icon_path=default_icon):
    return {
        "type": "file",
        "title": project_name,
        "subtitle": project_path,
        "arg": project_path,
        "autocomplete": project_name,
        "icon": {
            "path": icon_path
        },
        "variables": {
            "code_bin": project_code_bin,
            "project_name": project_name
        }
    }

def get_res(x, code_bin):
    res_items_list = []
    res_dict = {"items": res_items_list}
    code_icon = code_icon_map.get(code_bin, default_iconlsp)
    for path in x.res_projects:
        res_items_list.append(get_item(path.name,str(path),code_bin,code_icon))
    if not res_items_list:
        res_items_list.append(get_item("NO RESULT", "SEARCH NO RESULT here by this name", ""))

    return res_dict



if __name__ == "__main__":
    res_items_list = []
    x = X(CONFIG_FILE)
    arg_code_bin = sys.argv[1]
    arg_name_search_list = [i for i in (sys.argv[2:])]

    x.search(arg_name_search_list)
    res_dict = get_res(x, arg_code_bin)
    res_json = json.dumps(res_dict, indent=2)
    print(res_json)





