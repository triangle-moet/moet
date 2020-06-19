import json
from binance.client import Client
client = Client("O8Nrx1vRU3fy1Y1ocToiSaswNYrrg02c2dftryO1Mz3ZzK2CGG7OCMqrkJVqBWvt", "QpHsCcxAeaLqL0mts464NxSxtqCU8cHcbeE0aUIIFI3YUsi6yPAtCOv2woCXWotI")
def the_whole_program():
    Crypto = "ETHBTC"
    price = client.get_symbol_ticker(symbol=Crypto)
    with open(Crypto + '.moet', 'w') as outfile:
        json.dump(price, outfile)
while True:
    the_whole_program()