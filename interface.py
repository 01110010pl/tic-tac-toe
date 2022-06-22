import os, sys

def cleanScreen():
    if sys.platform == 'linux':
        os.system('clear')
    elif sys.platform == 'windows':
        os.system('cls')

def ioMenu(content, answers):
    cleanScreen()
    while True:
        for i in content[:len(content) - 1]:
            print(i)
        answer = input(content[len(content) - 1])
        try:
            answer = int(answer)
            if answer in answers:
                break
        except:
            cleanScreen()
    return answer