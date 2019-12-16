# Simon's ACSL Contest No.4 response 2019—enjoy!
# Kindly please only run with Python3

class Desmos:
    def __init__ (self):
        self.stack = []

    def push (self, p):
        if p in ['+', '-', '*', '/']:
            op1 = self.stack.pop()
            op2 = self.stack.pop()
            self.stack.append('(%s %s %s)' % (op1, p, op2) )
        elif p == '!':
            op = self.stack.pop()
            self.stack.append('%s!' % (op) )
        elif p in ['sin', 'cos', 'tan']:
            op = self.stack.pop()
            self.stack.append('%s(%s)' % (p, op) )
        elif p == '>':
            op1 = self.stack.pop()
            op2 = self.stack.pop()
            op3 = self.stack.pop()
            num = str(max(eval(op1), eval(op2), eval(op3)))
            self.stack.append(num)
        elif p == '@':
            op1 = self.stack.pop()
            op2 = self.stack.pop()
            op3 = self.stack.pop()
            if int(eval(op1)) > 0: self.stack.append(op2)
            else: self.stack.append(op3)
        else:
            self.stack.append(p)

    def convert (self, l):
        l.reverse()
        for e in l:
            self.push(e)
        return self.stack.pop()

c = Desmos()

for _ in range(5):
    inp = input().split(' ')
    print(eval(c.convert(inp)))