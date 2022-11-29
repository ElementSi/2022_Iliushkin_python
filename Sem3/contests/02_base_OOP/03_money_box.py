class Coin:
    def __init__(self, value):
        self.value = value


class MoneyBox:
    def __init__(self):
        self.coin_list = []

    def add_coin(self, value):
        self.coin_list.append(Coin(value))

    def get_coins_number(self):
        return len(self.coin_list)

    def get_coins_value(self):
        return sum(coin.value for coin in self.coin_list)


m = MoneyBox()
# Добавили монетку достоинством 10
m.add_coin(10)
# Добавили монетку достоинством 5
m.add_coin(5)

# Ожидаем, что монеток внутри 2 штуки
print(m.get_coins_number())
# Ожидаем, что общее достоинство всех монеток 15
print(m.get_coins_value())
