# chart.py
# Email: 23f3003273@ds.study.iitm.ac.in
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic monthly revenue data
months = pd.date_range(start="2023-01-01", periods=12, freq="M")
np.random.seed(0)
revenue = 100000 + np.random.normal(0, 10000, size=12) + 10000*np.sin(np.linspace(0, 2*np.pi, 12))

df = pd.DataFrame({
    "Month": months,
    "Revenue": revenue
})

# Set Seaborn style
sns.set_style("whitegrid")

# Create figure exactly 512x512 pixels
fig = plt.figure(figsize=(512/100, 512/100), dpi=100)  # 512px / 100 dpi = 5.12 inches
ax = sns.lineplot(data=df, x="Month", y="Revenue", marker="o")

# Titles and labels
ax.set_title("Monthly Revenue")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue (USD)")

# Save chart exactly 512x512 pixels
fig.savefig("chart.png", dpi=100)  # 5.12 in * 100 dpi = 512px
plt.close(fig)
