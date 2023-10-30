import requests
import json
import tkinter
from tkinter import *

pycrypto = Tk()
pycrypto.title("My Crypto Profolio")
pycrypto.iconbitmap("D:\PythonLearning\CoinMaster\panda.ico")


def font_color(amount):
    if amount >= 0:
        return "green"
    else:
        return "red"

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
    overall_profit_loss = 0
    coin_row = 1
    total_current_value = 0
    # print(api)
    for i in range(0, 5):
        for coin in coins:
            if api["data"][i]["symbol"] == coin["symbol"]:
                print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
                total_paid = coin['amount_owned'] * coin['price_per_coin']
                current_value = coin['amount_owned'] * api["data"][i]["quote"]["USD"]["price"]
                total_current_value = total_current_value + current_value
                pl_per_coin = api["data"][i]["quote"]["USD"]["price"] - coin['price_per_coin']
                total_pl = pl_per_coin * coin['amount_owned']
                overall_profit_loss = overall_profit_loss + total_pl

                name = Label(pycrypto, text=api["data"][i]["symbol"], bg="#F3F4F6", fg="black",font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
                name.grid(row=coin_row, column=0, sticky=N + S + E + W)

                price = Label(pycrypto, text="${0:2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg="#F3F4F6", fg="black",font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
                price.grid(row=coin_row, column=1, sticky=N + S + E + W)

                no_coins = Label(pycrypto, text=coin['amount_owned'], bg="#F3F4F6", fg="black",font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
                no_coins.grid(row=coin_row, column=2, sticky=N + S + E + W)

                amount_paid = Label(pycrypto, text="${0:2f}".format(total_paid), bg="#F3F4F6", fg="black",font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
                amount_paid.grid(row=coin_row, column=3, sticky=N + S + E + W)

                current_value = Label(pycrypto, text="${0:2f}".format(current_value), bg="#F3F4F6", fg="black",font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
                current_value.grid(row=coin_row, column=4, sticky=N + S + E + W)

                pl_per_coin = Label(pycrypto, text="${0:2f}".format(pl_per_coin), bg="#F3F4F6", fg=font_color(float("{0:2f}".format(pl_per_coin))),font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
                pl_per_coin.grid(row=coin_row, column=5, sticky=N + S + E + W)

                total_pl = Label(pycrypto, text="${0:2f}".format(total_pl), bg="#F3F4F6", fg=font_color(float("{0:2f}".format(total_pl))),font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
                total_pl.grid(row=coin_row, column=6, sticky=N + S + E + W)

                coin_row = coin_row + 1


    current_total_value = Label(pycrypto, text="${0:2f}".format(total_current_value), bg="#F3F4F6", fg=font_color(float("{0:2f}".format(total_current_value))), font="Lato 12", padx="2",pady="2", borderwidth=2, relief="groove")
    current_total_value.grid(row=coin_row, column=4, sticky=N + S + E + W)
    overall_pl = Label(pycrypto, text="${0:2f}".format(overall_profit_loss), bg="#F3F4F6", fg=font_color(float("{0:2f}".format(overall_profit_loss))), font="Lato 12", padx="2",pady="2", borderwidth=2, relief="groove")
    overall_pl.grid(row=coin_row, column=6, sticky=N + S + E + W)
    api = ""
    update = Button(pycrypto, text="Update", bg="white", fg="blue", font="Lato 12", command=my_portfolio,padx="2",pady="2", borderwidth=2, relief="groove")
    update.grid(row=coin_row + 1, column=6, sticky=N + S + E + W)

    #print("Your current protfolio value is : ${0:2f}".format(overall_profit_loss))



name=Label(pycrypto,text="Coin Name",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
name.grid(row=0,column=0,sticky=N+S+E+W)

price=Label(pycrypto,text="Price",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
price.grid(row=0,column=1,sticky=N+S+E+W)

no_coins=Label(pycrypto,text="No Of Coins",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
no_coins.grid(row=0,column=2,sticky=N+S+E+W)

amount_paid =Label(pycrypto,text="Total Amount Paid",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
amount_paid.grid(row=0,column=3,sticky=N+S+E+W)

current_value=Label(pycrypto,text="Current Value",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
current_value.grid(row=0,column=4,sticky=N+S+E+W)

pl_per_coin=Label(pycrypto,text="P/L Per coin",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
pl_per_coin.grid(row=0,column=5,sticky=N+S+E+W)

total_pl=Label(pycrypto,text="Total Profit and Loss",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
total_pl.grid(row=0,column=6,sticky=N+S+E+W)

my_portfolio()
pycrypto.mainloop()
print("Exiting my protfolio.....................")

