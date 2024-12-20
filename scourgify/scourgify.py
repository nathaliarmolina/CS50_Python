#biblioteca para escrever na linha de comando
import sys

#bibiloteca csv
import csv

#se tiver menos de 3 argumentos
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

#se tiver mais de 3 argumentos
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

#se tiver 3 argumentos, captura o nome dos arquivos para as variáveis
else:

    file_1 = sys.argv[1]
    file_2 = sys.argv[2]

try:

    #abre o leitor de dicionários
    with open(file_1) as file1:
        reader = csv.DictReader(file1)

        #abre o escritor de dicionários
        with open(file_2, "w") as file2:
            #coloca o nome das colunas
            writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
            writer.writeheader()

            #para cada linha do arquivo original (sendo lido)
            for row in reader:
                #extrai a coluna name do arquivo original para a variavel first
                row["first"] = row.pop("name")
                #separa a variavel first em last_name e first_name
                last_name, first_name = row["first"].split(",")
                #coloca o conteúdo de first_name no campo first
                row["first"] = first_name.strip()
                #coloca o conteúdo de last_name no campo last
                row["last"] = last_name.strip()
                #escreve a linha no novo arquivo
                writer.writerow(row)




except FileNotFoundError:
    sys.exit("Could not read " + file_1)

else:
    sys.exit()