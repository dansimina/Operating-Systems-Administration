#!/usr/bin/env python3

import os
import sys
from typing import Tuple

def findMaxSizeFile(dir_path: str) -> Tuple[str, int]:
    file_path = ""
    file_size = 0

    for fname in os.listdir(dir_path):
        fpath = os.path.join(dir_path, fname)
        if os.path.isdir(fpath):
            (res_file, res_size) = findMaxSizeFile(fpath)
            if res_size > file_size:
                file_path = res_file
                file_size = res_size
        elif os.path.isfile(fpath):
            fsize = os.path.getsize(fpath)
            if fsize > file_size:
                file_path = fpath
                file_size = fsize
    
    return (file_path, file_size)

def main():
    (file_name, size) = findMaxSizeFile(sys.argv[1])
    print(f"The file with max size is {file_name}, with size equals to {size}")


if __name__ == "__main__":
    main()