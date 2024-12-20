import random


def main():
    global lvl #variavel global lvl (para ser acessada em mais de uma função)
    global score #variavel global score
    score = 0

    lvl = get_level() #captura o level

    for i in range(10): #gera 10 problemas
        start_game()

    get_score() #gera pontuação

def start_game(): # gera x e y e gera um problema com os mesmos

    x = generate_integer(lvl)
    y = generate_integer(lvl)
    get_problem(x,y)


def get_level(): #captura level
    valid_level = False

    while valid_level == False: #enquanto o nível não for válido, continue o loop

        level = input("Level: ")

        try:
            level = int(level) #tentar cast para int, invalida quando não é digito

        except ValueError:
            continue

        else:

                if level >=1 and level <= 3: #se nivel for valido, sai do loop

                    valid_level == True
                    return level

                else:
                    continue



def generate_integer(lvl): #gera os números de x e y de acordo com os níveis
    if lvl == 1:
        rand = random.randint(0, 9)
        return rand
    if lvl == 2:
        rand = random.randint(10, 99)
        return rand
    if lvl == 3:
        rand = random.randint(100, 999)
        return rand

def get_score(): # printa o score
    print("Score: ", score)


def get_problem(x, y): #gera o problema usando x e y


    attempts = 0

    while True:

        if attempts >=0 and attempts < 3: #valida 3 tentativas

            print(x, "+", y, end="")
            answer = input(" =")
            answer = int(answer)
            result = x + y

            if answer == result: #se acerto, gera pontuação
                global score
                score += 1
                break

            else:
                attempts += 1 #se erro, gera EEE e aumenta uma tentativa
                print("EEE")

        else: #mostra reultado quando esgotam as tentativas
            print(x, " + ", y, " = ", result)
            break

if __name__ == "__main__":
    main()