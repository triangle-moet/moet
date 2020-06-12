from binance.client import Client
import time
import winsound
s = winsound.PlaySound
sleep = time.sleep
client = Client("O8Nrx1vRU3fy1Y1ocToiSaswNYrrg02c2dftryO1Mz3ZzK2CGG7OCMqrkJVqBWvt", "QpHsCcxAeaLqL0mts464NxSxtqCU8cHcbeE0aUIIFI3YUsi6yPAtCOv2woCXWotI")
br = "\n"
eth = 1
def the_whole_program():
    Crypto1 = "ETHBTC"
    price = client.get_symbol_ticker(symbol=Crypto1)
    price = str(price)
    price = price.replace("'}", "")
    price = price.replace("{'symbol': '" + Crypto1 + "', 'price': '", "")
    Crypto2 = "ADABTC"
    price2 = client.get_symbol_ticker(symbol=Crypto2)
    price2 = str(price2)
    price2 = price2.replace("'}", "")
    price2 = price2.replace("{'symbol': '" + Crypto2 + "', 'price': '", "")
    Crypto3 = "ADAETH"
    price3 = client.get_symbol_ticker(symbol=Crypto3)
    price3 = str(price3)
    price3 = price3.replace("'}", "")
    price3 = price3.replace("{'symbol': '" + Crypto3 + "', 'price': '", "")
    btc = float(price) * float(eth)
    ada = float(btc) / float(price2)
    eth2 = float(ada) * float(price3)
    print(Crypto1 + ": " + price)
    print(Crypto2 + ": " + price2)
    print(Crypto3 + ": " + price3)
    print("___________")
    if eth2 > 1.003:
        print("Trade")
        print("\n")
        print("ETH: " + str(eth))
        print("ETH2: " + str(eth2))
        s('sound.wav', winsound.SND_FILENAME)
        print("\nTausche ETH in BTC - BTC in ADA - ADA in ETH")
    elif eth2 < 0.997:
        print("Trade")
        print("\n")
        print("ETH: " + str(eth))
        print("ETH2: " + str(eth2))
        s('sound.wav', winsound.SND_FILENAME)
        print("\nTausche ETH in ADA - ADA in BTC - BTC in ETH")
    else:
        print("No profitable trading")
    print("_____________________________________________" + br)


while True:
    the_whole_program()