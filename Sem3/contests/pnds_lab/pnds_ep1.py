import pandas as pd

trans_frame = pd.read_csv('transactions.csv', sep=',', index_col='ID')

trans_frame = trans_frame[trans_frame['STATUS'] == 'OK'].sort_values(by='SUM', ascending=False)

print('The three largest payments:')
for i in range(3):
    print(trans_frame.iloc[i, 0] + ' ' + str(trans_frame.iloc[i, 2]))

trans_frame = trans_frame.groupby('CONTRACTOR').sum()

print('\nThe total sum in favor of company Umbrella, Inc:\n' + str(trans_frame.loc['Umbrella, Inc', 'SUM']))
