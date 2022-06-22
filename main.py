from game import TicTacToe
import interface

def main():
    menu1 = ["TIC TAC TOE GAME\n", "1) GRAJ!", "2) WYJŚĆIE!", "ODPOWIEDZ: "]
    menu2 = ["TIC TAC TOE GAME\n", "RUCH MA TERAZ: {0}.", 
    "PLANSZA:", "|{0}|{1}|{2}|\n|{3}|{4}|{5}|\n|{6}|{7}|{8}|\n", "ZAJMUJE POZYCJE NR. : "]
    while True:
        answer = interface.ioMenu(menu1, [1, 2])
        if answer == 1:
           pass
        else:
            interface.cleanScreen()
            exit()

if __name__ == "__main__":
    main()
else:
    print("It's not a module! Please run this file like a normal program!")
    input("Press any key to end...")