from colorama import Fore, Back, Style, init

class ChessPlayer:    
    def __init__(self, color:str):
        self.color : str = color.lower()
        if self.color == "white":
            self.startpoint : str = "1a"
            self.endpoint : str = "2h"
        elif self.color == "black":
            self.startpoint : str = "8a"
            self.endpoint : str = "7h"
        else:
            raise Exception
    def isAvailable(self, place:str, player1Positions: list[str], player2Positions: list[str]):
        """Function that evaluates if a place is free

        Args:
            place (str): Place of chess (ej. "2a")
            player1Positions list[str]: List of Positions of Player1
            player2Positions list[str]: List of Positions of Player2

        Returns:
            int: 0 if not available, 1 if available and 2 if there is a piece of the second player
        """
        #player2.getPositions()
        try:
            if int(place[0]) < 9 and int(place[0]) > 0:
                if ord(place[1])<105 and ord(place[1])>96:
                    if place in player1Positions: return 0
                    elif place in player2Positions: return 2
                    else: return 1
                else: return 0
            else: return 0
        except:
            return 0
    def createPlayer(self):
        self.listOfPawns : list[Pawns] = [Pawns(self.color, str(self.endpoint[0])+chr(ord("a")+i)) for i in range(8)]
        self.listOfRoocks : list[Rooks] = [Rooks(self.color, str(self.startpoint[0])+chr(ord("a")+i)) for i in range(0,8,7)]
        self.listOfKnights : list[Knights] = [Knights(self.color, str(self.startpoint[0])+chr(ord("a")+i)) for i in range(1,8,5)]
        self.listOfBishops : list[Bishop] = [Bishop(self.color, str(self.startpoint[0])+chr(ord("a")+i)) for i in range(2,8,3)]
        self.Queen : Queen = Queen(self.color, str(self.startpoint[0])+chr(ord("a")+3))
        self.King : King = King(self.color, str(self.startpoint[0])+chr(ord("a")+4))
    def getPositions(self):
        self.table = [[f"{i+1}"+chr(ord("a")+j) for i in range(8)] for j in range(8)]
        self.pawnsPositions = [i.getPos() for i in self.listOfPawns]
        self.roocksPositions = [i.getPos() for i in self.listOfRoocks]
        self.knightsPositions = [i.getPos() for i in self.listOfKnights]
        self.bishopsPositions = [i.getPos() for i in self.listOfBishops]
        self.queenPosition = [self.Queen.getPos()]
        self.kingPosition = [self.King.getPos()]
        self.Positions = self.pawnsPositions + self.roocksPositions + self.knightsPositions + self.bishopsPositions + self.queenPosition + self.kingPosition
        return self.Positions
    def printTable(self, player2):
        self.table = [[f"{i+1}"+chr(ord("a")+j) for i in range(8)] for j in range(8)]
        self.table1 = self.getPositions()
        self.table2 = player2.getPositions()
        for i in self.table:
            for j in i:
                if j in self.Positions or j in player2.Positions:
                    if j in self.pawnsPositions : self.table[self.table.index(i)][i.index(j)] = Fore.GREEN + 'P'
                    elif j in player2.pawnsPositions : self.table[self.table.index(i)][i.index(j)] = Fore.RED + 'P'
                    elif j in self.roocksPositions : self.table[self.table.index(i)][i.index(j)] = Fore.GREEN + "R"
                    elif j in player2.roocksPositions : self.table[self.table.index(i)][i.index(j)] = Fore.RED + "R"
                    elif j in self.knightsPositions : self.table[self.table.index(i)][i.index(j)] = Fore.GREEN + "N"
                    elif j in player2.knightsPositions : self.table[self.table.index(i)][i.index(j)] = Fore.RED + "N"
                    elif j in self.bishopsPositions : self.table[self.table.index(i)][i.index(j)] = Fore.GREEN + "B"
                    elif j in player2.bishopsPositions : self.table[self.table.index(i)][i.index(j)] = Fore.RED + "B"
                    elif j in self.queenPosition : self.table[self.table.index(i)][i.index(j)] = Fore.GREEN + "Q"
                    elif j in player2.queenPosition : self.table[self.table.index(i)][i.index(j)] = Fore.RED + "Q"
                    elif j in self.kingPosition : self.table[self.table.index(i)][i.index(j)] = Fore.GREEN + "K"
                    elif j in player2.kingPosition : self.table[self.table.index(i)][i.index(j)] = Fore.RED + "K"
                else:
                    self.table[self.table.index(i)][i.index(j)] = Fore.BLACK + self.table[self.table.index(i)][i.index(j)]
        print(Fore.YELLOW + "\t".join([" ", "a", "b", "c", "d", "e", "f", "g", "h"]), end="\n")
        for i in range(8):
            for j in range(8):
                if j == 0 and self.color == "white":
                    print(Fore.YELLOW + str(8-i), end="\t")
                elif j == 0 and self.color == "black":
                    print(Fore.YELLOW + str(i+1), end="\t")
                if self.color == "white":
                    print(self.table[j][7-i], end="\t")
                else:
                    print(self.table[j][i], end="\t")
            print("\n")
    def movPiece(self, fromPlace:str, toPlace:str, player2):
        possibleMoves = []
        player1Positions = self.getPositions()
        player2Positions = player2.getPositions()
        if fromPlace not in self.Positions:
            return False
        else:
            if fromPlace in self.pawnsPositions:
                possibleMoves = self.listOfPawns[self.pawnsPositions.index(fromPlace)].getPossiblesMoves(player1Positions, player2Positions)
            elif fromPlace in self.roocksPositions:
                possibleMoves = self.listOfRoocks[self.roocksPositions.index(fromPlace)].getPossiblesMoves(player1Positions, player2Positions)
            elif fromPlace in self.bishopsPositions:
                possibleMoves = self.listOfBishops[self.bishopsPositions.index(fromPlace)].getPossiblesMoves(player1Positions, player2Positions)
            elif fromPlace in self.knightsPositions:
                possibleMoves = self.listOfKnights[self.knightsPositions.index(fromPlace)].getPossiblesMoves(player1Positions, player2Positions)
            elif fromPlace == self.queenPosition[0]:
                possibleMoves = self.Queen.getPossiblesMoves(player1Positions, player2Positions)
            elif fromPlace == self.kingPosition[0]:
                possibleMoves = self.King.getPossiblesMoves(player1Positions, player2Positions)
        if toPlace in possibleMoves:
            if fromPlace in self.pawnsPositions:
                possibleMoves = self.listOfPawns[self.pawnsPositions.index(fromPlace)].changePlace(toPlace, player2)
            elif fromPlace in self.roocksPositions:
                possibleMoves = self.listOfRoocks[self.roocksPositions.index(fromPlace)].changePlace(toPlace, player2)
            elif fromPlace in self.bishopsPositions:
                possibleMoves = self.listOfBishops[self.bishopsPositions.index(fromPlace)].changePlace(toPlace, player2)
            elif fromPlace in self.knightsPositions:
                possibleMoves = self.listOfKnights[self.knightsPositions.index(fromPlace)].changePlace(toPlace, player2)
            elif fromPlace == self.queenPosition[0]:
                possibleMoves = self.Queen.changePlace(toPlace, player2)
            elif fromPlace == self.kingPosition[0]:
                possibleMoves = self.King.changePlace(toPlace, player2)
            return True
        else:
            return False
    def changePlace(self, place, player2):
        player2Positions = player2.getPositions()
        if place in player2Positions:
            if place in player2.pawnsPositions:
                self.pos = place
                player2.listOfPawns[player2.pawnsPositions.index(place)].pos = "X"
            elif place in player2.roocksPositions:
                self.pos = place
                player2.listOfRoocks[player2.roocksPositions.index(place)].pos = "X"
            elif place in player2.bishopsPositions:
                self.pos = place
                player2.listOfBishops[player2.bishopsPositions.index(place)].pos = "X"
            elif place in player2.knightsPositions:
                self.pos = place
                player2.listOfKnights[player2.knightsPositions.index(place)].pos = "X"
            elif place in player2.queenPosition[0]:
                self.pos = place
                player2.Queen.pos = "X"
            elif place in player2.kingPosition[0]:
                self.pos = place
                player2.King.pos = "X"
        else:
            self.pos = place
class Pawns(ChessPlayer):
    def __init__(self, color:str, pos:str):
        super().__init__(color)
        self.pos : str = pos
    def getPos(self):
        return self.pos
    def getPossiblesMoves(self, player1Positions, player2Positions):
        listMoves = []
        if self.color == "white":
            if self.pos[0] == "2":
                listMoves.append(str(int(self.pos[0])+2)+chr(ord(self.pos[1])))
            if self.isAvailable(str(int(self.pos[0])+1)+chr(ord(self.pos[1])+1), player1Positions, player2Positions) == 2:
                listMoves.append(str(int(self.pos[0])+1)+chr(ord(self.pos[1])+1))
            if self.isAvailable(str(int(self.pos[0])+1)+chr(ord(self.pos[1])-1), player1Positions, player2Positions) == 2:
                listMoves.append(str(int(self.pos[0])+1)+chr(ord(self.pos[1])-1))
            if self.isAvailable(str(int(self.pos[0])+1)+self.pos[1], player1Positions, player2Positions) == 1 and len(listMoves) == 0:
                listMoves.append(str(int(self.pos[0])+1)+chr(ord(self.pos[1])))
            return listMoves
        if self.color == "black":
            if self.pos[0] == "7":
                listMoves.append(str(int(self.pos[0])-2)+chr(ord(self.pos[1])))
            if self.isAvailable(str(int(self.pos[0])-1)+chr(ord(self.pos[1])+1), player1Positions, player2Positions) == 2:
                listMoves.append(str(int(self.pos[0])-1)+chr(ord(self.pos[1])+1))
            if self.isAvailable(str(int(self.pos[0])-1)+chr(ord(self.pos[1])-1), player1Positions, player2Positions) == 2:
                listMoves.append(str(int(self.pos[0])-1)+chr(ord(self.pos[1])-1))
            if self.isAvailable(str(int(self.pos[0])-1)+self.pos[1], player1Positions, player2Positions) == 1 and len(listMoves) == 0:
                listMoves.append(str(int(self.pos[0])-1)+chr(ord(self.pos[1])))
            return listMoves
class Bishop(ChessPlayer):
    def __init__(self, color:str, pos:str):
        super().__init__(color)
        self.pos : str = pos
    def getPos(self):
        return self.pos
    def getPossiblesMoves(self, player1Positions : list[str], player2Positions : list[str]):
        upRight = True
        upLeft = True
        downRight = True
        downLeft = True
        listMoves = []
        for i in range(1, 9):
            if upRight:
                if self.isAvailable(str(int(self.pos[0])+i) + chr(ord(self.pos[1])+i), player1Positions, player2Positions) == 1:
                    listMoves.append(str(int(self.pos[0])+i) + chr(ord(self.pos[1])+i))
                elif self.isAvailable(str(int(self.pos[0])+i) + chr(ord(self.pos[1])+i), player1Positions, player2Positions) == 2:
                    listMoves.append(str(int(self.pos[0])+i) + chr(ord(self.pos[1])+i))
                    upRight = False
                else:
                    upRight = False
            if downLeft:
                if self.isAvailable(str(int(self.pos[0])-i) + chr(ord(self.pos[1])-i), player1Positions, player2Positions) == 1:
                    listMoves.append(str(int(self.pos[0])-i) + chr(ord(self.pos[1])-i))
                elif self.isAvailable(str(int(self.pos[0])-i) + chr(ord(self.pos[1])-i), player1Positions, player2Positions) == 2:
                    listMoves.append(str(int(self.pos[0])-i) + chr(ord(self.pos[1])-i))
                    downLeft = False
                else:
                    downLeft = False
            if upLeft:
                if self.isAvailable(str(int(self.pos[0])+i) + chr(ord(self.pos[1])-i), player1Positions, player2Positions) == 1:
                    listMoves.append(str(int(self.pos[0])+i) + chr(ord(self.pos[1])-i))
                elif self.isAvailable(str(int(self.pos[0])+i) + chr(ord(self.pos[1])-i), player1Positions, player2Positions) == 2:
                    listMoves.append(str(int(self.pos[0])+i) + chr(ord(self.pos[1])-i))
                    upLeft = False
                else:
                    upLeft = False
            if downRight:
                if self.isAvailable(str(int(self.pos[0])-i) + chr(ord(self.pos[1])+i), player1Positions, player2Positions) == 1:
                    listMoves.append(str(int(self.pos[0])-i) + chr(ord(self.pos[1])+i))
                elif self.isAvailable(str(int(self.pos[0])-i) + chr(ord(self.pos[1])+i), player1Positions, player2Positions) == 2:
                    listMoves.append(str(int(self.pos[0])-i) + chr(ord(self.pos[1])+i))
                    downRight = False
                else:
                    downRight = False
        return listMoves
class Knights(ChessPlayer):
    def __init__(self, color:str, pos:str):
        super().__init__(color)
        self.pos : str = pos
    def getPos(self):
        return self.pos
    def getPossiblesMoves(self, player1Positions, player2Positions):
        listMoves = []
        if self.isAvailable(str(int(self.pos[0])+1)+chr(ord(self.pos[1])+2), player1Positions, player2Positions):
            listMoves.append(str(int(self.pos[0])+1)+chr(ord(self.pos[1])+2))
        if self.isAvailable(str(int(self.pos[0])+1)+chr(ord(self.pos[1])-2), player1Positions, player2Positions):
            listMoves.append(str(int(self.pos[0])+1)+chr(ord(self.pos[1])-2))
        if self.isAvailable(str(int(self.pos[0])-1)+chr(ord(self.pos[1])+2), player1Positions, player2Positions):
            listMoves.append(str(int(self.pos[0])-1)+chr(ord(self.pos[1])+2))
        if self.isAvailable(str(int(self.pos[0])-1)+chr(ord(self.pos[1])-2), player1Positions, player2Positions):
            listMoves.append(str(int(self.pos[0])-1)+chr(ord(self.pos[1])-2))
        if self.isAvailable(str(int(self.pos[0])+2)+chr(ord(self.pos[1])+1), player1Positions, player2Positions):
            listMoves.append(str(int(self.pos[0])+2)+chr(ord(self.pos[1])+1))
        if self.isAvailable(str(int(self.pos[0])-2)+chr(ord(self.pos[1])+1), player1Positions, player2Positions):
            listMoves.append(str(int(self.pos[0])-2)+chr(ord(self.pos[1])+1))
        if self.isAvailable(str(int(self.pos[0])+2)+chr(ord(self.pos[1])-1), player1Positions, player2Positions):
            listMoves.append(str(int(self.pos[0])+2)+chr(ord(self.pos[1])-1))
        if self.isAvailable(str(int(self.pos[0])-2)+chr(ord(self.pos[1])-1), player1Positions, player2Positions):
            listMoves.append(str(int(self.pos[0])-2)+chr(ord(self.pos[1])-1))
        return listMoves
class Rooks(ChessPlayer):
    def __init__(self, color:str, pos:str):
        super().__init__(color)
        self.pos : str = pos
    def getPos(self):
        return self.pos
    def getPossiblesMoves(self, player1Positions, player2Positions):
        up = True
        down = True
        right = True
        left = True
        listMoves = []
        for i in range(1, 9):
            if up:
                if self.isAvailable(str(int(self.pos[0])+i)+self.pos[1], player1Positions, player2Positions) == 1:
                    listMoves.append(str(int(self.pos[0])+i)+self.pos[1])
                elif self.isAvailable(str(int(self.pos[0])+i)+self.pos[1], player1Positions, player2Positions) == 2:
                    listMoves.append(str(int(self.pos[0])+i)+self.pos[1])
                    up = False
                else: up = False
            if down:
                if self.isAvailable(str(int(self.pos[0])-i)+self.pos[1], player1Positions, player2Positions) == 1:
                    listMoves.append(str(int(self.pos[0])-i)+self.pos[1])
                elif self.isAvailable(str(int(self.pos[0])-i)+self.pos[1], player1Positions, player2Positions) == 2:
                    listMoves.append(str(int(self.pos[0])-i)+self.pos[1])
                    down = False
                else: down = False
            if right:
                if self.isAvailable(self.pos[0]+chr(ord(self.pos[1])+i), player1Positions, player2Positions) == 1:
                    listMoves.append(self.pos[0]+chr(ord(self.pos[1])+i))
                elif self.isAvailable(self.pos[0]+chr(ord(self.pos[1])+i), player1Positions, player2Positions) == 2:
                    listMoves.append(self.pos[0]+chr(ord(self.pos[1])+i))
                    right = False
                else: right = False
            if left:
                if self.isAvailable(self.pos[0]+chr(ord(self.pos[1])-i), player1Positions, player2Positions) == 1:
                    listMoves.append(self.pos[0]+chr(ord(self.pos[1])-i))
                elif self.isAvailable(self.pos[0]+chr(ord(self.pos[1])-i), player1Positions, player2Positions) == 2:
                    listMoves.append(self.pos[0]+chr(ord(self.pos[1])-i))
                    left = False
                else: left = False
        return listMoves
class Queen(ChessPlayer):
    def __init__(self, color:str, pos:str):
        super().__init__(color)
        self.pos : str = pos
    def getPos(self):
        return self.pos
    def getPossiblesMoves(self, player1Positions : list[str], player2Positions : list[str]):
        up = True
        upRight = True
        right = True
        upLeft = True
        left = True
        downRight = True
        down = True
        downLeft = True
        listMoves = []
        for i in range(1, 9):
            if up:
                if self.isAvailable(str(int(self.pos[0])+i)+self.pos[1], player1Positions, player2Positions) == 1:
                    listMoves.append(str(int(self.pos[0])+i)+self.pos[1])
                elif self.isAvailable(str(int(self.pos[0])+i)+self.pos[1], player1Positions, player2Positions) == 2:
                    listMoves.append(str(int(self.pos[0])+i)+self.pos[1]) 
                    up = False
                else: up = False
            if upRight:
                if self.isAvailable(str(int(self.pos[0])+i)+chr(ord(self.pos[1])+i), player1Positions, player2Positions) == 1:
                    listMoves.append(str(int(self.pos[0])+i)+chr(ord(self.pos[1])+i))
                elif self.isAvailable(str(int(self.pos[0])+i)+chr(ord(self.pos[1])+i), player1Positions, player2Positions) == 2:
                    listMoves.append(str(int(self.pos[0])+i)+chr(ord(self.pos[1])+i))
                    upRight = False
                else: upRight = False
            if right:
                if self.isAvailable(str(int(self.pos[0]))+chr(ord(self.pos[1])+i), player1Positions, player2Positions) == 1:
                    listMoves.append(str(int(self.pos[0]))+chr(ord(self.pos[1])+i))
                elif self.isAvailable(str(int(self.pos[0]))+chr(ord(self.pos[1])+i), player1Positions, player2Positions) == 2:
                    listMoves.append(str(int(self.pos[0]))+chr(ord(self.pos[1])+i))
                    Right = False
                else: Right = False
            if downRight:
                if self.isAvailable(str(int(self.pos[0])-i)+chr(ord(self.pos[1])+i), player1Positions, player2Positions) == 1:
                    listMoves.append(str(int(self.pos[0])-i)+chr(ord(self.pos[1])+i))
                elif self.isAvailable(str(int(self.pos[0])-i)+chr(ord(self.pos[1])+i), player1Positions, player2Positions) == 2:
                    listMoves.append(str(int(self.pos[0])-i)+chr(ord(self.pos[1])+i))
                    downRight = False
                else: downRight = False
            if down:
                if self.isAvailable(str(int(self.pos[0])-i)+chr(ord(self.pos[1])), player1Positions, player2Positions) == 1:
                    listMoves.append(str(int(self.pos[0])-i)+chr(ord(self.pos[1])))
                elif self.isAvailable(str(int(self.pos[0])-i)+chr(ord(self.pos[1])), player1Positions, player2Positions) == 2:
                    listMoves.append(str(int(self.pos[0])-i)+chr(ord(self.pos[1])))
                    down = False
                else: down = False
            if downLeft:
                if self.isAvailable(str(int(self.pos[0])-i)+chr(ord(self.pos[1])-i), player1Positions, player2Positions) == 1:
                    listMoves.append(str(int(self.pos[0])-i)+chr(ord(self.pos[1])-i))
                elif self.isAvailable(str(int(self.pos[0])-i)+chr(ord(self.pos[1])-i), player1Positions, player2Positions) == 2:
                    listMoves.append(str(int(self.pos[0])-i)+chr(ord(self.pos[1])-i))
                    downLeft = False
                else: downLeft = False
            if left:
                if self.isAvailable(str(int(self.pos[0]))+chr(ord(self.pos[1])-i), player1Positions, player2Positions) == 1:
                    listMoves.append(str(int(self.pos[0]))+chr(ord(self.pos[1])-i))
                elif self.isAvailable(str(int(self.pos[0]))+chr(ord(self.pos[1])-i), player1Positions, player2Positions) == 2:
                    listMoves.append(str(int(self.pos[0]))+chr(ord(self.pos[1])-i))
                    left = False
                else: left = False
            if upLeft:
                if self.isAvailable(str(int(self.pos[0])+i)+chr(ord(self.pos[1])-i), player1Positions, player2Positions) == 1:
                    listMoves.append(str(int(self.pos[0])+i)+chr(ord(self.pos[1])-i))
                elif self.isAvailable(str(int(self.pos[0])+i)+chr(ord(self.pos[1])-i), player1Positions, player2Positions) == 2:
                    listMoves.append(str(int(self.pos[0])+i)+chr(ord(self.pos[1])-i))
                    upLeft = False
                else: upLeft = False
        return listMoves
class King(ChessPlayer):
    def __init__(self, color:str, pos:str):
        super().__init__(color)
        self.pos : str = pos
    def getPos(self):
        return self.pos
    def getPossiblesMoves(self, player1Positions, player2Positions):
        listMoves = []
        if self.isAvailable(str(int(self.pos[0])+1)+self.pos[1], player1Positions, player2Positions) > 0:
            listMoves.append(str(int(self.pos[0])+1)+self.pos[1])
        if self.isAvailable(str(int(self.pos[0])+1)+chr(ord(self.pos[1])+1), player1Positions, player2Positions) > 0:
            listMoves.append(str(int(self.pos[0])+1)+chr(ord(self.pos[1])+1))
        if self.isAvailable(str(int(self.pos[0]))+chr(ord(self.pos[1])+1), player1Positions, player2Positions) > 0:
            listMoves.append(str(int(self.pos[0]))+chr(ord(self.pos[1])+1))
        if self.isAvailable(str(int(self.pos[0])-1)+chr(ord(self.pos[1])+1), player1Positions, player2Positions) > 0:
            listMoves.append(str(int(self.pos[0])-1)+chr(ord(self.pos[1])+1))
        if self.isAvailable(str(int(self.pos[0])-1)+self.pos[1], player1Positions, player2Positions) > 0:
            listMoves.append(str(int(self.pos[0])-1)+self.pos[1])
        if self.isAvailable(str(int(self.pos[0])-1)+chr(ord(self.pos[1])-1), player1Positions, player2Positions) > 0:
            listMoves.append(str(int(self.pos[0])-1)+chr(ord(self.pos[1])-1))
        if self.isAvailable(str(int(self.pos[0]))+chr(ord(self.pos[1])-1), player1Positions, player2Positions) > 0:
            listMoves.append(str(int(self.pos[0]))+chr(ord(self.pos[1])-1))
        if self.isAvailable(str(int(self.pos[0])+1)+chr(ord(self.pos[1])-1), player1Positions, player2Positions) > 0:
            listMoves.append(str(int(self.pos[0])+1)+chr(ord(self.pos[1])-1))
        return listMoves

if __name__ == "__main__":
    player1 = ChessPlayer("White")
    player2 = ChessPlayer("Black")
    player1.createPlayer()
    player2.createPlayer()
    player1.printTable(player2)