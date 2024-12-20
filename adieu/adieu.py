import inflect

p = inflect.engine()

list = []
text = "Adieu, adieu, to "

while True:
    try:
        name = input("Name: ")
        list.append(name)
    except EOFError:
        print()
        break

join = p.join(list)
print(text + join)


