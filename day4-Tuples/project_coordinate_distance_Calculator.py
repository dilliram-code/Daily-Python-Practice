'''-----------------PROJECT: CO-ORDINATE DISTANCE CALCULATOR---------------'''
import math
cities = {
    "Kathmandu": (27.7172, 85.3240),
    "Pokhara": (28.2096, 83.9856),
    "Biratnagar": (26.4525, 87.2718),
    "Lalitpur": (27.6667, 85.3333),
}

def calculate_distance(city1_cord, city2_cord):
  x1, y1 = city1_cord       # x and y cord for city1
  x2, y2 = city2_cord       # x and y cord for city2

  distance = (x2 - x1)**2 + (y2 - y1)**2      # Euclidean distance
  distance_result = math.sqrt(distance)

  return distance_result

print("\nAvailable cities:")
for city in cities:
  print(f"-{city}")

# store the city name to pass as keys of the dict
city1 = input("enter the first city: ").title().strip()
city2 = input("enter the second city: ").title().strip()

# pass the city co-ordinates to the function and store the result in var: distance
distance = calculate_distance(cities[city1], cities[city2])
print(f"The distance between {city1} and {city2} is: {distance:.2f} units.")
