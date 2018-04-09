# ACSL 2017-2018 Intermediate Division
# Contest No.3
# Pittsford Sutherland High School
# Simon Narang

# --------------IMPORTANT-------------
# ONLY RUN WITH PYTHON 3,NOT PYTHON 2

inputProcessed = []
inputOriginal = []

def simulateGame():
    processInput(input())
    for i in range(1, 6):
        walk(input())

def processInput(input):
    global inputProcessed
    global inputOriginal
    input = input.split(',')
    for i in input:
        i = bin(int(i, 16))[2:].zfill(8)
        iProcessed = []
        for b in i:
            iProcessed.append([b, 90])
        inputProcessed.append(iProcessed)
    inputOriginal = inputProcessed

class Walkman:
    global inputProcessed
    posPrev = []
    posCurrent = []

    def __init__(self, posInit):
        self.posCurrent = posInit

    def updatePos(self, posNew):
        global inputProcessed
        self.posPrev = self.posCurrent
        self.posCurrent = posNew

    def continueFwd(self, deg):
        global inputProcessed
        if deg == 90:
            if self.posCurrent[0] > self.posPrev[0]:
                self.updatePos((self.posCurrent[0] - 1, self.posCurrent[1]))
            elif self.posCurrent[0] < self.posPrev[0]:
                self.updatePos((self.posCurrent[0], self.posCurrent[1]  - 1))
            elif self.posCurrent[1] > self.posPrev[1]:
                self.updatePos((self.posCurrent[0], self.posCurrent[1] - 1))
            elif self.posCurrent[1] < self.posPrev[1]:
                self.updatePos((self.posCurrent[0], self.posCurrent[1] + 1))
        elif deg == 180:
            if self.posCurrent[0] > self.posPrev[0]:
                self.updatePos((self.posCurrent[0]  - 1, self.posCurrent[1]))
            elif self.posCurrent[0] < self.posPrev[0]:
                self.updatePos((self.posCurrent[0]  + 1, self.posCurrent[1]))
            elif self.posCurrent[1] > self.posPrev[1]:
                self.updatePos((self.posCurrent[0], self.posCurrent[1] + 1))
            elif self.posCurrent[1] < self.posPrev[1]:
                self.updatePos((self.posCurrent[0], self.posCurrent[1] - 1))
        elif deg == 270:
            if self.posCurrent[0] > self.posPrev[0]:
                self.updatePos((self.posCurrent[0], self.posCurrent[1] - 1))
            elif self.posCurrent[0] < self.posPrev[0]:
                self.updatePos((self.posCurrent[0], self.posCurrent[1] + 1))
            elif self.posCurrent[1] > self.posPrev[1]:
                self.updatePos((self.posCurrent[0] + 1, self.posCurrent[1]))
            elif self.posCurrent[1] < self.posPrev[1]:
                self.updatePos((self.posCurrent[0] - 1, self.posCurrent[1]))
        elif deg == 360:
            if self.posCurrent[0] > self.posPrev[0]:
                self.updatePos((self.posCurrent[0]  + 1, self.posCurrent[1]))
            elif self.posCurrent[0] < self.posPrev[0]:
                self.updatePos((self.posCurrent[0]  - 1, self.posCurrent[1]))
            elif self.posCurrent[1] > self.posPrev[1]:
                self.updatePos((self.posCurrent[0], self.posCurrent[1] - 1))
            elif self.posCurrent[1] < self.posPrev[1]:
                self.updatePos((self.posCurrent[0], self.posCurrent[1] + 1))

        if self.posCurrent[0] > 8:
            self.posCurrent = (1, self.posCurrent[1])

        if self.posCurrent[1] > 8:
            self.posCurrent = (self.posCurrent[0], 1)

        if self.posCurrent[0] < 1:
            self.posCurrent = (8, self.posCurrent[1])

        if self.posCurrent[1] < 1:
            self.posCurrent = (self.posCurrent[0], 8)

    def walk(self, dir, count):
        global inputProcessed
        for i in range(0, count):
            if i == 0:
                if dir == 'A':
                    self.posPrev = (self.posCurrent[0] - 1, self.posCurrent[1])
                elif dir == 'B':
                    self.posPrev = (self.posCurrent[0] + 1, self.posCurrent[1])
                elif dir == 'L':
                    self.posPrev = (self.posCurrent[0], self.posCurrent[1] - 1)
                elif dir == 'R':
                    self.posPrev = (self.posCurrent[0], self.posCurrent[1] + 1)

            if inputProcessed[self.posCurrent[0] - 1][self.posCurrent[1] - 1][0] == '1':
                self.continueFwd(inputProcessed[self.posCurrent[0] - 1][self.posCurrent[1] - 1][1])
                inputProcessed[self.posCurrent[0] - 1][self.posCurrent[1] - 1][1] += 90
            else:
                self.continueFwd(180)
        posFinal = str(self.posCurrent[0]) + ',' + str(self.posCurrent[1])
        print(posFinal)


def walk(input):
    global inputProcessed
    global inputOriginal
    input = input.split(',')
    paulWalker = Walkman((int(input[0]), int(input[1])))
    paulWalker.walk(input[2], int(input[3]))
    inputProcessed = inputOriginal

simulateGame()
