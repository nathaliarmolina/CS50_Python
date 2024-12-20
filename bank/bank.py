msg = input("Greeting: ")
msg = msg.lower().strip()
i = msg[0]
first = msg.split()
firstc = msg.split(",")

if i == 'h':
    if 'hello' in first or 'hello' in firstc:
        print("$0")
    else:
        print("$20")
if i != 'h':
    print("$100")