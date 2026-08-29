import pandas as pd
import matplotlib.pyplot as plt

orders = pd.read_csv("data/orders.csv")
orders["order_date"] = pd.to_datetime(orders["order_date"], errors="coerce")

daily_orders = orders.groupby(orders["order_date"].dt.date).size()
daily_orders.plot(figsize=(10, 4), title="Daily Order Volume")
plt.xlabel("Date")
plt.ylabel("Orders")
plt.tight_layout()
plt.show()
