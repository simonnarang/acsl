# ACSL 2017-2018 Intermediate Division
# Contest No.1
# Pittsford Sutherland High School
# Simon Narang

# --------------IMPORTANT-------------
# ONLY RUN WITH PYTHON 3, NOT PYTHON 2

cards = [int]
playerDeck = []
playerScore = 0
playerPlayed = 0
dealerScore = 0
dealerPlayed = 0
score = 0

def reset():
    global cards
    global playerDeck
    global playerScore
    global dealerScore
    global dealerPlayed
    global playerPlayed
    global score
    cards = [int]
    playerDeck = []
    playerScore = 0
    dealerScore = 0
    playerPlayed = 0
    dealerPlayed = 0
    score = 0

def isInt(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def processInput(input):
    global cards
    global score
    input = input.split(', ')
    score = int(input[0])
    input = input[1:]
    for i in range(0, 10):
        if isInt(input[i]):
            cards.append(int(input[i]))
        else:
            if input[i] == 'T':
                cards.append(10)
            if input[i] == 'J':
                cards.append(11)
            if input[i] == 'Q':
                cards.append(12)
            if input[i] == 'K':
                cards.append(13)
            if input[i] == 'A':
                cards.append(14)
    cards = cards[1:]

def updateTotalScore(card):
    global score
    if card == 10:
        score -= 10
    elif card == 9:
        score = score
    elif card == 14:
        if score + 14 >= 99:
            score += 1
        else:
            score += 14
    else:
        score += card

def updatePlayerScore():
    global cards
    global playerScore
    global playerDeck
    global dealerScore
    global score
    global playerPlayed
    global dealerPlayed
    global dealer

    if playerDeck == []:
        playerDeck = (cards[:3])
        cards = cards[3:]
    else:
        playerCardDown = max(playerDeck)
        playerDeck.remove(playerCardDown)
        if score + playerCardDown <= 99:
            if playerCardDown == 9:
                playerScore = playerScore
            elif playerCardDown == 14:
                if score + 14 >= 99:
                    playerScore += 1
                else:
                    playerScore += 14
            elif playerCardDown == 10:
                playerScore += playerCardDown
            else:
                playerScore += playerCardDown
        playerDeck.append(cards[:1][0])
        cards = cards[1:]
        updateTotalScore(playerCardDown)
        playerPlayed += 1
        if score <= 99:
            dealerCardDown = cards[0]
            if score + dealerCardDown <= 99:
                if dealerCardDown == 9:
                    dealerCardDown = dealerCardDown
                elif dealerCardDown == 14:
                    if score + 14 >= 99:
                        dealerScore += 1
                    else:
                        dealerScore += 14
                elif dealerCardDown == 10:
                    dealerScore += dealerCardDown
                else:
                    dealerScore += dealerCardDown
            cards= cards[1:]
            updateTotalScore(dealerCardDown)
            dealerPlayed += 1

def simulateGame():
    for i in range(0, 5):
        processInput(input())
        while score <= 99:
            updatePlayerScore()
        if playerPlayed > dealerPlayed:
            print(str(score) + ', dealer')
        else:
            print(str(score) + ', player')
        reset()

simulateGame()
