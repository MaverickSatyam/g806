import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.linspace(0, 10, 50)
y = np.sin(x)

# Create the lineplot
sns.set(style="whitegrid")
plt.figure(figsize=(5.12, 5.12), dpi=100)  # 512x512 pixels

sns.lineplot(x=x, y=y)

plt.title("Sine Wave Lineplot")
plt.xlabel("X")
plt.ylabel("sin(X)")

plt.tight_layout()
plt.savefig("chart.png")
