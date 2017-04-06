"""
Problem

Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t)
dH(s,t), is the number of corresponding symbols that differ in s and t.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)

Sample Dataset
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample Output
7
"""
from sys import argv

script, s1, s2 = argv


def distance(s, t):
    i = 0
    difference = 0
    while i < len(s):
        if s[i] != t[i]:
            difference += 1
        i += 1
    return difference

if __name__ == '__main__':
    print distance(s1, s2)