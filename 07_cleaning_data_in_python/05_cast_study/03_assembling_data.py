"""
Assembling your data:
Here, three DataFrames have been pre-loaded: g1800s, g1900s, and g2000s. These contain the Gapminder life expectancy
data for, respectively, the 19th century, the 20th century, and the 21st century.

Your task in this exercise is to concatenate them into a single DataFrame called gapminder. This is a row-wise
concatenation, similar to how you concatenated the monthly Uber datasets in Chapter 3.

INSTRUCTIONS:
*   Use pd.concat() to concatenate g1800s, g1900s, and g2000s into one DataFrame called gapminder. Make sure you pass
    DataFrames to pd.concat() in the form of a list.
*   Print the shape and the head of the concatenated DataFrame.
"""


# Import files with pandas
import pandas as pd
g1800s = pd.read_csv('../_datasets/g1800.csv', delimiter=',')
g1900s = pd.read_csv('../_datasets/g1900.csv', delimiter=',')
g2000s = pd.read_csv('../_datasets/g2000.csv', delimiter=',')

# Concatenate the DataFrames row-wise
gapminder = pd.concat([g1800s, g1900s, g2000s], axis=0, sort=False)

# Print the shape of gapminder
print(gapminder.shape)

# Print the head of gapminder
print(gapminder.head())
print(gapminder.tail())