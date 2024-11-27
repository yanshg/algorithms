#!/usr/bin/python3

"""
Build info parser
"""

#####################################################################
# IMPORTS
#####################################################################
import re
import os
import sys
import json
import fnmatch
try:
    from tabulate import tabulate
except ModuleNotFoundError as e:
    print("Module missing. Please install 'pip3 install tabulate'")
    sys.exit(1)

#####################################################################
# Methods
#####################################################################


def get_files_generator(path):
    for dir_path, dir_names, filenames in os.walk(path):
        for file in filenames:
            if fnmatch.fnmatch(file, "*.json"):
                filename = os.path.join(dir_path, file)
                yield filename


def parse_data(path):
    for file in get_files_generator(path):
        url = []
        commits = []
        branches = []

        with open(file) as f:
            try:
                data = json.load(f)
                data = data.get("buildInfo", None)
                if not data:
                    print(f"ERROR: No data present in {file}\n")
                    continue
                for key, value in data["properties"].items():
                    if key.startswith("buildInfo.env.GIT_URL"):
                        if not key.split('_')[-1].isdigit():
                            key = key + '_0'
                        url.append((key, value))
                    if key.startswith("buildInfo.env.GIT_BRANCH"):
                        if not key.split('_')[-1].isdigit():
                            key = key + '_0'
                        branches.append((key, value))
                    if key.startswith("buildInfo.env.GIT_COMMIT"):
                        if not key.split('_')[-1].isdigit():
                            key = key + '_0'
                        commits.append((key, value))

                branches.sort(key=lambda x: int(re.search(r'\d+', x[0]).group()))
                url.sort(key=lambda x: int(re.search(r'\d+', x[0]).group()))
                commits.sort(key=lambda x: int(re.search(r'\d+', x[0]).group()))

                operation_array = []
                package = os.path.basename(file).split('-')[0]
                head = ["Package", "ID", "Repo", "Branch", "Commit"]
                for i, (repo, branch, commit) in enumerate(zip(url, branches, commits)):
                    operation_array.append((package, i, repo[1], branch[1], commit[1]))

                print(tabulate(operation_array, headers=head, tablefmt="grid"))
                print()

            except ValueError as error:
                print(error)
                return False
            except Exception as error:
                print(error)
                return False

    return True


def main():
    if len(sys.argv) < 2:
        print("Please provide full path of the directory.")
        print(f"{sys.argv[0]} <full_directory_path>")
        return False

    path = sys.argv[1]
    if not os.path.exists(path):
        print("Given location does not exists.")
        return False

    return parse_data(path)


if __name__ == "__main__":
    if main():
        sys.exit(0)
    sys.exit(1)
