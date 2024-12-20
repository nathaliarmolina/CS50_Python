def main():

    #dicionario das compras
    list = {}

    #enquanto não for pressionado Ctrl+D
    while True:

        #captura os itens da lista
        try:
            item = input()
            item = item.upper()

            #adiciona o item à lista de compras
            if item in list:
                list[item] +=1
            else:
                list[item] = 1

        #depois do Ctrl+D
        except EOFError:

            #ordem alfabetica
            list = sorted(list.items())

            #imprime a lista de compras
            for item, qtde in list:
                print(f"{qtde} {item}")
            break

if __name__ == "__main__":
    main()


