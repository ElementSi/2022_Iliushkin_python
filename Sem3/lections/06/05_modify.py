import pandas as pd

data = {'A': 1.1,
        'B': pd.Timestamp('20200901'),
        'C': 111,
        'D': [42 * i for i in range(4)],
        'E': 'foo'}

df = pd.DataFrame(data)
print(df)

# Можно присвоить отдельное значение
print("=================")
df.loc[0, 'D'] = -42
print(df)

# Или, например, столбец целиком
print("=================")
df.loc[:, 'D'] = [i for i in range(4)]
print(df)
