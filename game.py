import random

class TicTacToe:
    """Tic Tac Toe game's class."""
    
    def __init__(self):
        """Init of Tic Tac Toe game's object."""
        self._board = [i for i in range(9)]
        self._avaiablePlayers = ["X", "Y"]
        self._currentTurn = 0
    
    @property
    def board(self):
        return self._board[:]
    
    @property
    def currentTurn(self):
        return self._currentTurn
    
    def choicePlayerTurn(self):
        """This method sets the first turn of the game."""
        self._currentTurn = random.choice(self._avaiablePlayers)
    
    def changeTurn(self):
        """Change the current turn of players."""
        if self._currentTurn == self._avaiablePlayers[0]:
            self._currentTurn = self._avaiablePlayers[1]
        else:
            self._currentTurn = self._avaiablePlayers[0]

    def setPlace(self, place):
        """Method gets from players, a place where they want to set; if 
        the place is avaiable, method return True; against it's return False"""
        self._board[place] = self._currentTurn
         
    def getFreePlaces(self):
        return [i for i in self._board if type(i) == int]

    def checkWin(self):
        """Method returns True, if some user win the game; return False if not."""
        first = self._board[0] == self._board[1] == self._board[2]
        second = self._board[3] == self._board[4] == self._board[5]
        third = self._board[6] == self._board[7] == self._board[8]
        if first or second or third:
            return True
        first = self._board[0] == self._board[3] == self._board[6]
        second = self._board[1] == self._board[4] == self._board[7]
        third = self._board[2] == self._board[5] == self._board[8]
        if first or second or third:
            return True
        first = self._board[0] == self._board[4] == self._board[8]
        second = self._board[2] == self._board[4] == self._board[6]
        if first or second:
            return True
        
        return False