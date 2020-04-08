'''
You are given N lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.
'''

import re
if __name__ == "__main__":
    n = int(input())
    inp = []
    for i in range(0,n):
        inp.append(input().strip())
    search = []
    for line in inp:
        if re.findall(".(#[a-fA-F0-9]*)",line) != [] :
            search.append(re.findall(".(#[a-fA-F0-9]*)",line))
    for code_list in search:
        for code in code_list:
            print(code)