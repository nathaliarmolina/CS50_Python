#biblioteca da linha de comando
import sys

#biblioteca csv
import csv

#biblioteca tabulate
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) < 2:
    sys.exit("Too many command-line arguments")

elif ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")

else:
    file_name = sys.argv[1]


try:
    table = []

    with open(file_name, "r") as csvfile:

        # Cria um objeto leitor CSV
        reader = csv.reader(csvfile, delimiter=",")

        # Pega a primeira linha para criar cabeçalho
        h = next(reader)

        #adiciona as próximas linhas na lista table
        for line in reader:
            table.append(line)

#caso o arquivo não exista, sobe exceção
except FileNotFoundError:
    sys.out("File not exist")

#imprime tabela
else:
    print(tabulate(table, h, tablefmt="grid"))



