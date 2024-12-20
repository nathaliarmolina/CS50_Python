#biblioteca para escrever na linha de comando
import sys

#bibiloteca csv
import csv

#biblioteca PIL de imagens
from PIL import Image, ImageOps

#se tiver menos de 3 argumentos
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

#se tiver mais de 3 argumentos
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

#se tiver 3 argumentos corretos
if len(sys.argv) == 3:

    #se não tiver a extensão correta no arquivo de entrada
    if ".jpg" not in sys.argv[1] and ".png" not in sys.argv[1] and ".jpeg" not in sys.argv[1]:
        sys.exit("Invalid input")

    #se não tiver a extensão correta no arquivo de saida
    if ".jpg" not in sys.argv[2] and ".png" not in sys.argv[2] and ".jpeg" not in sys.argv[2]:
        sys.exit("Invalid output")

    #se não tiver a mesma extensão
    if ".jpg" in sys.argv[1] and ".jpg" not in sys.argv[2]:
        sys.exit("Input and output have different extensions")

    #se não tiver a mesma extensão
    if ".png" in sys.argv[1] and ".png" not in sys.argv[2]:
        sys.exit("Input and output have different extensions")

    #se não tiver a mesma extensão
    if ".jpeg" in sys.argv[1] and ".jpeg" not in sys.argv[2]:
        sys.exit("Input and output have different extensions")

    #se tiver 3 argumentos corretos, captura o nome dos arquivos para as variáveis
    else:

        in_image = sys.argv[1]
        saved_image = sys.argv[2]

#abre imagem do primeiro argumento, se existir
try:
    user_image = Image.open(in_image)

except FileNotFoundError:
    sys.exit("Input does not exist")

else:
    #abre imagem shirt
    shirt = Image.open("shirt.png")
    #regula o tamanho de shirt
    size = shirt.size
    #coloca o tamanho da imagem do mesmo tamanho da camisa
    user_image = ImageOps.fit(user_image, size)
    #sobrepoe imagem
    user_image.paste(shirt, shirt)
    #salva
    user_image.save(saved_image)