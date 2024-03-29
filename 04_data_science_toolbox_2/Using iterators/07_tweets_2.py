"""
Extracting information for large amounts of Twitter data:
It's good to know how to process a file in smaller, more manageable chunks, but it can become very tedious having to
write and rewrite the same code for the same task each time. In this exercise, you will be making your code more
reusable by putting your work in the last exercise in a function definition.
"""

import pandas as pd

# Define count_entries()
def count_entries(csv_file, c_size, colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize=c_size):

        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict


# Call count_entries(): result_counts
result_counts = count_entries(r"../_datasets/tweets.csv", 10, 'lang')

# Print result_counts
print(result_counts)
