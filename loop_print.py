'''
Read an integer .

Without using any string methods, try to print the following:


Note that "" represents the values in between.
'''

if __name__ == "__main__":
    inp = input()
    n = int(inp)
    out = ''
    for i in range(1,n+1):
        out = out + str(i)
    print(out)