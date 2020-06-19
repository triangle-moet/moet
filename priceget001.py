from binance.client import Client
client = Client("O8Nrx1vRU3fy1Y1ocToiSaswNYrrg02c2dftryO1Mz3ZzK2CGG7OCMqrkJVqBWvt", "QpHsCcxAeaLqL0mts464NxSxtqCU8cHcbeE0aUIIFI3YUsi6yPAtCOv2woCXWotI")
br = "\n"
tradevarbase = 1
gebühren = 0.075
Crypto1 = "ETHBTC"
Crypto2 = "AEBTC"
Crypto3 = "AEETH"
def trader():
    time1 = client.get_server_time()['serverTime']
    tradevarbase2 = float(float(float(float(client.get_symbol_ticker(symbol=Crypto1)['price']) * float(tradevarbase)) / float(client.get_symbol_ticker(symbol=Crypto2)['price'])) * float(client.get_symbol_ticker(symbol=Crypto3)['price']))
    if tradevarbase2 > 1.0045:
        print("Trade!")
        print(client.get_server_time()['serverTime'])
        tradevarbase3 = float(float(tradevarbase2) - float(1.00225) * 100)
        if tradevarbase3 > 0:
            print("Gewinn: " + tradevarbase3 + " %")
        else:
            trader()
    elif tradevarbase2 < 0.9955:
        print("Trade!")
        tradevarbase3 = float(float(0.99775) - float(tradevarbase2) * 100)
        if tradevarbase3 > 0:
            print("Gewinn: " + tradevarbase3 + " %")
        else:
            trader()
    else:
        print(tradevarbase2)
        print("NPT")
    print("Runtime: " + str(float(client.get_server_time()['serverTime']) - float(time1)) + " MS \n ---")
while 1:
    trader()