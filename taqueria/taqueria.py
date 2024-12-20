#dicionario do menu
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

#variavel com o valor total
total = 0.0

while True:

    try:

        item = input("Item: ").title()

    except KeyError:
        continue

    except EOFError:
        break

    if item in menu:
        total += menu[item]
        print("Total:  $%.2f" % total)




