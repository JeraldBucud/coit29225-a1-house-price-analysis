"""
COIT29225 Neural Networks & Deep Learning
Assignment 1 - Problem 1

House Price Data Analysis and Visualisation

This program analyses the supplied Brisbane house price dataset.

The program will:
- Load and inspect the house price dataset.
- Validate the dataset before analysis.
- Calculate required house price statistics.
- Categorise houses according to price ranges.
- Generate the required data visualisations.
- Export the sorted house price dataset.
- Generate a technical PDF report.
"""

import pandas as pd


# Path to the supplied house price dataset.
DATA_FILE = "data/house_prices.csv"


def load_data(file_path):
    """
    Load the house price dataset from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pandas.DataFrame: The loaded house price dataset.
    """
    data = pd.read_csv(file_path)
    return data


def inspect_and_validate_data(data):
    """
    Inspect the dataset and check for common data quality issues.

    The function displays the dataset structure, data types,
    missing values, duplicate rows, suburb values, and demand values.

    Args:
        data (pandas.DataFrame): House price dataset to inspect.
    """
    print("\nFirst five records:")
    print(data.head())

    print("\nDataset dimensions:")
    print(data.shape)

    print("\nColumn names:")
    print(data.columns)

    print("\nData types:")
    print(data.dtypes)

    print("\nMissing values:")
    print(data.isnull().sum())

    print("\nDuplicate rows:")
    print(data.duplicated().sum())

    print("\nSuburb values:")
    print(data["suburb"].unique())

    print("\nDemand values:")
    print(data["demand"].unique())


def main():
    """
    Run the House Price Data Analysis application.
    """
    data = load_data(DATA_FILE)

    inspect_and_validate_data(data)


if __name__ == "__main__":
    main()