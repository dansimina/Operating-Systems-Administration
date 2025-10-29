#!/usr/bin/env python3

import subprocess
import os

def main():
    ls_results = subprocess.run(["ls"], capture_output=True, text=True).stdout.split('\n')

    listdir_results = sorted(os.listdir("./"))

    if len(ls_results) - 1 != len(listdir_results):
        print("Diffrent lengths!")
        return
    
    n = len(listdir_results)
    for i in range(n):
        print(f"ls: {ls_results[i]} listdir: {listdir_results[i]} same: {ls_results[i] == listdir_results[i]}")
    
if __name__ == "__main__":
    main()