from src import search
import sys
import json

if __name__ == '__main__':
    sys.argv.append("goLand")
    sys.argv.append("zshc")
    sys.argv.append("shconf")
    print(sys.argv)


    x = search.X(search.CONFIG_FILE)
    arg_code_bin = sys.argv[1]
    arg_name_search_list = [i for i in (sys.argv[2:])]

    x.search(arg_name_search_list)

    print(x.res_projects)

   
    res_dict = search.get_res(x, arg_code_bin)



    print(json.dumps(res_dict,indent=2))

