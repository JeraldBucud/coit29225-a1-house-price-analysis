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