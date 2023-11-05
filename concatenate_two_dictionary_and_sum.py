# Define two dictionaries
dict1 = {'a': 11, 'b': 12, 'c': 13}
dict2 = {'b': 14, 'c': 15, 'd': 16}

# Concatenate the two dictionaries
concatenated_dict = {**dict1, **dict2}

# Calculate the sum of all values in the concatenated dictionary
total_sum = sum(concatenated_dict.values())

# Display the concatenated dictionary and the sum
print("Concatenated Dictionary:")
print(concatenated_dict)
print(f"Sum of all values: {total_sum}")
