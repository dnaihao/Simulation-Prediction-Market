import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./example_retail_sales.csv")
plt.plot(df["ds"], df["y"])
plt.show()