from montyUtils import *
import random

numTests = 100000
totalFirst = 0
totalSecond = 0
totalGuesses = 0
winFirst = 0
lostFirst = 0
winSecond = 0
lostSecond = 0
def collect_info(firstGuess, correctGuess):
    global totalGuesses
    global totalFirst
    global totalSecond
    global winFirst
    global lostFirst
    global winSecond
    global lostSecond

    totalGuesses += 1

    if firstGuess and correctGuess:
        winFirst = winFirst + 1
        totalFirst += 1
    elif firstGuess and not correctGuess:
        lostFirst = lostFirst + 1
        totalFirst += 1
    elif not firstGuess and correctGuess:
        winSecond = winSecond + 1
        totalSecond += 1
    elif not firstGuess and not correctGuess:
        lostSecond = lostSecond + 1
        totalSecond += 1

    if totalGuesses == numTests:

        print('-------------------------------\n#' + str(totalGuesses) + ' iterations done')
        print(str((winFirst / totalFirst) * 100.0) + "% wins on first guess")
        print(str((lostFirst / totalFirst) * 100.0) + "% losses on first guess")
        print('\n')
        print(str((winSecond / totalSecond) * 100.0) + "% wins on second guess")
        print(str((lostSecond / totalSecond) * 100.0) + "% losses on second guess")

print('Running...')
for i in range(numTests):
    doorSet = DoorSet()

    firstGuess = doorSet.get_rnd()
    doorSet.place_guess(firstGuess)
    doorSet.open_nonprize_door()

    choise = totalGuesses % 2 == 0 # random.choice([True,False])
    if choise:
        doorSet.change_guess()
        win = doorSet.check_guess()
        collect_info(False, win)
    else:
        win = doorSet.check_guess()
        collect_info(True, win)
