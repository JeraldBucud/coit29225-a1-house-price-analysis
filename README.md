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

## House Price Categories

Properties are grouped into four price categories:

- **Entry Level:** Less than $500,000
- **Economical Level:** Up to $800,000 after the Entry Level range
- **Middle-Class Level:** Up to $1,400,000 after the Economical Level range
- **Premium Level:** Above $1,400,000

The supplied dataset does not contain properties priced exactly at the
boundary values of $500,000, $800,000, or $1,400,000.

## Project Structure

```text
coit29225-a1-house-price-analysis/
├── data/
│   └── house_prices.csv
├── output/
│   └── figures/
├── q1.py
├── requirements.txt
├── README.md
└── .gitignore
```