#Main configs and use call libraries
import config
from binance.client enums import
import time
import nump as np


client = Client(config.API_KEY, config.API_SECRET. tld='com')


# Follow Ticker function with putting Place Order

symbolTicker = 'USDTETH'
quanity = 1
prev_symbolPrice = 0


list_of_tickers = client.get_all_tickers()
for tick_2 in list_of_tickers:
    if tick_2['symbol'] == symbolTicker:
        prev_symbolPrice =  float(tick_2['price'])

# Basicamente el Bot en todo momento sigue al par que anteriormente listamos y le ordenamos que siga,
# luego lo persigue en todo moemnto y le va dejando ordener de compra para perseguir su precio,
# y cuando lo alcanza compra abajo y empieza a seguirlo tirandole cuantas ordenes de compra pueda tirarle
# poniendo y quitandole ordenes de venta, segun vaya subiendo hasta que vaya a empezar otro cicli bajista. 
# buscando vender en el mejor precio promedio alto, y comprando en el emjor precio promedio bajo,
# para continuar nuevamente y todo el tiempo con otro ciclo...

buyOrder = client.create_order(
    symbol = 'symbol Ticker',
    side = 'BUY'
    Type = 'STOP_LOSS_LIMIT'
    quanity = quantity,
    price = round(prev_symbolPrice*1.001,7),
    stopPrice = round(prev_symbolPrice*1.002,7),
    timeInForce = 'GTC'


)

FunctionExport.save()



# Buycoins Function









#SellCoins Function







