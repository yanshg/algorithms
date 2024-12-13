import os
import re

def lowercase_dir_name(base_dir):
    for path, sub_dirs, sub_files in os.walk(base_dir, topdown=False):
        print(f"\n==== {path} ====")
        for sub_dir in sub_dirs:
            if sub_dir.startswith('tmp-mount'):
                continue

            print(f"sub_dir: {sub_dir}")
            orig_path = os.path.join(path, sub_dir)
            new_path = os.path.join(path, sub_dir.lower())
            if orig_path != new_path:
                print(f"renaming {orig_path} to {new_path}")
                #os.rename(dir_name_orig, dir_name_lowercase)

        for sub_dir in os.listdir(path):
            full_path = os.path.join(path, sub_dir)
            if os.path.isdir(full_path):
                print("listdir  sub_dir", full_path)

        for sub_file in sub_files:
            if not sub_file:
                continue

            print(f"sub_file: {sub_file}")
            if re.match(r'.*\.csv$', sub_file):
                print(f"csv file with re.match: {sub_file}")

            if re.search(r'\.csv$', sub_file):
                print(f"csv file with re.search: {sub_file}")

            if sub_file.endswith(r'.csv'):
                print(f"csv file with endswith: {sub_file}")

lowercase_dir_name('/tmp/test')