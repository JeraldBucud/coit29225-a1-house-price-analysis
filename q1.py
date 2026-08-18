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
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

# Path to the supplied house price dataset.
DATA_FILE = "data/house_prices.csv"
FIGURES_DIR = "output/figures"


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

def categorise_price(price):
    """
    Categorise a house according to its selling price.

    Args:
        price (int or float): Selling price of the house.

    Returns:
        str: The corresponding house price category.
    """

    if price < 500000:
        return "Entry Level"
    elif price <= 800000:
        return "Economical Level"
    elif price <= 1400000:
        return "Middle-Class Level"
    else:
        return "Premium Level"

def categorise_house_prices(data):
    """
    Add a price category to each house in the dataset.

    Args:
        data (pandas.DataFrame): House price dataset.

    Returns:
        pandas.DataFrame: Dataset containing an additional price_category column.
    """

    data["price_category"] = data["price"].apply(categorise_price)

    return data

def display_category_distribution(data):
    """
    Display the number of houses in each price category.

    Args:
        data (pandas.DataFrame): Categorised house price dataset.
    """

    print("\nHouse Price Categories:")
    print(data["price_category"].value_counts())

def create_visualisations(data):
    """
    Create and save the four visualisations required for Problem 1.

    The generated figures include:
    - House price category pie chart.
    - House price category bar chart.
    - Demand-level price histogram.
    - Price and demand scatter plot across suburbs.

    Args:
        data (pandas.DataFrame): Categorised house price dataset.
    """

    # Ensure the output directory exists before attempting to save figures.
    Path(FIGURES_DIR).mkdir(parents=True, exist_ok=True)

    category_order = [
        "Entry Level",
        "Economical Level",
        "Middle-Class Level",
        "Premium Level",
    ]

    category_counts = (
        data["price_category"]
        .value_counts()
        .reindex(category_order)
    )

    # -----------------------------------------------------------------------
    # Pie Chart - House Price Category Distribution
    # -----------------------------------------------------------------------

    plt.figure(figsize=(8, 6))

    plt.pie(
        category_counts,
        labels=category_counts.index,
        autopct="%1.1f%%",
        startangle=90,
    )

    plt.title("House Price Category Distribution")
    plt.tight_layout()

    plt.savefig(
        f"{FIGURES_DIR}/price_category_pie_chart.png",
        dpi=300,
    )

    plt.close()

    # -----------------------------------------------------------------------
    # Bar Chart - House Price Distribution by Category
    # -----------------------------------------------------------------------

    plt.figure(figsize=(9, 6))

    bars = plt.bar(
    category_counts.index,
    category_counts.values,
    )

    plt.bar_label(bars)

    plt.title("House Price Distribution by Category")
    plt.xlabel("Price Category")
    plt.ylabel("Number of Houses")

    plt.xticks(rotation=15)
    plt.tight_layout()

    plt.savefig(
        f"{FIGURES_DIR}/price_distribution_bar_chart.png",
        dpi=300,
    )

    plt.close()

    high_demand_prices = data.loc[
        data["demand"] == "High",
        "price",
    ]

    general_demand_prices = data.loc[
        data["demand"] == "General",
        "price",
    ]

    # -----------------------------------------------------------------------
    # Histogram - Price Distribution by Demand Level
    # -----------------------------------------------------------------------

    plt.figure(figsize=(9, 6))

    plt.hist(
        [high_demand_prices, general_demand_prices],
        bins=10,
        label=["High Demand", "General Demand"],
        alpha=0.7,
    )

    plt.title("House Price Distribution by Demand Level")
    plt.xlabel("House Price ($)")
    plt.gca().xaxis.set_major_formatter(
    StrMethodFormatter("${x:,.0f}")
    )
    plt.ylabel("Number of Houses")
    plt.legend()

    plt.tight_layout()

    plt.savefig(
        f"{FIGURES_DIR}/demand_price_histogram.png",
        dpi=300,
    )

    plt.close()

    # -----------------------------------------------------------------------
    # Scatter Plot - House Price and Demand Level Across Suburbs
    # -----------------------------------------------------------------------

    plt.figure(figsize=(10, 6))

    suburb_order = ["TW", "WM", "HH", "SF", "NL"]

    suburb_names = {
        "TW": "Toowong",
        "WM": "Wynnum",
        "HH": "Highgate Hill",
        "SF": "Springfield",
        "NL": "North Lake",
    }

    # Convert the categorical demand values to numerical positions so they
    # can be displayed on the scatter plot's y-axis.
    demand_positions = {
        "General": 0,
        "High": 1,
    }

    for suburb in suburb_order:
        suburb_data = data[data["suburb"] == suburb]

        y_positions = suburb_data["demand"].map(demand_positions)

        plt.scatter(
            suburb_data["price"],
            y_positions,
            label=suburb_names[suburb],
            alpha=0.7,
        )

    plt.title("House Price and Demand Level Across Suburbs")
    plt.xlabel("House Price ($)")
    plt.ylabel("Demand Level")

    plt.yticks(
        [0, 1],
        ["General Demand", "High Demand"],
    )

    plt.gca().xaxis.set_major_formatter(
        StrMethodFormatter("${x:,.0f}")
    )

    plt.legend(title="Suburb")
    plt.tight_layout()

    plt.savefig(
        f"{FIGURES_DIR}/suburb_demand_scatter_plot.png",
        dpi=300,
    )

    plt.close()

def main():
    """
    Run the House Price Data Analysis application.
    """
    data = load_data(DATA_FILE)

    inspect_and_validate_data(data)

    statistics = calculate_statistics(data)
    display_statistics(statistics)

    data = categorise_house_prices(data)
    display_category_distribution(data)

    create_visualisations(data)

if __name__ == "__main__":
    main()