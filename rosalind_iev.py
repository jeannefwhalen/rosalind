# coding=utf-8
"""
Problem
For a random variable X taking integer values between 1 and n the expected value of X is E(X)=SUM(nk)=1k×Pr(X=k). The
expected value offers us a way of taking the long-term average of a random variable over a large number of trials.
As a motivating example, let X be the number on a six-sided die. Over a large number of rolls, we should expect to
obtain an average of 3.5 on the die (even though it's not possible to roll a 3.5). The formula for expected value
confirms that E(X)=SUM(6k=1k×Pr(X=k))=3.5
More generally, a random variable for which every one of a number of equally spaced outcomes has the same probability is
called a uniform random variable (in the die example, this "equal spacing" is equal to 1). We can generalize our die
example to find that if X is a uniform random variable with minimum possible value a and maximum possible value b,
then E(X)=a+b2. You may also wish to verify that for the dice example, if Y
Y is the random variable associated with the outcome of a second die roll, then E(X+Y)=7

Given:
Six positive integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a
population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of
couples having the following genotypes:
AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa

Return:
The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that
every couple has exactly two offspring.

Sample Dataset
1 0 0 1 0 1

Sample Output

3.5
"""
from sys import argv

script, hdhd, hdhet, hdhr, hethet, hethr, hrhr = argv

def count_offspring(a,b,c,d,e,f):
    #P(dominant phenotype) * number of couples mating * number of offspring
    a_count = 1 * float(a) * 2.0 #P(dominant from HD_HD) = 100%
    b_count = 1 * float(b) * 2.0 #P(dominant from HD_Het) = 100%
    c_count = 1 * float(c) * 2.0 #P(dominant from HD_HR) = 100%
    d_count = 0.75 * float(d) * 2.0 #P(dominant from Het_Het) = 75%
    e_count = 0.5 * float(e) * 2.0 #P(dominant from Het_HR) = 50%
    f_count = 0.0 * float(f) * 2.0 #P(dominant from HR_HR) = 0%
    return a_count + b_count + c_count + d_count + e_count + f_count


if __name__ == '__main__':
    print count_offspring(hdhd, hdhet, hdhr, hethet, hethr, hrhr)