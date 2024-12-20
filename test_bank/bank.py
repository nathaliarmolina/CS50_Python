def main():
    greeting = input("Greeting: ")
    money = value(greeting)
    print("$",money)

def value (greeting):

    greeting = greeting.lower().strip()
    i = greeting[0]
    first = greeting.split()
    firstc = greeting.split(",")

    if i == 'h':
        if 'hello' in first or 'hello' in firstc:
            return 0
        else:
            return 20
    if i != 'h':
        return 100

if __name__ == "__main__":
    main()