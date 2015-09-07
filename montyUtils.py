import random


class DoorState:
    Closed = 0
    Open = 1

class Door:
    State = DoorState.Closed
    HasPrize = False
    CurrentGuess = False

    def __init__(self):
        self.State = DoorState.Closed
        self.HasPrize = False
        self.CurrentGuess = False

class DoorSet:
    Door1 = Door()
    Door2 = Door()
    Door3 = Door()
    __doors = [Door1,Door2,Door3]

    def get_rnd(self):
        return random.choice([0,1,2])

    def __init__(self):
        Door1 = Door()
        Door2 = Door()
        Door3 = Door()
        __doors = [self.Door1, self.Door2, self.Door3]

        for d in range(3):
            self.__doors[d].CurrentGuess = False
            self.__doors[d].HasPrize = False
            self.__doors[d].State = DoorState.Closed

        winningdoor = self.get_rnd();
        self.__doors[winningdoor].HasPrize = True


    def place_guess(self, pos):
        for d in range(3):
            self.__doors[d].CurrentGuess = False
        self.__doors[pos].CurrentGuess = True

    def check_guess(self):
        for d in range(3):
            if self.__doors[d].CurrentGuess:
                return self.__doors[d].HasPrize

    def open_nonprize_door(self):
        rnddoor = self.get_rnd()
        while True:
            if not self.__doors[rnddoor].HasPrize and not self.__doors[rnddoor].CurrentGuess:
                self.__doors[rnddoor].State = DoorState.Open
                break
            else:
                rnddoor = self.get_rnd()

    def change_guess(self):
        pos = -1
        for d in range(3):
            if not self.__doors[d].CurrentGuess:
                if self.__doors[d].State == DoorState.Closed:
                    pos = d
        for d in range(3):
            self.__doors[d].CurrentGuess = False
        self.__doors[pos].CurrentGuess = True
