from binance.client import Client
from binance.enums import *
import time

br = "\n"
tradevarbase = 1
import datetime
Crypto1 = "ETHBTC"
Crypto2 = "ADXBTC"
Crypto3 = "ADXETH"
tradewert = 0.05
def trader(client = Client("O8Nrx1vRU3fy1Y1ocToiSaswNYrrg02c2dftryO1Mz3ZzK2CGG7OCMqrkJVqBWvt", "QpHsCcxAeaLqL0mts464NxSxtqCU8cHcbeE0aUIIFI3YUsi6yPAtCOv2woCXWotI")):
    time1 = client.get_server_time()['serverTime']
    askcry1 = client.get_orderbook_ticker(symbol=Crypto1)['askPrice']
    bidcry2 = client.get_orderbook_ticker(symbol=Crypto2)['bidPrice']
    askcry3 = client.get_orderbook_ticker(symbol=Crypto3)['askPrice']

    var1 = tradevarbase * askcry1
    var2 = float(var1) / float(bidcry2)
    tradevarbase2 = float(var2) * float(askcry3)

    if tradevarbase2 > 1.0035:
        tradevarbase3 = float(float(float(tradevarbase2) - float(1.00225)) * 100)
        if tradevarbase3 > 0:
            print("Trade!")
            print("Gewinn: " + str(tradevarbase3) + " %")
            #Kaufe mit ETH BTC
            """client = client.create_order(symbol=Crypto1,
                                         side=SIDE_SELL,
                                         type=ORDER_TYPE_LIMIT,
                                         timeInForce=TIME_IN_FORCE_GTC,
                                         quantity=0.05,
                                         price=askcry1)"""
            #Kaufe mit BTC AE
            quantadx = float(tradewert) * float(askcry1)
            print("quantadx " + str(quantadx))
            """client = client.create_order(symbol=Crypto2,
                                         side=SIDE_BUY,
                                         type=ORDER_TYPE_LIMIT,
                                         timeInForce=TIME_IN_FORCE_GTC,
                                         quantity=str("%.3f" % (quantadx)),
                                         price=bidcry2)"""
            #Kaufe mit AE ETH
            quanteth = float(quantadx) / float(bidcry2)
            print("quanteth " + str(quanteth))
            """client = client.create_order(symbol=Crypto3,
                                         side=SIDE_SELL,
                                         type=ORDER_TYPE_LIMIT,
                                         timeInForce=TIME_IN_FORCE_GTC,
                                         quantity=str("%.3f" % (quanteth)),
                                         price=askcry3)"""
        else:
            print("NPT")
        #print(tradevarbase3)
    else:
        print("NPT")
    output = float(float(tradevarbase2 - 1) * 100)
    print("RAW plus: " + str(output) + " %")
    print("Runtime: " + str(float(client.get_server_time()['serverTime']) - float(time1)) + " MS \n ---")
    time.sleep(0.2)
while 1:
    trader()