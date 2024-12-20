import sys

def main():
    fraction = input("Fraction: ")
    p = convert(fraction)
    g = gauge(p)
    print(g)


def convert(fraction):

        try:
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
            sys.exit()

        except ZeroDivisionError:
            print("You can't divide by 0")
            sys.exit()

        else:
            return porc

def gauge(percentage):
    if percentage <= 1:
            return "E"
            #print("E")

    elif percentage >= 99 and percentage <= 100:
        return "F"
        print("F")

    else:

        return str(percentage) + "%"


if __name__ == "__main__":
    main()



