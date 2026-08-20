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
- Calculate supporting findings for the required analysis questions.
"""
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.ticker import StrMethodFormatter



# Path to the supplied house price dataset.
DATA_FILE = "data/house_prices.csv"
FIGURES_DIR = "output/figures"
SORTED_DATA_FILE = "output/sorted_house_prices.csv"
PDF_REPORT_FILE = "output/house_price_technical_report.pdf"

SUBURB_NAMES = {
    "TW": "Toowong",
    "WM": "Wynnum",
    "HH": "Highgate Hill",
    "SF": "Springfield",
    "NL": "North Lake",
}


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
    # Scatter Plot - Price and Demand Across Suburbs
    # -----------------------------------------------------------------------

    plt.figure(figsize=(10, 6))

    # Preserve the suburb order used in the assignment dataset.
    suburb_order = ["TW", "WM", "HH", "SF", "NL"]

    suburb_labels = [
        SUBURB_NAMES[suburb]
        for suburb in suburb_order
    ]

    # Convert suburb codes into numerical positions for the x-axis.
    suburb_positions = {
        suburb: index
        for index, suburb in enumerate(suburb_order)
    }

    # Slightly separate demand categories so overlapping points remain visible.
    demand_offsets = {
        "General": -0.08,
        "High": 0.08,
    }

    for demand_level in ["General", "High"]:
        demand_data = data[data["demand"] == demand_level]

        x_positions = (
            demand_data["suburb"].map(suburb_positions)
            + demand_offsets[demand_level]
        )

        plt.scatter(
            x_positions,
            demand_data["price"],
            label=f"{demand_level} Demand",
            alpha=0.7,
        )

    plt.title("House Prices and Demand Levels Across Suburbs")
    plt.xlabel("Suburb")
    plt.ylabel("House Price ($)")

    plt.xticks(
        range(len(suburb_order)),
        suburb_labels,
    )

    plt.gca().yaxis.set_major_formatter(
        StrMethodFormatter("${x:,.0f}")
    )

    plt.legend()
    plt.tight_layout()

    plt.savefig(
        f"{FIGURES_DIR}/suburb_demand_scatter_plot.png",
        dpi=300,
    )

    plt.close()

def export_sorted_data(data, statistics):
    """
    Sort the house price dataset in ascending order and export it to CSV.

    The exported dataset includes the median, lowest, and highest house
    prices required by the assignment.

    Args:
        data (pandas.DataFrame): House price dataset.
        statistics (dict): Calculated house price statistics.

    Returns:
        pandas.DataFrame: The sorted dataset that was exported.
    """

    # Preserve the original dataset structure while creating a separate
    # DataFrame for the sorted CSV output.
    sorted_data = (
        data[["id", "price", "suburb", "demand"]]
        .sort_values(by="price", ascending=True)
        .copy()
    )

    # Add the required summary statistics as numerical columns so they
    # remain available alongside every record in the exported CSV.
    sorted_data["median_price"] = statistics["median_price"]
    sorted_data["lowest_price"] = statistics["lowest_price"]
    sorted_data["highest_price"] = statistics["highest_price"]

    # Ensure the output directory exists before saving the CSV file.
    Path(SORTED_DATA_FILE).parent.mkdir(parents=True, exist_ok=True)

    sorted_data.to_csv(
        SORTED_DATA_FILE,
        index=False,
    )

    print(f"\nSorted dataset saved to: {SORTED_DATA_FILE}")

    return sorted_data

def generate_pdf_report(data, statistics):
    """
    Generate the technical PDF report required for Problem 1.

    The report contains the calculated house price statistics and the
    four required visualisations.

    Args:
        data (pandas.DataFrame): Analysed house price dataset.
        statistics (dict): Calculated house price statistics.
    """

    # Ensure the output directory exists before creating the report.
    Path(PDF_REPORT_FILE).parent.mkdir(parents=True, exist_ok=True)

    figure_files = [
        f"{FIGURES_DIR}/price_category_pie_chart.png",
        f"{FIGURES_DIR}/price_distribution_bar_chart.png",
        f"{FIGURES_DIR}/demand_price_histogram.png",
        f"{FIGURES_DIR}/suburb_demand_scatter_plot.png",
    ]

    with PdfPages(PDF_REPORT_FILE) as pdf:
        # -------------------------------------------------------------------
        # Page 1 - Statistical Summary
        # -------------------------------------------------------------------

        figure = plt.figure(figsize=(8.27, 11.69))
        axis = figure.add_subplot(111)
        axis.axis("off")

        figure.suptitle(
            "House Price Data Analysis - Technical Report",
            fontsize=18,
            fontweight="bold",
            y=0.95,
        )

        summary_text = (
            "Dataset Summary\n\n"
            f"Total houses: {len(data)}\n"
            f"Median house price: ${statistics['median_price']:,.2f}\n"
            f"Lowest house price: ${statistics['lowest_price']:,.2f}\n"
            f"Highest house price: ${statistics['highest_price']:,.2f}\n"
            f"Percentage below median: "
            f"{statistics['below_median_percentage']:.2f}%\n"
            f"Percentage above median: "
            f"{statistics['above_median_percentage']:.2f}%"
        )

        axis.text(
            0.10,
            0.80,
            summary_text,
            fontsize=13,
            verticalalignment="top",
            linespacing=1.8,
        )

        pdf.savefig(figure)
        plt.close(figure)

        # -------------------------------------------------------------------
        # Pages 2-5 - Required Visualisations
        # -------------------------------------------------------------------

        for file_path in figure_files:
            image = plt.imread(file_path)

            figure, axis = plt.subplots(figsize=(11.69, 8.27))

            axis.imshow(image)
            axis.axis("off")

            figure.tight_layout()

            pdf.savefig(
                figure,
                bbox_inches="tight",
            )

            plt.close(figure)

    print(f"\nTechnical PDF report saved to: {PDF_REPORT_FILE}")


def calculate_analysis_findings(data, statistics):
    """
    Calculate supporting findings for the Problem 1 analysis questions.

    The results provide quantitative evidence for analysing suburb price
    patterns, the overall price distribution, and differences between
    demand levels.

    Args:
        data (pandas.DataFrame): Analysed house price dataset.
        statistics (dict): Previously calculated house price statistics.

    Returns:
        dict: Supporting findings used for the written analysis.
    """

    prices = data["price"]
    median_price = statistics["median_price"]

    # Select only houses priced above the overall median, then count
    # how many occur in each suburb.
    above_median_by_suburb = (
        data[data["price"] > median_price]
        .groupby("suburb")
        .size()
        .sort_values(ascending=False)
    )

    # Identify the suburb code with the largest number of houses
    # priced above the overall median.
    top_suburb_code = above_median_by_suburb.idxmax()
    top_suburb_count = int(above_median_by_suburb.max())

    # Calculate descriptive statistics that help explain the shape
    # and spread of the overall house price distribution.
    mean_price = prices.mean()
    standard_deviation = prices.std()
    first_quartile = prices.quantile(0.25)
    third_quartile = prices.quantile(0.75)
    skewness = prices.skew()

    # Compare price statistics between General and High demand groups.
    demand_summary = (
        data.groupby("demand")["price"]
        .agg(["count", "mean", "median", "min", "max"])
        .round(2)
    )

    findings = {
        "above_median_by_suburb": above_median_by_suburb,
        "top_suburb_code": top_suburb_code,
        "top_suburb_name": SUBURB_NAMES[top_suburb_code],
        "top_suburb_count": top_suburb_count,
        "mean_price": mean_price,
        "standard_deviation": standard_deviation,
        "first_quartile": first_quartile,
        "third_quartile": third_quartile,
        "skewness": skewness,
        "demand_summary": demand_summary,
    }

    return findings

def display_analysis_findings(findings):
    """
    Display supporting findings for the Problem 1 analysis questions.

    Args:
        findings (dict): Calculated supporting analysis findings.
    """

    print("\nAdditional Analysis Findings:")

    print("\nHouses above the overall median by suburb:")

    for suburb_code, count in findings["above_median_by_suburb"].items():
        suburb_name = SUBURB_NAMES[suburb_code]
        print(f"{suburb_name}: {count}")

    print(
        "\nSuburb with the most houses above the median: "
        f"{findings['top_suburb_name']} "
        f"({findings['top_suburb_count']} houses)"
    )

    print("\nOverall Price Distribution:")
    print(f"Mean price: ${findings['mean_price']:,.2f}")
    print(
        f"Standard deviation: "
        f"${findings['standard_deviation']:,.2f}"
    )
    print(
        f"First quartile (Q1): "
        f"${findings['first_quartile']:,.2f}"
    )
    print(
        f"Third quartile (Q3): "
        f"${findings['third_quartile']:,.2f}"
    )
    print(f"Skewness: {findings['skewness']:.3f}")

    print("\nPrice Statistics by Demand Level:")
    print(findings["demand_summary"])

def main():
    """
    Run the House Price Data Analysis application.
    """
    data = load_data(DATA_FILE)

    inspect_and_validate_data(data)

    statistics = calculate_statistics(data)
    display_statistics(statistics)

    analysis_findings = calculate_analysis_findings(
    data,
    statistics,
    )

    display_analysis_findings(analysis_findings)

    data = categorise_house_prices(data)
    display_category_distribution(data)

    create_visualisations(data)

    export_sorted_data(data, statistics)
    generate_pdf_report(data, statistics)

if __name__ == "__main__":
    main()