import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas._libs import index

tp = pd.read_csv('./sup_branch/cycle_trend.csv')
df = pd.DataFrame(tp)

x = []
for i in range(len(df)):
    if i%7 == 0:
        x.append((df['date'][i]))

y = []
for i in range(len(df)):
    if i%7 == 0:
        y.append((df['traffic'][i]))
print(x)
print(y)

plt.title("cycle_traffic_trend", fontweight='bold', fontsize = 12)
plt.xlabel("date", fontweight='bold', fontsize = 12)
plt.xticks(rotation=90)
plt.ylabel("traffic", fontweight='bold', fontsize = 12)

plt.plot(x, y, c='red')
plt.show()

