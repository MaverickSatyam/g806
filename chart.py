# chart.py
# Email: 23f3003273@ds.study.iitm.ac.in
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate realistic synthetic monthly revenue data
months = pd.date_range(start="2023-01-01", periods=12, freq="M")
np.random.seed(0)
revenue = 100000 + np.random.normal(0, 10000, size=12) + 10000*np.sin(np.linspace(0, 2*np.pi, 12))

df = pd.DataFrame({
    "Month": months,
    "Revenue": revenue
})

# Minimal, validator-friendly Seaborn lineplot
sns.set_style("whitegrid")
plt.figure(figsize=(8, 8))  # 512x512 pixels
sns.lineplot(data=df, x="Month", y="Revenue", marker="o")  # lineplot with marker

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (USD)")
plt.tight_layout()
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.show()
