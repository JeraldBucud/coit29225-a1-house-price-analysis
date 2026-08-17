import pandas as pd

data = pd.read_csv("data/house_prices.csv")

print(data.head())

print("\nDataset dimensions:")
print(data.shape)

print("\nColumn names:")
print(data.columns)

print("\nData types:")
print(data.dtypes)

print("\nMissing values:")
print(data.isnull().sum())

print("\nMissing values:")
print(data.isnull().sum())

print("\nDuplicate rows:")
print(data.duplicated().sum())

print("\nSuburb values:")
print(data["suburb"].unique())

print("\nDemand values:")
print(data["demand"].unique())