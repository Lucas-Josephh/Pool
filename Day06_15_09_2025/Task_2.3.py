import os

old_path = []
black_path_list = []


def search_dir(paths):

    contenu = os.listdir(paths)

    for content in contenu:
        if os.path.isdir(content) and not content in black_path_list:
            old_path.insert(0, content)
            return search_dir(f"{paths}\\{content}")

    for result in os.listdir(paths):
        print(f"{paths}\\{result}")

    if os.getcwd() == paths:
        return "FINISH"

    if len(old_path) > 0:
        black_path_list.insert(0, old_path[0])
        last_element = len(old_path[0]) - 1
        old_path.pop(len(old_path) - 1)
        search_dir(paths[: len(paths) - last_element - 2])

    else:
        search_dir(os.getcwd())


print(search_dir(os.getcwd()))
