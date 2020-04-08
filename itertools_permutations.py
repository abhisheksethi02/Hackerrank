'''
This tool returns successive r length permutations of elements in an iterable.
If r is not specified or is None, then r defaults to the length of the iterable, 
and all possible full length permutations are generated.
Permutations are printed in a lexicographic sorted order. 
So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.
'''

from itertools import permutations as pm
inp = input().split()
string = inp[0]
try:
    n = int(inp[1])
except:
    n = len(string)
list_req = sorted(list(pm(string,n)))
for tp in list_req:
    output = ''
    for value in tp:
        output = output + value
    print(output)
