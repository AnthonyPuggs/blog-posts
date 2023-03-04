import pandas as pd
import scipy
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (11, 5)

df = pd.read_csv('GreedflationData.csv')
# Data is from https://www.abs.gov.au/statistics/economy/business-indicators/business-indicators-australia/latest-release

fig, ax = plt.subplots(figsize=(10, 5))

x1 = df['Quarter']
y1 = df['Wages']

plt.plot(x1, y1, label = "Seasonally adjusted Wages")

x2 = df['Quarter']
y2 = df['CGOP']

plt.plot(x2, y2, label = "Seasonally adjusted Company Gross Operating Profits")

plt.xlabel('Date')
plt.ylabel('Current Prices ($ Millions)')
plt.suptitle('Wages and Company Gross Operating Profits across all Australian industries', y=0.96)

plt.legend()

plt.annotate('12.4% decrease in profits',
            xy=(x2[12], y2[12]),
            xycoords='data',
            xytext=(0, -53), 
            textcoords='offset points',
            arrowprops=dict(arrowstyle="-"),
            ha='right') 

text = "Graph created by @AnthonyPuggs using ABS data"
text_x = 0.595
text_y = -.08

plt.annotate(text, xy=(text_x, 0), xycoords='axes fraction',
            xytext=(text_x, text_y), textcoords='axes fraction',
            fontsize=9, ha='left', va='top')

plt.grid(axis = 'y')
plt.savefig('AusWageCGOP.png')
plt.show()
