def count_average(data, num_of_days=5):
    last_open_list = [x[1] for x in data[-1:-num_of_days - 5:-1]]
    last_open_list.reverse()
    last_avg_list = [sum(last_open_list[i:i + 5:]) / 5 for i in range(0, num_of_days)]
    return last_avg_list


def count_w_average(data, num_of_days=5):
    last_open_list = [x[1] for x in data[-1:-num_of_days - 5:-1]]
    last_open_list.reverse()
    last_w_avg_list = []
    for i in range(num_of_days):
        w_sum = 0
        for j in range(5):
            w_sum += last_open_list[i + j] * (j + 1)
        last_w_avg_list.append(w_sum / 15)

    return last_w_avg_list


def count_trend(avg_list, w_avg_list):
    trend_list = []
    for i in range(len(avg_list)):
        trend_list.append(w_avg_list[i] < avg_list[i])

    return trend_list


def count_profit(trend_list, data, btc_ini=100, usd_ini=0, num_of_days=5):
    last_open_list = [x[1] for x in data[-1:-num_of_days - 1:-1]]
    last_open_list.reverse()
    btc = btc_ini
    usd = usd_ini

    for i in range(num_of_days):
        if trend_list[i]:
            btc += usd / last_open_list[i]
            usd = 0

        else:
            usd += btc * last_open_list[i]
            btc = 0

    return (btc_ini * last_open_list[0] + usd_ini) - (btc * last_open_list[0] + usd)
