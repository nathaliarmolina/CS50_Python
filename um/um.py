import re



def main():
    print(count(input("Text: ")))


def count(s):
    input_min = re.findall(r"\bum\b",s)
    input_mai = re.findall(r"\bUm\b",s)
    qtde_min = len(input_min)
    qtde_mai = len(input_mai)
    q_total = qtde_min + qtde_mai

    return q_total


if __name__ == "__main__":
    main()
