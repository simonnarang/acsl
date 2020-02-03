inputText = open('int-sample-input.txt', 'r')
for l in inputText:
    n, p = l.split('  ')
    # Make p left-indexed instead of right-indexed.. more intuitive
    p = len(n) - int(p)
    c_p = int(n[p])
    output = list(n)
    for i in range(len(n)):
        c = int(n[i])
        if i < p:
            output[i] = str(c_p+c)[-1]
        if i > p:
            output[i] = str(abs(c-c_p))[-1]
    print(''.join(output))