my_list = [12, 23, 34, 'Alice', (41, 52), 623, 714]

# Initialize a counter
count = 0

# Iterate through the list
for item in my_list:
    count += 1
    if isinstance(item, tuple):
        break

# Print the count of elements until a tuple is encountered
print(f"Count of elements until a tuple is encountered: {count}")
