#!/usr/bin/env python3

import sys
import os
import shutil

def removeEmptyDirs(path: str) -> None:
    for fname in os.listdir(path):
        fpath = os.path.join(path, fname)
        if os.path.isdir(fpath):
            if len(os.listdir(fpath)) == 0:
                print(f"Do you want to delete: {fpath}?")
                user_input = input()

                while user_input.lower() not in ["yes", "no"]:
                    user_input = input()

                if user_input == "yes":
                    shutil.rmtree(fpath)
            else:
                removeEmptyDirs(fpath)

def main():
    if not os.path.isdir(sys.argv[1]):
        print("The argument must be a directory!")
        return 
    
    src = sys.argv[1]
    dst = sys.argv[1] + "(copy)"

    shutil.copytree(src, dst, dirs_exist_ok=True)

    removeEmptyDirs(dst)




if __name__ == "__main__":
    main()