import requests
import json
from tkinter import *
from tkinter import messagebox
import sqlite3

pycrypto = Tk()
pycrypto.title("My Crypto Profolio")
pycrypto.iconbitmap("panda.ico")

con = sqlite3.connect("coin.db")
cursor = con.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS coin(id INTEGER PRIMARY KEY,symbol TEXT,amount INTEGER,price REAL)")
# con.commit()
#
# cursor.execute("INSERT INTO coin VALUES(1,'BTC',2,28322.061728)")
# con.commit()
# cursor.execute("INSERT INTO coin VALUES(2,'ETH',10,1552.851426)")
# con.commit()

def reset():
    for cell in pycrypto.winfo_children():
        cell.destroy()

    app_nav()
    app_head()
    my_portfolio()

def app_nav():
    def clear_all():
        cursor.execute("DELETE FROM coin")
        con.commit()

        messagebox.showinfo("Portfolio Notification", "Portfolio Cleared - Add New Coins")
        reset()

    def close_app():
        pycrypto.destroy()

    menu = Menu(pycrypto)
    file_item = Menu(menu)
    file_item.add_command(label='Clear Portfolio', command=clear_all)
    file_item.add_command(label='Close App', command=close_app)
    menu.add_cascade(label="File", menu=file_item)
    pycrypto.config(menu=menu)

def my_portfolio():
    api_request = requests.get(
        "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=100&convert=USD&CMC_PRO_API_KEY=f0b41557-5c32-4674-a6aa-098821c6196e")
    api = json.loads(api_request.content)
    # coins = ["BTC","ETH"]
    cursor.execute("select * from coin")
    coins = cursor.fetchall()
    print(coins)
    overall_profit_loss = 0
    coin_row = 1
    total_current_value = 0
    total_amount_paid = 0

    def font_color(amount):
        if amount >= 0:
            return "green"
        else:
            return "red"
    def insert_coin():
        cursor.execute("INSERT INTO coin(symbol,amount,price) VALUES(?,?,?)",(symbol_txt.get(),amount_txt.get(),price_txt.get()))
        con.commit()
        messagebox.showinfo("Profolio management","Coin added successfully to portfolio..")
        reset()
    def update_coin():
        cursor.execute("UPDATE coin set symbol=?,amount=?,price=? where id = ?",(symbol_update.get(),amount_update.get(),price_update.get(),protid_update.get()))
        con.commit()
        messagebox.showinfo("Profolio management", "Coin updated successfully to portfolio..")
        reset()

    def delete_coin():
        cursor.execute("DELETE from coin where id = ?",(protid_delete.get(),))
        con.commit()
        messagebox.showinfo("Profolio management", "Coin deleted from portfolio ...")
        reset()
    # print(api)
    for i in range(0, 20):
        for coin in coins:
            if api["data"][i]["symbol"] == coin[1]:
                print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
                total_paid = coin[2]* coin[3]
                current_value = coin[2]* api["data"][i]["quote"]["USD"]["price"]
                total_current_value = total_current_value + current_value
                pl_per_coin = api["data"][i]["quote"]["USD"]["price"] - coin[3]
                total_pl = pl_per_coin * coin[2]
                overall_profit_loss = overall_profit_loss + total_pl
                total_amount_paid +=total_paid

                portfolio_id = Label(pycrypto, text=coin[0], bg="#F3F4F6", fg="black",font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
                portfolio_id.grid(row=coin_row, column=0, sticky=N + S + E + W)

                name = Label(pycrypto, text=api["data"][i]["symbol"], bg="#F3F4F6", fg="black",font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
                name.grid(row=coin_row, column=1, sticky=N + S + E + W)

                price = Label(pycrypto, text="${0:2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg="#F3F4F6", fg="black",font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
                price.grid(row=coin_row, column=2, sticky=N + S + E + W)

                no_coins = Label(pycrypto, text=coin[2], bg="#F3F4F6", fg="black",font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
                no_coins.grid(row=coin_row, column=3, sticky=N + S + E + W)

                amount_paid = Label(pycrypto, text="${0:2f}".format(total_paid), bg="#F3F4F6", fg="black",font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
                amount_paid.grid(row=coin_row, column=4, sticky=N + S + E + W)

                current_value = Label(pycrypto, text="${0:2f}".format(current_value), bg="#F3F4F6", fg="black",font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
                current_value.grid(row=coin_row, column=5, sticky=N + S + E + W)

                pl_per_coin = Label(pycrypto, text="${0:2f}".format(pl_per_coin), bg="#F3F4F6", fg=font_color(float("{0:2f}".format(pl_per_coin))),font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
                pl_per_coin.grid(row=coin_row, column=6, sticky=N + S + E + W)

                total_pl = Label(pycrypto, text="${0:2f}".format(total_pl), bg="#F3F4F6", fg=font_color(float("{0:2f}".format(total_pl))),font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
                total_pl.grid(row=coin_row, column=7, sticky=N + S + E + W)

                coin_row = coin_row + 1


    #insert
    symbol_txt = Entry(pycrypto,borderwidth=2,relief="groove")
    symbol_txt.grid(row=coin_row + 1,column=1)

    price_txt = Entry(pycrypto,borderwidth=2,relief="groove")
    price_txt.grid(row=coin_row + 1,column=2)

    amount_txt = Entry(pycrypto,borderwidth=2,relief="groove")
    amount_txt.grid(row=coin_row + 1,column=3)

    add_coin = Button(pycrypto, text="Add Coin", bg="white", fg="blue", font="Lato 12", command=insert_coin,padx="2",pady="2", borderwidth=2, relief="groove")
    add_coin.grid(row=coin_row + 1, column=4, sticky=N + S + E + W)

    #update

    protid_update = Entry(pycrypto,borderwidth=2,relief="groove")
    protid_update.grid(row=coin_row + 2,column=0)

    symbol_update = Entry(pycrypto,borderwidth=2,relief="groove")
    symbol_update.grid(row=coin_row + 2,column=1)

    price_update = Entry(pycrypto,borderwidth=2,relief="groove")
    price_update.grid(row=coin_row + 2,column=2)

    amount_update = Entry(pycrypto,borderwidth=2,relief="groove")
    amount_update.grid(row=coin_row + 2,column=3)

    update_coin = Button(pycrypto, text="Update Coin", bg="white", fg="blue", font="Lato 12", command=update_coin,padx="2",pady="2", borderwidth=2, relief="groove")
    update_coin.grid(row=coin_row + 2, column=4, sticky=N + S + E + W)

    #delete

    protid_delete = Entry(pycrypto,borderwidth=2,relief="groove")
    protid_delete.grid(row=coin_row + 3,column=0)

    delete_coin = Button(pycrypto, text="Delete Coin", bg="white", fg="blue", font="Lato 12", command=delete_coin,padx="2",pady="2", borderwidth=2, relief="groove")
    delete_coin.grid(row=coin_row + 3, column=4, sticky=N + S + E + W)


    total_amt_paid = Label(pycrypto, text="${0:2f}".format(total_amount_paid), bg="#F3F4F6", fg=font_color(float("{0:2f}".format(total_current_value))), font="Lato 12", padx="2",pady="2", borderwidth=2, relief="groove")
    total_amt_paid.grid(row=coin_row, column=4, sticky=N + S + E + W)

    current_total_value = Label(pycrypto, text="${0:2f}".format(total_current_value), bg="#F3F4F6", fg=font_color(float("{0:2f}".format(total_current_value))), font="Lato 12", padx="2",pady="2", borderwidth=2, relief="groove")
    current_total_value.grid(row=coin_row, column=5, sticky=N + S + E + W)

    overall_pl = Label(pycrypto, text="${0:2f}".format(overall_profit_loss), bg="#F3F4F6", fg=font_color(float("{0:2f}".format(overall_profit_loss))), font="Lato 12", padx="2",pady="2", borderwidth=2, relief="groove")
    overall_pl.grid(row=coin_row, column=7, sticky=N + S + E + W)
    api = ""
    refresh = Button(pycrypto, text="Refresh", bg="white", fg="blue", font="Lato 12", command=reset,padx="2",pady="2", borderwidth=2, relief="groove")
    refresh.grid(row=coin_row + 1, column=7, sticky=N + S + E + W)

    #print("Your current protfolio value is : ${0:2f}".format(overall_profit_loss))


def app_head():
    profolio_id = Label(pycrypto, text="Portfolio Id", bg="#142E54", fg="white", font="Lato 12 bold", padx="5", pady="5",
                 borderwidth=2, relief="groove")
    profolio_id.grid(row=0, column=0, sticky=N + S + E + W)

    name = Label(pycrypto, text="Coin Name", bg="#142E54", fg="white", font="Lato 12 bold", padx="5", pady="5",
                 borderwidth=2, relief="groove")
    name.grid(row=0, column=1, sticky=N + S + E + W)
    price = Label(pycrypto, text="Price", bg="#142E54", fg="white", font="Lato 12 bold", padx="5", pady="5",
                  borderwidth=2, relief="groove")
    price.grid(row=0, column=2, sticky=N + S + E + W)
    no_coins = Label(pycrypto, text="No Of Coins", bg="#142E54", fg="white", font="Lato 12 bold", padx="5", pady="5",
                     borderwidth=2, relief="groove")
    no_coins.grid(row=0, column=3, sticky=N + S + E + W)
    amount_paid = Label(pycrypto, text="Total Amount Paid", bg="#142E54", fg="white", font="Lato 12 bold", padx="5",
                        pady="5", borderwidth=2, relief="groove")
    amount_paid.grid(row=0, column=4, sticky=N + S + E + W)
    current_value = Label(pycrypto, text="Current Value", bg="#142E54", fg="white", font="Lato 12 bold", padx="5",
                          pady="5", borderwidth=2, relief="groove")
    current_value.grid(row=0, column=5, sticky=N + S + E + W)
    pl_per_coin = Label(pycrypto, text="P/L Per coin", bg="#142E54", fg="white", font="Lato 12 bold", padx="5",
                        pady="5", borderwidth=2, relief="groove")
    pl_per_coin.grid(row=0, column=6, sticky=N + S + E + W)
    total_pl = Label(pycrypto, text="Total Profit and Loss", bg="#142E54", fg="white", font="Lato 12 bold", padx="5",
                     pady="5", borderwidth=2, relief="groove")
    total_pl.grid(row=0, column=7, sticky=N + S + E + W)


app_nav()
app_head()

my_portfolio()
pycrypto.mainloop()
cursor.close()
con.close()

print("Exiting my protfolio.....................")

