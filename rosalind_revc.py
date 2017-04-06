"""
Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
The reverse complement of a DNA string s is the string s^c formed by reversing the symbols of s,
then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement s^c of s.

Sample Dataset
AAAACCCGGT

Sample Output
ACCGGGTTTT
"""

from sys import argv
script, dna = argv

def revcom(dna):
    rc = dna[::-1]
    rc = rc.replace('A','X')
    rc = rc.replace('T', 'A')
    rc = rc.replace('C', 'Y')
    rc = rc.replace('G', 'C')
    rc = rc.replace('X','T')
    rc = rc.replace('Y', 'G')
    return rc

if __name__ == '__main__':
    print revcom(dna)