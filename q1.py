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


def calculate_statistics(data):
    """
    Calculate the house price statistics required for Problem 1.

    Args:
        data (pandas.DataFrame): House price dataset containing a price column.

    Returns:
        dict: A dictionary containing the median price, lowest price,
        highest price, and percentages of houses below and above
        the median price.
    """

    # Select the price column once so it can be reused for all calculations.
    prices = data["price"]

    median_price = prices.median()
    lowest_price = prices.min()
    highest_price = prices.max()

    # Strict comparisons are used because the assignment asks specifically
    # for houses priced below and above the median.
    below_median_count = (prices < median_price).sum()
    above_median_count = (prices > median_price).sum()

    total_houses = len(data)

    below_median_percentage = (below_median_count / total_houses) * 100
    above_median_percentage = (above_median_count / total_houses) * 100

    statistics = {
        "median_price": median_price,
        "lowest_price": lowest_price,
        "highest_price": highest_price,
        "below_median_percentage": below_median_percentage,
        "above_median_percentage": above_median_percentage,
    }

    return statistics

def display_statistics(statistics):
    """
    Display the calculated house price statistics in a readable format.

    Args:
        statistics (dict): Calculated house price statistics.
    """
    print("\nHouse Price Statistics:")
    print(f"Median house price: ${statistics['median_price']:,.2f}")
    print(f"Lowest house price: ${statistics['lowest_price']:,.2f}")
    print(f"Highest house price: ${statistics['highest_price']:,.2f}")
    print(
        f"Percentage below median: "
        f"{statistics['below_median_percentage']:.2f}%"
    )
    print(
        f"Percentage above median: "
        f"{statistics['above_median_percentage']:.2f}%"
    )



def main():
    """
    Run the House Price Data Analysis application.
    """
    data = load_data(DATA_FILE)

    inspect_and_validate_data(data)

    statistics = calculate_statistics(data)

    display_statistics(statistics)


if __name__ == "__main__":
    main()