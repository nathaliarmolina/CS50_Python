msg = input("Input:")


for m in msg  :
    if 'a' in m:
        m = m.replace("a","")
    if 'A' in m:
        m = m.replace("A","")
    if 'e' in m:
        m = m.replace("e","")
    if 'E' in m:
        m = m.replace("E","")
    if 'i' in m:
        m = m.replace("i","")
    if 'I' in m:
        m = m.replace("I","")
    if 'o' in m:
        m = m.replace("o","")
    if 'O' in m:
        m = m.replace("O","")
    if 'u' in m:
        m = m.replace("u","")
    if 'U' in m:
        m = m.replace("U","")
    print(m, end="")

print("\n")

