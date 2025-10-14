#!/usr/bin/env python3

def main():
    my_list = [1, 2, 3, 4, 2, 6, 2, 3, 5, 4, 8, 7]
    freq = dict()

    for x in my_list:
        freq[x] = freq.get(x, 0) + 1
    
    print(freq)

if __name__ == "__main__":
    main()