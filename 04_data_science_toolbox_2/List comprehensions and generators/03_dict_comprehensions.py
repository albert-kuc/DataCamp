"""
Dict comprehensions:

Create a dictionary using the comprehension syntax. In this case, the comprehension is called a dict comprehension.
Recall that the main difference between a list comprehension and a dict comprehension is the use of curly braces {}
instead of []. Additionally, members of the dictionary are created using a colon :, as in <key> : <value>.

You are given a list of strings fellowship and, using a dict comprehension, create a dictionary with the members of the
list as the keys and the length of each string as the corresponding values.
"""

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship}

# Print the new list
print(new_fellowship)
