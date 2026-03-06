from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,binancecoin&vs_currencies=usd"
    try:
        data = requests.get(url).json()
        btc_price = data.get("bitcoin", {}).get("usd", 0)
        eth_price = data.get("ethereum", {}).get("usd", 0)
        sol_price = data.get("solana", {}).get("usd", 0)
        bnb_price = data.get("binancecoin", {}).get("usd", 0)
    except Exception as e:
        print("Error fetching data:", e)
        btc_price = eth_price = sol_price = bnb_price = 0

    return render_template("index.html",
                           btc=btc_price,
                           eth=eth_price,
                           sol=sol_price,
                           bnb=bnb_price)

if __name__ == "__main__":
    app.run(debug=True)
