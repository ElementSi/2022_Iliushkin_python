import csv
import btc_functions as btc

with open('BTC-USD.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)

for i in range(1, len(data)):
    for j in range(1, 7):
        data[i][j] = float(data[i][j])

avg_list = btc.count_average(data, 700)
w_avg_list = btc.count_w_average(data, 700)
trend_list = btc.count_trend(avg_list, w_avg_list)

print(avg_list)
print(w_avg_list)
print(trend_list)
print(btc.count_profit(trend_list, data, 100, 0, 700))
