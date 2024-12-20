def main():

    msg = input("Input:")
    short = shorten(msg)
    print(short)

def shorten(word):

        if 'a' in word:
            word = word.replace("a","")
        if 'A' in word:
            word = word.replace("A","")
        if 'e' in word:
            word = word.replace("e","")
        if 'E' in word:
            word = word.replace("E","")
        if 'i' in word:
            word = word.replace("i","")
        if 'I' in word:
            word = word.replace("I","")
        if 'o' in word:
            word = word.replace("o","")
        if 'O' in word:
            word = word.replace("O","")
        if 'u' in word:
            word = word.replace("u","")
        if 'U' in word:
            word = word.replace("U","")
        return word

if __name__ == "__main__":
    main()


