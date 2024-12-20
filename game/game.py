import random

#seta o validador para falso
valid = False

#enquanto o validador for falso, o loop continua
while valid == False:
    try:
        n = input("Level: ") #captura nivel
        if n.isdigit() == False: #se nivel não for numérico, sobe a exceção
            raise ValueError


    except ValueError:
        continue #se subir a exceção, continua o loop

    else: #se nivel for numérico
            n = int(n) #converte n para int
            if n > 1: #certifica que o nível é maior do que 1
                valid = True 

#gera numero aleatório entre 1 e n
rand = random.randint(1, n)


#seta o número certo para falso
right_number = False

#enquanto o número certo for falso
while right_number == False:

    #solicita palpite para usuário e converte em int
    guess = input("Guess: ")
    guess = int(guess)

    #maior
    if guess > rand:
        print("Too large!")

    #menor
    elif guess < rand:
        print("Too small!")

    #certo
    else:
        print("Just right!")
        right_number = True