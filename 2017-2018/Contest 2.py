# ACSL 2017-2018 Intermediate Division
# Contest No.2
# Pittsford Sutherland High School
# Simon Narang

# --------------IMPORTANT-------------
# ONLY RUN WITH PYTHON 3, NOT PYTHON 2
paranthesisOpen = 0
paranthesisClose = 0
hardBracketsOpen = 0
hardBracketsClose = 0
locations = []
operators = ["+", "-", "*", "/"]

def processInput(input):
    global paranthesisOpen
    global paranthesisClose
    global hardBracketsOpen
    global hardBracketsClose

    for c in input:
        if c == "(":
            paranthesisOpen += 1
        if c == ")":
            paranthesisClose += 1
        if c == "[":
            hardBracketsOpen += 1
        if c == "]":
            hardBracketsClose += 1

    if paranthesisOpen - paranthesisClose > 0:
        addEnclosure(0, input)
    elif paranthesisOpen - paranthesisClose < 0:
        addEnclosure(1, input)
    elif hardBracketsOpen - hardBracketsClose < 0:
        addEnclosure(2, input)
    elif hardBracketsOpen - hardBracketsClose > 0:
        addEnclosure(3, input)

def addEnclosure(missingEnclosure, input):
    if missingEnclosure == 0:
        openParenthesis = 0
        closedBracket = len(input)
        for i, c in enumerate(input):
            if c == "(":
                openParenthesis = i
            elif c == "]":
                closedBracket = i
        for i, c in enumerate(input):
            if (i + 1) == len(input):
                if (isInt(input[i]
                and i < (closedBracket - 1))):
                    locations.append(i + 2)
            else:
                if (not c in operators
                and i < closedBracket
                and i > (openParenthesis + 1)
                and not isInt(input[i + 1])):
                    locations.append(i + 2)
        printLocations(locations)

    if missingEnclosure == 1:
        openBracket = 0
        closedParenthesis = len(input)
        for i, c in enumerate(input):
            if c == "[":
                openBracket = i
            elif c == ")":
                closedParenthesis = i
        for i, c in enumerate(input):
            if (not c in operators and i > openBracket and i < (closedParenthesis - 1)):
                locations.append(i + 1)
        printLocations(locations)


    if missingEnclosure == 2:
        openParenthesis = 0
        for i, c in enumerate(input):
            if c == "(":
                openParenthesis = i
        for i, c in enumerate(input):
            if (not c in operators and i <= openParenthesis):
                locations.append(i + 1)
        printLocations(locations)

    if missingEnclosure == 3:
        closedParenthesis = len(input)
        for i, c in enumerate(input):
            if c == ")":
                closedParenthesis = i
        for i, c in enumerate(input):
            if (i + 1) == len(input):
                locations.append(i + 2)
            else:
                if (not c in operators
                and i >= closedParenthesis
                and not isInt(input[i + 1])):
                    locations.append(i + 2)
        printLocations(locations)

def printLocations(locations):
    for i, l in enumerate(locations):
        if i == (len(locations) - 1):
            print(l)
        else:
            print(str(l) + ", ", end="")

def isInt(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def simulateGame():
    global paranthesisOpen
    global paranthesisClose
    global hardBracketsOpen
    global hardBracketsClose
    global locations
    for i in range(0, 5):
        processInput(input())
        paranthesisOpen = 0
        paranthesisClose = 0
        hardBracketsOpen = 0
        hardBracketsClose = 0
        locations = []

simulateGame()
