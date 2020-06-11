from binance.client import Client
import time
sleep = time.sleep
import json
client = Client("O8Nrx1vRU3fy1Y1ocToiSaswNYrrg02c2dftryO1Mz3ZzK2CGG7OCMqrkJVqBWvt", "QpHsCcxAeaLqL0mts464NxSxtqCU8cHcbeE0aUIIFI3YUsi6yPAtCOv2woCXWotI")
br = "\n"
timeserv = client.get_server_time()
pricesraw = client.get_all_tickers()
print("First Price Load:\n" + json.dumps(pricesraw))
with open('pricesout.json', 'w') as outfile:
    json.dump(pricesraw, outfile)
def the_whole_program():
    timeservn = client.get_server_time()
    pricesrawn = client.get_all_tickers()
    print("\n\n\nCurrent Price Load: \n\nFormat 'JSON'\n\nServertime (UNIX): [" + str(timeservn) + "]\n\nCurrent Load: " + json.dumps(pricesrawn) + "\n\n")
    with open('pricesout.json', 'w') as outfile:
        json.dump(pricesrawn, outfile)
while True:
    the_whole_program()