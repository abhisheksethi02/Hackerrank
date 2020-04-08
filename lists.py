if __name__ == "__main__":
    n = int(input())
    ls = []
    def opcode(inp,ls):
        check = inp.split()
        call_funcs = {
            'insert' : ls.insert(int(check[1]),check[2]),
            'print' : print(ls),
            'remove' : ls.remove(check[1]),
            'append' : ls.append(check[1]),
            'sort' : ls.sort(),
            'pop' : ls.pop(),
            'reverse' : ls.sort(reverse = True),
                }
        func = call_funcs.get(check[0],'Invalid Command')
        return ls
    for i in range(n):
        comm = input()
        ls = opcode(comm,ls)
