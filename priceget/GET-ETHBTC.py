from binance.client import Client
client = Client("O8Nrx1vRU3fy1Y1ocToiSaswNYrrg02c2dftryO1Mz3ZzK2CGG7OCMqrkJVqBWvt", "QpHsCcxAeaLqL0mts464NxSxtqCU8cHcbeE0aUIIFI3YUsi6yPAtCOv2woCXWotI")
Crypto = "ETHBTC"

def the_whole_program():
    print(client.get_symbol_ticker(symbol=Crypto)['price'])
while True:
    the_whole_program()