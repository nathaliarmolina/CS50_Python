

month_list =  [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]



while True:

    try:

        date = input("Date: ")

        if "," in date:
            monday, year = date.split(",")
            mon, day = monday.split()
            mon = mon.capitalize()
            month = month_list.index(mon) + 1
            day = int(day)

            if day > 31:
                raise ValueError


            else:
                day = str(day)
                month = str(month)
                mon.strip()
                day.strip()
                year.strip()
                print (year, month.zfill(2), day.zfill(2), sep="-", end="")
                break

        elif "/" in date:
            mon, day, year = date.split("/")
            day = int(day)
            mon = int(mon)

            if day > 31:
                raise ValueError
            if mon > 12:
                raise ValueError

            day = str(day)
            mon = str(mon)
            if len(mon) > 2 or len(day) > 2:
                raise ValueError

            month = mon
            print (year.strip(), month.strip().zfill(2), day.strip().zfill(2), sep="-", end="")
            break


        else:
            pass

    except ValueError:
        pass







