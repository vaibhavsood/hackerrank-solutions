n, m = map(int, input().split(' '))
bar = 1
for i in range(n):
    if i == int(n/2):
        dash = (m-7)/2
        print('-'*int(dash)+'WELCOME'+'-'*int(dash))
        bar += 2
    else:
        if i < n/2:
            if i == 0:
                bar = 1
            else:
                bar += 2
        else:
            bar -= 2
        dash = (m-(bar*3))/2
        print('-'*int(dash)+'.|.'*bar+'-'*int(dash))
