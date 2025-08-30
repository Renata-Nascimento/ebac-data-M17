# código de geração do gráfico
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

gas = pd.read_csv('gasolina.csv')
sns.lineplot(x='dia', y='venda', data=gas)
plt.savefig('gasolina.png')