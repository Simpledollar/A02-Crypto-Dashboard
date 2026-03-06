import requests
import pandas as pd
import matplotlib.pyplot as plt
import time

tokens = ["bitcoin", "ethereum", "binancecoin"]

while True:
    # Lấy dữ liệu giá từ CoinGecko
    data = {}
    for token in tokens:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={token}&vs_currencies=usd"
        response = requests.get(url).json()
        data[token] = response[token]["usd"]

    # Hiển thị bảng với pandas
    df = pd.DataFrame(list(data.items()), columns=["Token", "Price (USD)"])
    print(df)

    # Vẽ biểu đồ với matplotlib
    plt.figure(figsize=(8,5))
    plt.bar(df["Token"], df["Price (USD)"], color=["orange","blue","green"])
    plt.title("Giá các token lớn (USD)")
    plt.xlabel("Token")
    plt.ylabel("Giá (USD)")
    plt.show()

    # Chờ 5 phút rồi cập nhật lại
    print("Đang chờ 5 phút để cập nhật lại...\n")
    time.sleep(30)
