import re


def main():

    print(parse(input("HTML: ")))



def parse(s):

    #iframe = re.search(r'^<iframe src=', s)
    iframe = re.search(r"<iframe(.)*><\/iframe>", s)

    if iframe:
        yt = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)",s)
        if yt:
            end = (yt.group(4))
            subs = re.sub(r"(.)*youtube\.com\/embed\/([a-z_A-Z_0-9]+)(.)*", "https://youtu.be/" + end,s)
            return subs
        else:
            return None


if __name__ == "__main__":
    main()