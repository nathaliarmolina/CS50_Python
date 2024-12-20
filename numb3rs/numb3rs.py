import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    valid = re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip)

    if valid:

        one = int(valid.group(1))
        two = int (valid.group(2))
        three = int(valid.group(3))
        four = int(valid.group(4))

        if one >= 0 and one <=255 and two >= 0 and two <=255 and three >= 0 and three <=255 and four >= 0 and four <=255:
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()