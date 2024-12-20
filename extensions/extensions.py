file = input("File name: ")

##padronizar em minusculas e tirar espaços
f = file.lower().strip()

##capturar o final da string e retornar um boolean

jpg = f.endswith('jpg')
jpeg = f.endswith('jpeg')
gif = f.endswith('gif')
png = f.endswith('png')
pdf = f.endswith('pdf')
txt = f.endswith('txt')
zipp = f.endswith('zip')


if jpg == True or jpeg == True:
    print("image/jpeg")

elif gif == True:
    print("image/gif")

elif png == True:
    print("image/png")

elif pdf == True:
    print("application/pdf")

elif txt == True:
    print("text/plain")

elif zipp == True:
    print("application/zip")

else:
    print("application/octet-stream")

