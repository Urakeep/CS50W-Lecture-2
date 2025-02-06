# Crate an emty set
s = set()

# Add element to set (any duplicate number will not be included)
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)

# remove element from set
s.remove(2)
print(s)

# check the number in set
print(f"The set has {len(s)} elements.")