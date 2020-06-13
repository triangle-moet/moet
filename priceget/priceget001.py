from binance.client import Client
from binance.enums import *
client = Client("O8Nrx1vRU3fy1Y1ocToiSaswNYrrg02c2dftryO1Mz3ZzK2CGG7OCMqrkJVqBWvt", "QpHsCcxAeaLqL0mts464NxSxtqCU8cHcbeE0aUIIFI3YUsi6yPAtCOv2woCXWotI")
br = "\n"
tradevarbase = 1
def the_whole_program():
    Crypto1 = "ETHBTC"
    Crypto2 = "ADABTC"
    Crypto3 = "ADAETH"
    price = client.get_symbol_ticker(symbol=Crypto1)
    price = str(price)
    price = price.replace("'}", "")
    price = price.replace("{'symbol': '" + Crypto1 + "', 'price': '", "")
    price2 = client.get_symbol_ticker(symbol=Crypto2)
    price2 = str(price2)
    price2 = price2.replace("'}", "")
    price2 = price2.replace("{'symbol': '" + Crypto2 + "', 'price': '", "")
    price3 = client.get_symbol_ticker(symbol=Crypto3)
    price3 = str(price3)
    price3 = price3.replace("'}", "")
    price3 = price3.replace("{'symbol': '" + Crypto3 + "', 'price': '", "")
    var1 = float(price) * float(tradevarbase)
    var2 = float(var1) / float(price2)
    tradevarbase2 = float(var2) * float(price3)
    print("--")
    if tradevarbase2 > 1.003:
        print("ETH: " + str(tradevarbase))
        print("ETH2: " + str(tradevarbase2))
    elif tradevarbase2 < 0.997:
        print("ETH: " + str(tradevarbase))
        print("ETH2: " + str(tradevarbase2))

    else:
        print("NPT")
        order = client.create_test_order(
            symbol=Crypto1,
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=1,
            price='0.00001')
    print("___" + br)


while True:
    the_whole_program()