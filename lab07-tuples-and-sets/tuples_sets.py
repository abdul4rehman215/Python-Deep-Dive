# Tuple example
coordinates = (10, 20, 30)
print("Coordinates Tuple:", coordinates)

# Attempt to modify tuple
try:
    coordinates[0] = 100
except TypeError as e:
    print("Error:", e)

# Set example
number_set = {1, 2, 3, 4, 5}
print("Initial Set:", number_set)

# Add duplicate element
number_set.add(3)
print("Set after adding duplicate:", number_set)
