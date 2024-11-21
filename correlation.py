import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('./irisDataset.csv')
numeric_data = data.select_dtypes(include=[float, int])
correlation_matrix = numeric_data.corr()
print(correlation_matrix)
correlation_matrix_unstacked = correlation_matrix.abs().unstack()
sorted_correlation = correlation_matrix_unstacked.sort_values(ascending=False)
sorted_correlation = sorted_correlation[sorted_correlation != 1]
strongest_pair = sorted_correlation.idxmax()
sns.pairplot(data, hue="variety", markers=["o", "s", "D"])
plt.show()
print(f"\nThe two attributes showing the strongest linear relationship are: {strongest_pair}")
