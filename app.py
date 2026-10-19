from flask import Flask, redirect
import json
import os

app = Flask(__name__)

# Load saved data
if os.path.exists("save.json"):
    with open("save.json", "r") as file:
        data = json.load(file)
        balance = data["balance"]
        inventory = data["inventory"]
else:
    balance = 100
    inventory = []

def save_game():
    data = {
        "balance": balance,
        "inventory": inventory
    }

    with open("save.json", "w") as file:
        json.dump(data, file)

@app.route("/")
def home():
    return f"""
    <html>
    <head>
        <title>ShubhiCoin</title>
    </head>

    <body style="
    background:#1e1e2f;
    font-family:Arial;
    text-align:center;
    color:white;
    padding:30px;
    ">

    <div style="
    background:#2d2d44;
    width:500px;
    margin:auto;
    padding:25px;
    border-radius:20px;
    box-shadow:0px 0px 20px gold;
    ">

    <h1 style="color:gold;">
    🪙 ShubhiCoin (SHB)
    </h1>

    <h3>Created by Shubhi</h3>

    <h2 style="color:lightgreen;">
    Balance: {balance} SHB
    </h2>

    <a href="/mine">
        <button style="
        padding:10px 20px;
        background:gold;
        border:none;
        border-radius:10px;
        font-size:18px;
        cursor:pointer;
        ">
        Mine SHB
        </button>
    </a>

    <br><br>

    <a href="/buy_sword">
        <button style="
        padding:10px 20px;
        background:dodgerblue;
        color:white;
        border:none;
        border-radius:10px;
        font-size:18px;
        cursor:pointer;
        ">
        Buy Sword (50 SHB)
        </button>
    </a>

    <br><br>

    <h3>Inventory</h3>

    <p style="font-size:18px;">
    {', '.join(inventory) if inventory else 'Empty'}
    </p>

    </div>

    </body>
    </html>
    """

@app.route("/mine")
def mine():
    global balance
    balance += 10
    save_game()
    return redirect("/")

@app.route("/buy_sword")
def buy_sword():
    global balance, inventory

    if balance >= 50:
        balance -= 50
        inventory.append("Sword")
        save_game()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
