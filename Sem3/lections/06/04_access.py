import pandas as pd

data = {'A': 1.1,
        'B': pd.Timestamp('20200901'),
        'C': 111,
        'D': [42 * i for i in range(4)],
        'E': 'foo'}

df = pd.DataFrame(data)

# Посмотрим весь фрейм
print(df)

# Выборки средствами .loc, при обращении через .loc используются *ключи*.
# Можно использовать отдельные значения, списки, диапазоны.

print("=== .loc access ===")

# Заданная пара строк, все столбцы
# (обратите внимание, что последний элемент включён в выборку)
print("=================")
print(df.loc[1:2])

# Заданный столбец, все строки
print("=================")
print(df.loc[:, 'D'])

# Заданная пара строк, избранные столбцы
print("=================")
print(df.loc[1:2, ['A', 'D']])

# Конкретная "ячейка"
print("=================")
print(df.loc[1, 'A'])

# То же самое, но .at вместо .loc
# (умеет работать только со скалярами, зато быстрее)
print("=================")
print(df.at[1, 'A'])

# Выборки средствами .iloc, при обращении через .iloc используются *номера*.
# Можно использовать отдельные значения, списки, диапазоны.

print("=== .iloc access ===")

# Заданная пара строк, все столбцы
# (обратите внимание, что последний элемент не включён в выборку)
print("=================")
print(df.iloc[1:3])

# Заданный столбец, все строки
print("=================")
print(df.iloc[:, 3])

# Заданная пара строк, избранные столбцы
print("=================")
print(df.iloc[[0, 3], [0, 3]])

# Конкретная "ячейка"
print("=================")
print(df.iloc[1, 3])

# То же самое, но .iat вместо .iloc
# (умеет работать только со скалярами, зато быстрее)
print("=================")
print(df.iat[1, 3])

print("=== 'default' access ===")

# Все значения из столбца
# (кажется, по умолчанию используется .loc ...)
print("=================")
print(df['D'])

# Ой, а так вообще нельзя
# print(df[0])

# А так можно, и это будут строки
print("=================")
print(df[0:2])

# "Просто скобочками" можно обращаться к столбцам по имени или к строкам по диапазонам.
# Просто потому что это частая хотелка и интуитивное ожидание.
# Но во избежание путаницы есть смысл использовать .loc или .iloc явно.
