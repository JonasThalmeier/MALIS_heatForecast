import matplotlib.pyplot as plt
import numpy as np

# Data
percentiles = [50, 60, 70, 80, 90, 95]
accuracy = [0.7645, 0.7530, 0.7452, 0.7494, 0.8302, 0.9164]
precision = [0.8075, 0.7804, 0.7531, 0.6656, 0.4024, 0.1898]
recall = [0.7965, 0.7010, 0.5323, 0.2781, 0.0595, 0.0076]
f1_score = [0.8020, 0.7386, 0.6238, 0.3923, 0.1037, 0.0147]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(percentiles, accuracy, label="Accuracy", marker="o")
plt.plot(percentiles, precision, label="Precision", marker="o")
plt.plot(percentiles, recall, label="Recall", marker="o")
plt.plot(percentiles, f1_score, label="F1 Score", marker="o")

# Labels and Title
plt.xlabel("Percentile")
plt.ylabel("Performance Metric")
plt.title("Model Performance vs Percentile")
plt.xticks(percentiles)
plt.legend()
plt.grid(True)

# Show plot
plt.tight_layout()
plt.savefig("performance_vs_percentile.png", dpi=300)
plt.show()

