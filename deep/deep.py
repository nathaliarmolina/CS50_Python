answer = input ("What is Great Question of Life, the Universe and Everything? ").strip()

answer = answer.lower()


match answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")