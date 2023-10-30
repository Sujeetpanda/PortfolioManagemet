import requests
import json
import tkinter
from tkinter import *

pycrypto = Tk()
pycrypto.title("My Crypto Profolio")




def my_portfolio():
    api_request = requests.get(
        "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=f0b41557-5c32-4674-a6aa-098821c6196e")
    api = json.loads(api_request.content)
    # coins = ["BTC","ETH"]
    coins = [
        {
            "symbol": "BTC",
            "amount_owned": 2,
            "price_per_coin": 28322.061728
        },
        {
            "symbol": "ETH",
            "amount_owned": 10,
            "price_per_coin": 1552.851426
        }
    ]
    print("===============================")
    print("===============================")
    overall_profit_loss = 0
    coin_row = 1
    # print(api)
    for i in range(0, 5):
        for coin in coins:
            if api["data"][i]["symbol"] == coin["symbol"]:
                print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
                total_paid = coin['amount_owned'] * coin['price_per_coin']
                current_value = coin['amount_owned'] * api["data"][i]["quote"]["USD"]["price"]
                pl_per_coin = api["data"][i]["quote"]["USD"]["price"] - coin['price_per_coin']
                total_pl = pl_per_coin * coin['amount_owned']
                overall_profit_loss = overall_profit_loss + total_pl
                # print("Price - ${0:2f}".format(api["data"][i]["quote"]["USD"]["price"]))
                # print("Total Amount Paid - ${0:2f}".format(total_paid))
                # print("Current Value - ${0:2f}".format(current_value))
                # print("P/L Per coin - ${0:2f}".format(pl_per_coin))
                # print("Total P/L - ${0:2f}".format(total_pl))
                # print("===============================")

                name = Label(pycrypto, text=api["data"][i]["symbol"], bg="grey", fg="black")
                name.grid(row=coin_row, column=0, sticky=N + S + E + W)

                price = Label(pycrypto, text="${0:2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg="white", fg="black")
                price.grid(row=coin_row, column=1, sticky=N + S + E + W)

                no_coins = Label(pycrypto, text=coin['amount_owned'], bg="grey", fg="black")
                no_coins.grid(row=coin_row, column=2, sticky=N + S + E + W)

                amount_paid = Label(pycrypto, text="${0:2f}".format(total_paid), bg="white", fg="black")
                amount_paid.grid(row=coin_row, column=3, sticky=N + S + E + W)

                current_value = Label(pycrypto, text="${0:2f}".format(current_value), bg="grey", fg="black")
                current_value.grid(row=coin_row, column=4, sticky=N + S + E + W)

                pl_per_coin = Label(pycrypto, text="${0:2f}".format(pl_per_coin), bg="white", fg="black")
                pl_per_coin.grid(row=coin_row, column=5, sticky=N + S + E + W)

                total_pl = Label(pycrypto, text="${0:2f}".format(total_pl), bg="grey", fg="black")
                total_pl.grid(row=coin_row, column=6, sticky=N + S + E + W)

                coin_row = coin_row + 1
    print("Your current protfolio value is : ${0:2f}".format(overall_profit_loss))



name=Label(pycrypto,text="Coin Name",bg="grey",fg="black")
name.grid(row=0,column=0,sticky=N+S+E+W)

price=Label(pycrypto,text="Price",bg="white",fg="black")
price.grid(row=0,column=1,sticky=N+S+E+W)

no_coins=Label(pycrypto,text="No Of Coins",bg="grey",fg="black")
no_coins.grid(row=0,column=2,sticky=N+S+E+W)

amount_paid =Label(pycrypto,text="Total Amount Paid",bg="white",fg="black")
amount_paid.grid(row=0,column=3,sticky=N+S+E+W)

current_value=Label(pycrypto,text="Current Value",bg="grey",fg="black")
current_value.grid(row=0,column=4,sticky=N+S+E+W)

pl_per_coin=Label(pycrypto,text="P/L Per coin",bg="white",fg="black")
pl_per_coin.grid(row=0,column=5,sticky=N+S+E+W)

total_pl=Label(pycrypto,text="Total Profit and Loss",bg="grey",fg="black")
total_pl.grid(row=0,column=6,sticky=N+S+E+W)

my_portfolio()
pycrypto.mainloop()
print("Exiting my protfolio.....................")

