"""
Problem
For example, say that we have a bag containing 3 red balls and 2 blue balls. If we let X represent the random variable
corresponding to the color of a drawn ball, then the probability of each of the two outcomes is given by Pr(X=red)=35
and Pr(X=blue)=25.

Random variables can be combined to yield new random variables. Returning to the ball example, let Y
model the color of a second ball drawn from the bag (without replacing the first ball). The probability of Y
being red depends on whether the first ball was red or blue. To represent all outcomes of X and Y, we therefore use a
probability tree diagram. This branching diagram represents all possible individual probabilities for X and Y, with
outcomes at the endpoints ("leaves") of the tree. The probability of any outcome is given by the product of
probabilities along the path from the beginning of the tree.

An event is simply a collection of outcomes. Because outcomes are distinct, the probability of an event can be written
as the sum of the probabilities of its constituent outcomes. For our colored ball example, let A be the event "Y is
blue." Pr(A) is equal to the sum of the probabilities of two different outcomes:
Pr(X=blue and Y=blue)+Pr(X=red and Y=blue), or 310+110=25


Given:
Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous
dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return:
The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele
(and thus displaying the dominant phenotype). Assume that any two organisms can mate.

Sample Dataset
2 2 2

Sample Output
0.78333
"""
#
from sys import argv
script, k, m, n = argv

def mendel(hd, het, hr):
    hd = float(hd)
    het = float(het)
    hr = float(hr)
    pop = hd+hr+het
    recessive_pop = (hr/pop) * ((hr-1)/(pop-1))
    hetero_pop = ((het/pop) * ((het-1)/(pop-1)))
    het_rec = ((het/pop) * (hr/(pop-1))) + ((hr/pop) * (het/(pop-1)))
    p = recessive_pop + (hetero_pop*0.25) + (het_rec*0.5)
    return 1-p

if __name__ == '__main__':
    print mendel(k, m, n)
