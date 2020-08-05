import converters
from converters import lbs_to_kg
from utils import find_max

print(converters.lbs_to_kg(100))

print(converters.kg_to_lbs(70))

numbers = [1, 4, 2, 3, 6, 8, 5, 9, 23, 14, 19, 32]
maximum = find_max(numbers)
print(maximum)
