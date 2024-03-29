import pandas as pd

data = [[0.990360, -1.131429, -1.065981, 0.855488],
        [0.493665, 0.589660, -0.432106, -0.240378],
        [-0.807992, -1.794176, -1.210304, 0.201295],
        [-0.270479, -1.121976, 0.459273, -0.178025],
        [0.188286, -0.931686, 1.959219, 0.387350],
        [2.252443, 0.848532, 0.925256, 1.014754]]

df = pd.DataFrame(data, columns=list('ABCD'))
print(df)

# Индекс (определяет, как будем обращаться к строкам)
# По умолчанию в нём номера строк
print("=================")
print(df.index)

# Обращение к отдельной "ячейке таблицы"
print("=================")
print(df.loc[0, 'A'])

# Создадим новый фрейм из тех же данных,
# но индекс теперь будет нестандартный
dates = pd.date_range('20200101', periods=6)
df2 = pd.DataFrame(data, index=dates, columns=list('ABCD'))

# Посмотрим на фрейм и его индекс
print("=================")
print(df2)
print("=================")
print(df2.index)

# И обратим внимание, как теперь выглядит обрашение к "ячейке таблицы"
print("=================")
print(df2.loc['20200101', 'A'])

"""
На этапе первого общения с pandas вряд ли нужны нестандартные индексы. Но стоит знать, что они бывают.
И при обращении через .loc нужно именно значение индекса, и оно может быть не равно номеру строки.
"""
