def main():

    timeSt = input("What time is it? ")
    time = convert(timeSt)

    if time >= 07.00 and time <= 08.00:
        print("breakfast time")

    if time >= 12.00 and time <= 13.00:
        print("lunch time")

    if time >= 18.00 and time <= 19.00:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    minute = int(minute)
    minute = int(minute/0.6)
    minute = str(minute)

    time = hour + "." + minute
    time = float(time)
    return time

if __name__ == "__main__":
    main()