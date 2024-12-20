def main():
    #miss=50 pois caso o usuário insira um valor inválido, ele ainda vai dever 50 centavos
    miss = 50
    total = 0

    #continuar pedindo moedas enquanto o total de 50 não for atingido
    while total < 50:
        #reseta nova moeda
        coin = 0
        #captura valor da moeda
        coin = int(input("Insert Coin:"))
        #valida valor da moeda
        valcoin = validate_coin(coin)
        #se valor da moeda for validado, fazer as contas
        if valcoin == True:
            #total será acrescido do valor da moeda inserida
            total = total + coin
            #miss indica o valor que falta para 50 (50 - o valor total já inserido)
            miss = 50 - total

            #se o total inserido for valido e ainda for abaixo de 50, print Amount Due
            if total < 50 and total > 0:
                print("Amount Due:", miss)

        #se valor da moeda for inválido
        else:
            print("Amount Due:", miss)

    #se o valor inserido for maior do que 50, necessário troco
    if total >= 50:
        print("Change Owed:", total - 50)

# valida se a moeda é de 5, 10 ou 25 centavos
def validate_coin(c):
    if c == 5 or c == 10 or c == 25:
        return True


main()