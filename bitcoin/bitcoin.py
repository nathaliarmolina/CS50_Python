import requests
import sys
import json

requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
else:
    value = sys.argv[1]

try:
    value = float(value)
except ValueError:
    sys.exit("Command-line argument is not a number")
else:
    req = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")


    data = req.json()
    price = data["bpi"]["USD"]["rate"]
    price = price.replace(",", "")
    price = float(price) * value
    print(f"${price:,.4f}")