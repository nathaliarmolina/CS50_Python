def convert(txt):
    txt = (txt.replace(":(", "🙁"))
    txt = (txt.replace(":)", "🙂"))
    print(txt)
    return txt

def main():
    text = input("")
    convert(text)

main()

