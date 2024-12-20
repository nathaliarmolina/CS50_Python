msg = input("camelCase:")


#laço for que irá percorrer todas as letras de msg
for m in msg:
    #boolean para verificar se m é maiuscula
    mai = m.isupper()

    #se m for minuscula (maiuscula é falsa)
    if mai == False:
            #printa m sem quebra de linha
            print(m, end="")

    #caso for maicuscula(else)
    else:
          #printa _
          print("_", end="")
          #altera para letra minuscula e printa
          print(m.lower(), end="")

print("\n")



