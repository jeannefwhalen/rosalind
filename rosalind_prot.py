"""
Problem
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except
for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string
will incorporate protein strings along with DNA strings and RNA strings. The RNA codon table dictates the details
regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.

Sample Dataset
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

Sample Output
MAMAPRTEINSTRING
"""
from bioinfo_core import rna_codons
from sys import argv

script, rna = argv

def translate(rna, codon_table):
    if not len(rna)%3==0:
        print "The RNA is incomplete"
        return False
    else:
        i = 0
        prot_string = ''
        while (i + 3) < len(rna):
            prot_string += codon_table[rna[i:(i+3)]]
            i += 3
    return prot_string

if __name__ == '__main__':
    print translate(rna, rna_codons)
