import pandas as pd

games = input()
rates = input()

games_frame = pd.read_csv(games, sep=';', index_col='id')

rates_frame = pd.read_csv(rates, sep=';', index_col='id').groupby('id').mean()

rg_frame = pd.merge(games_frame, rates_frame, on='id')
rg_frame = rg_frame.sort_values(by='mark', ascending=False)
rg_frame = rg_frame.reset_index(drop=True)

for i in range(3):
    print(rg_frame.iloc[i, 0] + ' ' + str("%.3f" % rg_frame.iloc[i, 2]))

rg_frame = rg_frame.assign(gg=rg_frame.mark > 8.0)
rg_frame['gg'] = rg_frame['gg'].astype('int')
rg_frame = rg_frame.groupby('company').sum()
rg_frame = rg_frame.sort_values(by='gg', ascending=False)

print(rg_frame.index[0] + ' ' + str(rg_frame.iloc[0, 1]))

