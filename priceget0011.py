from binance.client import Client
client = Client("O8Nrx1vRU3fy1Y1ocToiSaswNYrrg02c2dftryO1Mz3ZzK2CGG7OCMqrkJVqBWvt", "QpHsCcxAeaLqL0mts464NxSxtqCU8cHcbeE0aUIIFI3YUsi6yPAtCOv2woCXWotI")
br = "\n"
tradevarbase = 1
def the_whole_program():
    Crypto1 = "ETHBTC"
    Crypto2 = "ADXBTC"
    Crypto3 = "ADXETH"
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
    if tradevarbase2 > 1.0035:
        mailoutput = "ETH-BTC-ADX " + str(float(float(tradevarbase2) - float(1.00225)) * 100) + " %"
        print(price)
        print(price2)
        print(price3)
        print(mailoutput)
    elif tradevarbase2 < 0.9965:
        mailoutput = "ETH-ADX-BTC " + str(float(float(0.99775) - float(tradevarbase2)) * 100) + " %"
        print(mailoutput)
    else:
        print("Npt")
    print("___" + br)
while True:
    the_whole_program()