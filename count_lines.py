"""
Aim: This script counts the number of lines in standard input
Input: Strings from the command line
Output: Gives the output as the total number of lines
"""
import sys

count = 0
for line in sys.stdin:
	count += 1

print(count, "lines in standard input")
