import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('/content/irisDataset.csv')

numeric_data=data.select_dtypes(include=[float,int])
correlation_matrix=numeric_data.corr()

correlation_matrix_unstacked=correlation_matrix.unstack()
sorted_correlation=correlation_matrix_unstacked.sort_values(ascending=False)
sorted_correlation=sorted_correlation[sorted_correlation!=1]
print(sorted_correlation)

strongest_pair=sorted_correlation.idxmax()

print(f"Attributes strongest pair:{strongest_pair}")
