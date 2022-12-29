import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('.\Iris.csv')
x=df['Species']
y=df['Id']
plt.pie(y,labels=x)
plt.show()

