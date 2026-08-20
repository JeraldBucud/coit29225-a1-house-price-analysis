# Problem 1 Analysis

This document records the analysis findings for COIT29225 Assignment 1,
Problem 1. The answers are based on the supplied house price dataset,
calculated statistics, and generated visualisations.

## Question 1: Which suburb has the most houses priced above the median?

The overall median house price is **$915,000**.

The number of houses priced above the median in each suburb is:

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

The overall descriptive statistics are:

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

The mean is higher than the median, which is consistent with a
right-skewed distribution. The histogram also shows a long upper tail,
with a relatively small number of expensive properties extending beyond
$2 million and up to $3.2 million.

The price-category visualisations show that the largest category is
**Middle-Class Level**, containing 49 houses or approximately 44.5% of
the dataset. The remaining properties are distributed across Economical
Level, Premium Level, and Entry Level categories.

There are also differences between the two demand groups:

| Demand Level | Count | Mean Price | Median Price | Minimum | Maximum |
|---|---:|---:|---:|---:|---:|
| General | 54 | $1,119,026.43 | $985,000 | $50,005 | $3,200,000 |
| High | 56 | $894,534.21 | $890,000 | $99,000 | $2,000,000 |

In this dataset, General Demand properties have both a higher mean and
median price than High Demand properties. Therefore, a High Demand label
does not necessarily indicate a more expensive property.

The suburb scatter plot also demonstrates that house prices vary
considerably between and within suburbs. Highgate Hill and Toowong contain
several of the higher-priced properties, while other suburbs have a more
concentrated price range.

Overall, the dataset contains substantial price variation, a long
upper-price tail, and identifiable differences between suburb and demand
groups.

## Question 3: Can the distribution be accurately modelled by a single Gaussian kernel?

A single Gaussian distribution would **not provide an accurate model of
the house price distribution**.

A Gaussian distribution is approximately symmetric around its mean.
However, the observed house price data is positively skewed, with a
skewness value of approximately **1.194**.

The mean house price of approximately **$1.005 million** is noticeably
higher than the median of **$915,000**, which is another indication that
high-value properties are pulling the distribution toward the right.

The dataset also contains a long upper tail, including properties priced
above $2 million and a maximum price of $3.2 million. These high-price
observations make the distribution less symmetric than would be expected
under a single Gaussian model.

In addition, the dataset combines properties from different suburbs and
demand categories. These groups have different price characteristics,
meaning the overall data may represent a mixture of several underlying
market segments rather than one homogeneous population.

Therefore, a single Gaussian model would oversimplify the distribution.
A model capable of representing skewness or multiple groups, such as a
Gaussian mixture model or a non-parametric kernel density estimate, may
provide a better representation of the observed house prices.

## Question 4: Business Problem and Real-Estate Application

### Business Problem

A real-estate agency needs to determine **which suburb, price range, and
demand segments should receive the greatest marketing attention and how
properties in those segments should be positioned and priced**.

Treating all properties in the same way could lead to inefficient
marketing expenditure because the dataset shows substantial differences
in price distributions across suburbs and demand categories.

### Proposed Solution

The agency could segment its property portfolio using:

- Suburb
- House price
- Price category
- Demand level
- Median and average prices within each market segment

The analysis shows, for example, that Highgate Hill has the largest number
of properties above the overall median price. This could indicate a strong
higher-value property segment within that suburb.

The analysis also shows that General Demand properties have a higher mean
and median price than High Demand properties in this dataset. Therefore,
the agency should not assume that a High Demand classification
automatically represents a premium-priced property.

### Benefits to Marketing

The agency could use this information to:

- Target premium-property advertising toward suburbs containing more
  high-value properties.
- Create different campaigns for Entry, Economical, Middle-Class, and
  Premium property segments.
- Allocate advertising budgets toward suburb and price combinations that
  are most relevant to the target customer.
- Match marketing messages to the characteristics of each property
  segment.
- Avoid using demand level alone as an indicator of property value.

### Benefits to Strategic Planning

The agency could also use the analysis to:

- Identify suburbs with stronger higher-priced market segments.
- Support pricing and listing strategies using suburb-level statistics.
- Determine which property categories make up the largest share of the
  current market.
- Monitor changes in demand and price distributions over time.
- Improve decisions about where to focus future listings and sales
  resources.

Using data-driven segmentation would allow the agency to make marketing
and strategic decisions based on observed market patterns rather than
treating all properties and suburbs as equivalent.