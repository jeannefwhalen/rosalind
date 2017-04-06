"""
Problem

Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string
implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three
reading frames result from reading the string itself, whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop
codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids
until a stop codon is reached.

Given:
A DNA string s of length at most 1 kbp in FASTA format.

Return:
Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

Sample Dataset
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

Sample Output
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
"""

from sys import argv
import bioinfo_core

script, fasta_file = argv

fasta_dictionary = bioinfo_core.read_fasta(fasta_file)
dna =  fasta_dictionary.values()[0]


codon = {'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
         'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
         'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
         'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
         'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
         'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
         'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
         'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
         'TAT': 'Y', 'TAC': 'Y', 'CAT': 'H', 'CAC': 'H',
         'CAA': 'Q', 'CAG': 'Q', 'AAT': 'N', 'AAC': 'N',
         'AAA': 'K', 'AAG': 'K', 'GAT': 'D', 'GAC': 'D',
         'GAA': 'E', 'GAG': 'E', 'TGT': 'C', 'TGC': 'C',
         'TGG': 'W', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R',
         'CGG': 'R', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G',
         'GGG': 'G', 'AGA': 'R', 'AGT': 'S', 'AGG': 'R',
         'AGC': 'S'}


def find_start(my_dna):
    i = 0
    j = 3
    pep = my_dna[i:j]
    start_list = []
    while j < len(my_dna):
        if pep == 'ATG':
            start_list.append(i)
        i = i + 1
        j = j + 1
        pep = my_dna[i:j]
    return start_list


def orf_detection(start, DNA):
    stop = ['TAA', 'TAG', 'TGA']
    end = start + 3
    orf = ''
    seq = DNA[start:end]
    while end <= len(DNA):
        seq = DNA[start:end]
        if seq in stop:
            return orf
            end = len(DNA) + 1  # This should end the while loop
        elif end <= len(DNA):
            orf = orf + seq  # increase the open reading frame by the next codon.
            start = start + 3
            end = end + 3
        elif end == len(DNA) and seq not in stop:
            end = len(DNA) + 1
            orf = ''
            # this is not an orf, so end the while loop and return nothing


def translate(orf, codon_dictionary):
    protein = ''
    x = 0
    y = 3
    if orf != None:
        while y <= len(orf):
            sub = orf[x:y]
            if sub in codon_dictionary:
                protein += codon_dictionary[sub]
                x += 3
                y += 3
        return protein



def reverse_complement(dna):
    revcom = dna[::-1]
    revcom = revcom.replace('A', 'Z')
    revcom = revcom.replace('C', 'Y')
    revcom = revcom.replace('G', 'C')
    revcom = revcom.replace('T', 'A')
    revcom = revcom.replace('Z', 'T')
    revcom = revcom.replace('Y', 'G')
    return revcom
# print revdna

def orf_prediction(dna_string):
    my_orfs = []
    string_list = [dna_string, reverse_complement(dna_string)]
    for dna in string_list:
        for position in find_start(dna):
            orf = orf_detection(position, dna)
            the_orf = (translate(orf, codon))
            if the_orf is not None:
                my_orfs.append(the_orf)
    return set(my_orfs)


if __name__ == '__main__':
    for orf in orf_prediction(dna):
        print orf