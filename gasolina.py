import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("gasolina.csv")

sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.lineplot(x="dia", y="venda", data=df, marker="o")

plt.title("Preço da Gasolina por Dia", fontsize=16)
plt.xlabel("Dia", fontsize=12)
plt.ylabel("Preço (R$)", fontsize=12)

plt.savefig("gasolina.png", format="png")
plt.close()
