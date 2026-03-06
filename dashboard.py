from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # Lấy dữ liệu giá Bitcoin và Ethereum từ CoinGecko API
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    data = requests.get(url).json()
    btc_price = data["bitcoin"]["usd"]
    eth_price = data["ethereum"]["usd"]

    return render_template("index.html", btc=btc_price, eth=eth_price)

if __name__ == "__main__":
    app.run(debug=True)
