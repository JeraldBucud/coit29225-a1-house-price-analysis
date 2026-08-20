# COIT29225 Assignment 1 - House Price Analysis

Problem 1 of COIT29225 Neural Networks & Deep Learning Assignment 1.

This project implements a Python application for analysing and visualising
house price data from five Brisbane suburbs.

## Current Features

- Load the supplied house price CSV dataset
- Inspect the dataset structure
- Check column data types
- Check for missing values
- Check for duplicate records
- Inspect suburb categories
- Inspect demand categories
- Calculate the median house price
- Calculate the lowest and highest house prices
- Calculate the percentages of houses below and above the median price
- Categorise properties into Entry, Economical, Middle-Class, and Premium price levels
- Display the number of houses in each price category
- Generate and save the four required data visualisations
- Export the house price dataset sorted by price in ascending order
- Include the median, lowest, and highest prices in the exported CSV
- Calculate supporting statistical findings for the Problem 1 analysis questions
- Compare houses above the median across suburbs
- Calculate distribution measures including mean, quartiles, standard deviation, and skewness
- Compare house price statistics between General and High demand properties
- Generate the required technical PDF report

## Dataset

The supplied dataset contains 110 house records with four columns:

- `id`
- `price`
- `suburb`
- `demand`

The suburb codes used by the dataset are:

- `TW` - Toowong
- `WM` - Wynnum
- `HH` - Highgate Hill
- `SF` - Springfield
- `NL` - North Lake

The demand categories in the supplied dataset are:

- `General`
- `High`


## Statistical Analysis

The application calculates the following statistics from the supplied
house price dataset:

- Median house price
- Lowest house price
- Highest house price
- Percentage of houses priced below the median
- Percentage of houses priced above the median

The values are calculated dynamically from the CSV dataset rather than
being hard-coded in the program.

## Supporting Analysis

The application also calculates supporting statistical findings for the
Problem 1 analysis questions, including:

- Houses priced above the overall median by suburb
- Identification of the suburb with the most above-median properties
- Mean house price
- Standard deviation
- First and third quartiles
- Price distribution skewness
- Price statistics for General and High demand properties

These results provide quantitative evidence for the written analysis
rather than relying only on visual interpretation of the generated charts.



## House Price Categories

Properties are grouped into four price categories:

- **Entry Level:** Less than $500,000
- **Economical Level:** Up to $800,000 after the Entry Level range
- **Middle-Class Level:** Up to $1,400,000 after the Economical Level range
- **Premium Level:** Above $1,400,000

The supplied dataset does not contain properties priced exactly at the
boundary values of $500,000, $800,000, or $1,400,000.

## Generated Visualisations

The application generates four visualisations in `output/figures/`:

- `price_category_pie_chart.png` - Percentage distribution across the four price categories
- `price_distribution_bar_chart.png` - Number of houses in each price category
- `demand_price_histogram.png` - Comparison of house price distributions for High and General demand
- `suburb_demand_scatter_plot.png` - Relationship between house prices and demand levels across suburbs

The bar chart represents house price distribution using the four price
categories defined in the assignment. The pie chart presents relative
percentages, while the bar chart presents absolute property counts.

## Data Export

The application generates:

`output/sorted_house_prices.csv`

The exported dataset:

- Contains all 110 original house records
- Is sorted by house price in ascending order
- Preserves the original `id`, `price`, `suburb`, and `demand` fields
- Includes `median_price`, `lowest_price`, and `highest_price` columns

The statistical values are stored as numerical values so the exported
CSV remains suitable for further analysis.



## Technical PDF Report

The application generates:

`output/house_price_technical_report.pdf`

The technical report contains:

1. A statistical summary of the house price dataset
2. House price category pie chart
3. House price distribution bar chart
4. High and General demand price histogram
5. House price and demand scatter plot across suburbs

The statistical values and figures are generated dynamically from the
supplied dataset.

## Problem 1 Analysis

The detailed findings and written responses to the four required Problem 1
analysis questions are documented in:

`docs/problem1-analysis.md`

The conclusions are based on statistics and supporting analysis calculated
directly by `q1.py`, together with the generated visualisations.


coit29225-a1-house-price-analysis/
├── data/
│   └── house_prices.csv
├── docs/
│   └── problem1-analysis.md
├── output/
│   ├── figures/
│   │   ├── price_category_pie_chart.png
│   │   ├── price_distribution_bar_chart.png
│   │   ├── demand_price_histogram.png
│   │   └── suburb_demand_scatter_plot.png
│   ├── sorted_house_prices.csv
│   └── house_price_technical_report.pdf
├── q1.py
├── requirements.txt
├── README.md
└── .gitignore