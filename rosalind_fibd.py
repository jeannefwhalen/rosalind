# coding=utf-8
"""
Problem


Figure 4. A figure illustrating the propagation of Fibonacci's rabbits if they die after three months.
Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence
relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of
offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all
rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for
three months (meaning that they reproduce only twice before dying).

Given:
Positive integers n≤100 and m≤20.

Return:
The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

Sample Dataset
6 3

Sample Output
4
"""

from sys import argv

script, months, months_alive = argv

n = int(months)
m = int(months_alive)

def fibd(num_months, alive_months):
    total_list = []
    total = 0
    i = 0 #this is an index, when i = 1 this is F(2)
    j = 1
    x = 1 ##x keeps track of the month
    while x <= n:
        if x == 1: #month 1 is baby rabbits to start
            total_list.append(1)
        elif x == 2: #month 2 is mature rabbits
            total_list.append(1)
        elif x > 2 and x <= m: #the rabbits start to mate
            total = total_list[i] + total_list[j]
            total_list.append(total)
            i = i + 1
            j = j + 1
        elif x > m: #x is greater than the lifespan of rabbits, one pair will be gone each month
            ##needed a little help on this part. understood completely now. Equation changes
            ##once rabbits start dying.
            rabbits = 0
            for t in range(x-m, x-1):
                rabbits = rabbits + total_list[t-1]
            total_list.append(rabbits)
            i = i + 1
            j = j + 1
        x = x + 1
    return total_list[-1]


if __name__ == '__main__':
    print fibd(n,m)