import re


def main():
    print(convert(input("Hours: ")))

def convert(s):

    if hours := re.search(r"^([0-9][0-2]?):?([0-5][0-9])? (AM|PM)? to ([0-9][0-2]?):?([0-5][0-9])? (AM|PM)?$",s):
        if int(hours.group(1)) > 12 or int(hours.group(4)) > 12:
            raise ValueError

        time_one = make_time(int(hours.group(1)), hours.group(2), hours.group(3))
        time_two = make_time(int(hours.group(4)), hours.group(5), hours.group(6))
        return time_one + " to " + time_two

    else:
        raise ValueError

def make_time(hour,minute,time):
    if time == "PM":
        if hour == 12:
            hour = 12
        else:
            hour += 12
    else:
        if hour == 12:
            hour = 0

    if minute == None:
        minute = ":00"
        full_time = f"{hour:02}{minute:02}"

    else:
        full_time = f"{hour:02}:{minute:02}"

    return full_time

if __name__ == "__main__":
    main()
