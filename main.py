#Terminal'den "pip install python-binance" yazarak binance kütüphanesini indirin#

from binance.client import Client
#Binance keys.py dosyasını içeri çekiyoruz.#
import keys

client=Client(api_key=keys.Pkey,api_secret=keys.Skey)

balanceETH=client.get_asset_balance("ETH")
balanceETC=client.get_asset_balance("ETC")
balanceBNB=client.get_asset_balance("BNB")
balanceUSDT=client.get_asset_balance("USDT")

print(balanceETH)
print(balanceETC)
print(balanceBNB)
print(balanceUSDT)