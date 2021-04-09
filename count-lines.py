"""This module  counts the number of lines in standard input
Input: any string from thr system standard input
"""
impo
ort sys

count = 0

for line in sys.stdin:
    count += 1

print (count, "lines in standard input")
