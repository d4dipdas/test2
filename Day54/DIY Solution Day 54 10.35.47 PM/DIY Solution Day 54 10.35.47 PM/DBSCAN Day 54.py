import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

df = pd.read_csv('Mall_Customers.csv')

correlation_matrix = df.corr()
least_correlated_column = correlation_matrix.min().idxmin()
df.drop(least_correlated_column, axis=1, inplace=True)

plt.subplots(figsize=(12,9))
sns.heatmap(correlation_matrix ,annot=True)
plt.title('Correlation between CustomerID, Age, Annual Income, Spending Score', fontsize = 20)
plt.show()

df_encoded = pd.get_dummies(df, columns=['Gender'])

dbscan = DBSCAN(eps=12.5, min_samples=4)
clusters = dbscan.fit_predict(df_encoded)

cluster_sizes = pd.Series(clusters).value_counts()
outliers_size = cluster_sizes[-1]
print("Cluster sizes:")
print(cluster_sizes)
print("Size of outliers' cluster:", outliers_size)


plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_encoded, x='Annual Income (k$)', y='Spending Score (1-100)', hue=clusters, palette='viridis')
plt.title('Annual Income vs. Spending Score')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()
