import json

btc = open("btc.json")
btc_dicts = json.load(btc)

sum_ask = 0
counter = 0
for btc_dict in btc_dicts:
    if btc_dict['ask'] is not None:
        sum_ask += btc_dict['ask']
        counter += 1

print(sum_ask / counter)
