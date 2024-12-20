while True:

    try:
        fraction = input("Fraction: ")
        num, den = fraction.split("/")
        num = int(num)
        den = int(den)



        porc = (num/den) * 100
        porc = round(porc + 0.5, 2)
        porc = int(porc)

        if num > den:
            raise ValueError

    except ValueError:
        print("Invalid Fraction")

    except ZeroDivisionError:
        print("You can't divide by 0")

    else:



        if porc <= 1:
            print("E")
            break

        elif porc >= 99 and porc <= 100:
            print("F")
            break

        else:
            print(porc, "%", sep="")
            break

