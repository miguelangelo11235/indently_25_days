# Constants
MILES_TO_KILOMETERS = 1.60934
KILOMETERS_TO_MILES = 1 / MILES_TO_KILOMETERS

# User inputs
miles_input = 35
km_input = 20

# Conversions
converted_miles = miles_input * MILES_TO_KILOMETERS
converted_km = km_input * KILOMETERS_TO_MILES

# Display
print(f"{miles_input} miles is {converted_miles} kilometers.")
print(f"{km_input} km is {converted_km} miles.")