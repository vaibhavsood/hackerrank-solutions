if __name__ == '__main__':
    N = int(input())
    res = []
    for _ in range(N):
        cmd = input().split(' ')
        op = cmd[0]
        args = cmd[1:]
        if cmd[0] != 'print':
            eval("res."+op+"("+",".join(args)+")")
        else:
            print(res)
