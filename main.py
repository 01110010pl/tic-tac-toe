from game import TicTacToe
import interface

def main():
    menu1 = ["TIC TAC TOE GAME\n", "1) GRAJ!", "2) WYJŚĆIE!", "ODPOWIEDZ: "]
    menu2 = ["TIC TAC TOE GAME\n", "RUCH MA TERAZ: {0}.", 
    "PLANSZA:", "|{0}|{1}|{2}|\n|{3}|{4}|{5}|\n|{6}|{7}|{8}|\n", "ZAJMUJE POZYCJE NR. : "]
    while True:
        answer = interface.ioMenu(menu1, [1, 2])
        if answer == 1:
            interface.cleanScreen()
            tic = TicTacToe()
            while True:
                menu2copy = menu2[:]
                menu2copy[1] = menu2copy[1].format(tic.currentTurn)
                menu2copy[3] = menu2copy[3].format(*tic.board)
                answer = interface.ioMenu(menu2copy, tic.getFreePlaces())
                tic.setPlace(answer)
                if tic.checkWin():
                    menu3 = ["WYGRAŁ {0}!", "WCIŚNIJ DOWOLNY KLAWISZ ABY KONTRYNOWAĆ..."]
                    menu3[0] = menu3[0].format(tic.currentTurn)
                    interface.ioMenu(menu3)
                    break
                elif tic.getFreePlaces() == []:
                    menu3 = ["NIKT NIE WYGRAŁ!", "WCIŚNIJ DOWOLNY KLAWISZ ABY KONTRYNOWAĆ..."]
                    interface.ioMenu(menu3)
                    break
                else:
                    tic.changeTurn()
        else:
            interface.cleanScreen()
            exit()

if __name__ == "__main__":
    main()
else:
    print("It's not a module! Please run this file like a normal program!")
    input("Press any key to end...")