import requests
import pandas as pd
import matplotlib.pyplot as plt

# Danh sách token lớn
tokens = ["bitcoin", "ethereum", "binancecoin"]

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
