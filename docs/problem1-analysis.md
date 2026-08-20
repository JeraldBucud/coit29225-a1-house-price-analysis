# Problem 1 Analysis

This document records the findings for COIT29225 Assignment 1, Problem 1.

The conclusions are based on statistics and supporting analysis calculated
directly by `q1.py`, together with the visualisations generated from the
supplied house price dataset.

## Question 1: Which suburb has the most houses priced above the median?

The overall median house price is **$915,000**.

The number of houses priced above the median by suburb is:

| Suburb | Houses Above Median |
|---|---:|
| Highgate Hill | 19 |
| Toowong | 18 |
| Wynnum | 10 |
| Springfield | 5 |
| North Lake | 3 |

**Highgate Hill has the highest number of houses priced above the overall
median, with 19 properties.**

Toowong is a close second with 18 properties above the median.

## Question 2: Characteristics of the Data Distribution

The house price distribution is **positively skewed (right-skewed)**.

The calculated statistics are:

| Statistic | Value |
|---|---:|
| Mean | $1,004,739.48 |
| Median | $915,000.00 |
| Standard deviation | $550,302.03 |
| Minimum | $50,005.00 |
| First quartile (Q1) | $695,000.00 |
| Third quartile (Q3) | $1,200,019.50 |
| Maximum | $3,200,000.00 |
| Skewness | 1.194 |

The mean is higher than the median, while the positive skewness value of
1.194 indicates that the distribution has a longer upper-price tail.

The generated histogram also shows a relatively small number of expensive
properties extending above $2 million, with the most expensive property
priced at $3.2 million.

The price-category distribution is:

- Entry Level: 15 properties
- Economical Level: 26 properties
- Middle-Class Level: 49 properties
- Premium Level: 20 properties

The Middle-Class Level is the largest category, representing approximately
44.5% of the dataset.

The demand groups also show different price characteristics:

| Demand | Count | Mean | Median | Minimum | Maximum |
|---|---:|---:|---:|---:|---:|
| General | 54 | $1,119,026.43 | $985,000 | $50,005 | $3,200,000 |
| High | 56 | $894,534.21 | $890,000 | $99,000 | $2,000,000 |

In this dataset, General Demand properties have both a higher mean and
median price than High Demand properties. Therefore, the High Demand
classification does not necessarily indicate a higher-priced property.

Overall, the data shows substantial price variation, a long upper-price
tail, and noticeable differences between suburbs and demand groups.

## Question 3: Can the Distribution Be Modelled Accurately by a Single Gaussian Kernel?

A single Gaussian model would **not accurately represent the observed
house price distribution**.

A Gaussian distribution is approximately symmetric around its mean.
However, the house price distribution has a positive skewness value of
**1.194**, indicating a longer right-hand tail.

The overall mean price of approximately **$1.005 million** is also higher
than the median of **$915,000**, showing that relatively expensive
properties are pulling the mean upward.

The dataset includes properties above $2 million and reaches a maximum of
$3.2 million, further contributing to the asymmetric upper tail.

In addition, the observations come from multiple suburbs and demand
categories with different price characteristics. The overall distribution
therefore represents several market segments rather than one completely
homogeneous population.

For these reasons, a single Gaussian model would oversimplify the observed
distribution. A model capable of representing skewness or multiple market
segments may provide a better representation.

## Question 4: Business Problem and Real-Estate Application

### Business Problem

A real-estate agency needs to determine which suburb, price range, and
demand segments should receive the greatest marketing attention and how
properties in those segments should be positioned.

Treating every property and suburb using the same marketing strategy may
lead to inefficient advertising expenditure because the analysis shows
substantial differences in house prices and market characteristics.

### How the Analysis Could Help

The agency could segment properties according to:

- Suburb
- Price
- Price category
- Demand level
- Typical price statistics within each segment

For example, Highgate Hill contains the largest number of houses priced
above the overall median, indicating a substantial higher-value segment
within that suburb.

The analysis also demonstrates that High Demand properties are not
automatically the most expensive. General Demand properties have higher
mean and median prices in this dataset.

### Marketing Benefits

The agency could use these findings to:

- Target premium advertising toward suburbs containing more high-value properties.
- Develop different campaigns for Entry, Economical, Middle-Class, and Premium properties.
- Allocate advertising budgets according to suburb and price segment.
- Tailor marketing messages to different groups of prospective buyers.
- Avoid relying on demand classification alone as an indication of property value.

### Strategic Planning Benefits

The agency could also:

- Identify suburbs with stronger higher-value property segments.
- Support listing and pricing decisions with suburb-level data.
- Determine which price categories dominate the current portfolio.
- Monitor changes in price and demand patterns over time.
- Allocate sales and marketing resources toward more relevant market segments.

Using data-driven segmentation would help the agency make marketing and
strategic decisions based on observed property-market patterns rather than
treating all listings as equivalent.