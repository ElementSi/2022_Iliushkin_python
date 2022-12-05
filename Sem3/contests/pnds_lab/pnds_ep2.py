import pandas as pd
import matplotlib.pyplot as plt

flights_frame = pd.read_csv('flights.csv', sep=',', index_col='ID')

flights_frame = flights_frame.assign(FLIGHTS=1).groupby('CARGO').sum()

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
fig.set_size_inches(10, 6)
plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.95,
                    top=0.9,
                    wspace=0.4)

ax1.bar(flights_frame.index, flights_frame['FLIGHTS'], color='#00D7CF')
ax1.set_title('Total flights')

ax2.bar(flights_frame.index, flights_frame['PRICE'], color='#66D700')
ax2.set_title('Total price')

ax3.bar(flights_frame.index, flights_frame['WEIGHT'], color='#0700D7')
ax3.set_title('Total weight')

plt.savefig('flights.png', dpi=400)
