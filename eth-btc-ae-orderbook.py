from binance.client import Client
from datetime import datetime
from binance.enums import *


client = Client("vMKv5uaXbUi1z35CVgmPzUNkViu0qCaYQSGyQEJSy9FSG5S7Sa5rfdvZa8zNe3EJ", "HOhJZfwM64uaUlGP4rCicqZVFZ8NEPzB4QFCqH5dRslwdETQEEstVfDwv3uPovaC")

br = "\n"
tradevarbase = 1
AdxMenge = 700
EthMenge2 = 0.4

def the_whole_program():
    Crypto1 = "ETHBTC"
    Crypto2 = "ADXBTC"
    Crypto3 = "ADXETH"
    priceask = client.get_orderbook_ticker(symbol=Crypto1)['askPrice']
    pricebid = client.get_orderbook_ticker(symbol=Crypto2)['bidPrice']
    priceask2 = client.get_orderbook_ticker(symbol=Crypto3)['askPrice']
    var1 = float(priceask) * float(tradevarbase)
    var2 = float(var1) / float(pricebid)
    tradevarbase2 = float(var2) * float(priceask2)
    print("--")

    #print(tradevarbase2)

    print("ETHBTC" + " " + "ask" + " " + priceask)
    print("ADXBTC" + " " + "bid" + " " + pricebid)
    print("ADXETH" + " " + "ask" + " " + priceask2)
    if tradevarbase2 > 1.0035:

        mailoutput = "ETH-BTC-ADX " + str("%.2f" % (float(float(tradevarbase2) - float(1.00225)) * 100)) + " %"
        print(mailoutput)
        EthMengeT = str("%.4f" % (float(AdxMenge) * float(priceask2)))
        print("EthMenge" + " " + str("%.4f" % (float(AdxMenge) * float(priceask2))))
        servertime = client.get_server_time()['serverTime']
        print(datetime.fromtimestamp(int(float(servertime) / float(1000))))
    elif tradevarbase2 < 0.9965:

        mailoutput = "ETH-ADX-BTC " + str(float(float(0.99775) - float(tradevarbase2)) * 100) + " %"
        print(mailoutput)
        print("AdxMenge2" + " " + str("%.4f" % (float(EthMenge2) / float(price3))))
        servertime = client.get_server_time()['serverTime']
        print(datetime.fromtimestamp(int(float(servertime) / float(1000))))

    else:
        print("Npt")
    print("___" + br)


while True:
    the_whole_program()