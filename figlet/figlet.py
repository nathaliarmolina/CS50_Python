from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

fontes = figlet.getFonts() #variável que irá conter as fontes / tipo lista

#se o usuário não inserir parametro da fonte, gera fonte aleatória
if len(sys.argv) == 1:
    figlet.setFont(font = random.choice(fontes))

#se o usuário inserir dois argumentos, verifica se são válidos para inserir fonte e se estão na lista de fontes
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fontes:
    figlet.setFont(font=sys.argv[2]) #seta a fonte para a digitada

#argumento inválido, exibe mensagem de erro
else:
    sys.exit("Invalid usage")

text = input("Input: ") #captura input
print(figlet.renderText(text)) #renderiza o texto

