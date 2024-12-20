#biblioteca para escrever na linha de comando
import sys

#se forem menos de 2 argumentos
if len(sys.argv) < 2:
    sys.exit("Too few command-line argument")

#se forem mais de 2 argumentos
elif len(sys.argv) > 2:
    sys.exit("Too many command-line argument")

#se não tiver a extensão .py
elif ".py" not in sys.argv[1]:
    sys.exit("Not a Python file")

#passa o comando da linha de código para a variável
else:

    file_name = sys.argv[1]

try:
    #abrir o arquivo
    with open(file_name, "r") as f:
        count = 0

        #se não tiver espaços e não for comentário, insira uma linha
        for line in f:
            if not line.lstrip(). startswith("#") and line.lstrip() != '':
                count +=1


#levanta exceção caso o arquivo não exista
except FileNotFoundError:
    sys.exit("File does not exist")

else:

    print(count)