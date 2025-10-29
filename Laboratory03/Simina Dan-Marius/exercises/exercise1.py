#!/usr/bin/env python3

import sys

def main():
	nums = [int(sys.argv[i]) for i in range(1, len(sys.argv))]
	div = int(1)
	for i in range(2, min(nums) + 1):
		ok = True
		for x in nums:
			if x % i != 0:
				ok = False
				break
		if ok == True:
			div = i
	print(div)

if __name__ == "__main__":
	main()
