# Matplotlib with pandas

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./president_heights.csv")

fig, ax = plt.subplots()
ax.plot(df['order'], df['geight(cm)'], label="height")

ax.set_xlabel('order')
ax.set_ylabel('height(cm)')
ax.legend()