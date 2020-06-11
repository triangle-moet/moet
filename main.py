from binance.client import Client
import time
sleep = time.sleep
import json
client = Client("O8Nrx1vRU3fy1Y1ocToiSaswNYrrg02c2dftryO1Mz3ZzK2CGG7OCMqrkJVqBWvt", "QpHsCcxAeaLqL0mts464NxSxtqCU8cHcbeE0aUIIFI3YUsi6yPAtCOv2woCXWotI")
br = "\n\r"
Crypto = "BNBETH"
def the_whole_program():
    price = client.get_symbol_ticker(symbol=Crypto)
    price = str(price)
    price = price.replace("'}", "")
    price = price.replace("{'symbol': '" + Crypto + "', 'price': '", "")
    timeserv = client.get_server_time()
    timeserv1 = str(timeserv)
    timeserv2 = timeserv1.replace("{'serverTime': ", "")
    timeserv = timeserv2.replace("}", "")
    printvar = br + br + br + br + "Servertime (UNIX): " + timeserv + br + "Symbol: "+ Crypto + br + "Current Price: " + price
    print(printvar)
    with open(Crypto + '.json', 'w') as outfile:
        json.dump(printvar, outfile)
while True:
    the_whole_program()




