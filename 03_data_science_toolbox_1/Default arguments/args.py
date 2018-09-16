"""
Functions with variable-length arguments (*args)
Flexible arguments enable to pass a variable number of arguments to a function.

The function gibberish() can accept a variable number of string values. Its return value is a single string composed of
all the string arguments concatenated together in the order they were passed to the function call.
"""


# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""

    # Initialize an empty string: hodgepodge
    hodgepodge = ""
    # Concatenate the strings in args
    for word in args:
        hodgepodge += word
    # Return hodgepodge
    return hodgepodge


# Call gibberish() with one string: one_word
one_word = gibberish("luke")
# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")

# Print one_word and many_words
print(one_word)
print(many_words)
