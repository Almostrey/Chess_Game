from colorama import Fore, Back, Style, init
from ChessPackage import ChessPlayer

def main():
    player1 = ChessPlayer.ChessPlayer(color="White")
    player2 = ChessPlayer.ChessPlayer(color="Black")
    player1.createPlayer()
    player2.createPlayer()
    while True:
        while True:
            player1.printTable(player2)
            fromPlace = input(Fore.GREEN + "Fichas color VERDE juegan. ¿Que ficha desea mover?: ")
            toPlace = input(f"Mover ficha \"{fromPlace}\" a : ")
            if player1.movPiece(fromPlace, toPlace, player2):
                print("Jugada Realizada, esperando al siguiente jugador...")
                break
            else:
                print("Lugares indicados incorrectos...")
        if player2.King.pos == "X":
            print("Jugador 1 ha ganado")
            break
        while True:
            player1.printTable(player2)
            fromPlace = input(Fore.RED + "Fichas color ROJO juegan. ¿Que ficha desea mover?: ")
            toPlace = input(f"Mover ficha \"{fromPlace}\" a : ")
            if player2.movPiece(fromPlace, toPlace, player1):
                print("Jugada Realizada, esperando al siguiente jugador...")
                break
            else:
                print("Lugares indicados incorrectos...")
        if player1.King.pos == "X":
            print(Fore.YELLOW + "Jugador 2 ha ganado")
            break
    print(Fore.BLACK)
if __name__ == "__main__":
    main()