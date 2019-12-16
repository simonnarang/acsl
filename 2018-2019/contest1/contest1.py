# Simon's ACSL Contest No.1 response - enjoy!
# Kindly please only run with Python3

for _ in range(5):
    inp = input().split(' ')
    line = list(map(int, str(inp[0])))
    r = int(inp[1])
    sum = 0
    for i in range(len(line)):
        try:
            scapegoat = line[i+r-1]
            sum += int(''.join([str(elem) for elem in line[i:i+r] ]))
        except IndexError: scapegoat = 'persecuted'
    print(sum)