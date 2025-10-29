#!/usr/bin/env python3

import os
import sys

def main():
    prog = sys.argv[1]
    paths = os.getenv("PATH").split(":")
    
    for path in paths:
        if prog in os.listdir(path):
            result = os.path.join(path, prog)
            print(result)
            return 
    
    print("Not found!")


if __name__ == "__main__":
    main()