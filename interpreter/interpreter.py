exp = input("Expression: ")
x, y, z = exp.split()


match y:
    case "+":
        r = float(x) + float(z)
        print(r)
    case "-":
        r = float(x) - float(z)
        float(r)
        print(r)
    case "/":
        r = float(x) / float(z)
        float(r)
        print(r)
    case "*":
        r = float(x) * float(z)
        float(r)
        print(r)