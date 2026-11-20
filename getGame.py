import random
import webbrowser
from time import sleep

def randomNumber(limit):
    return random.randrange(0,limit,1)

def parseInput(rawInput):
    lines = rawInput.split('\n')

    games = []
    for line in lines:

        if not line.strip():
            continue

        words = line.split(' ')
        id = words[0]
        if len(words) >= 2:
            name = " ".join(words[1:])
        else:
            name = "Unknown"
        games.append({"id":id,"name":name})

    return games

def playAnimation(games,limit):
    ROLL_COUNT = 7
    for i in range(ROLL_COUNT):
        print(games[random.randrange(0,limit,1)]["name"])
        sleep(0.33)


if __name__ == "__main__":
    rawText = open("gameIds.txt", 'r').read()

    games = parseInput(rawText)
    idCount = len(games)
    chosenGame = games[randomNumber(idCount)]

    playAnimation(games,idCount)
    print("\n YOUR GAME IS...\n",chosenGame["name"])
    sleep(1)
    webbrowser.open(f"roblox://experiences/start?placeId={chosenGame['id']}")


