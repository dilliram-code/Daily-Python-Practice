import math 

def manhattan_distance(point1, point2):
  
  distance = 0
  
  for i in range(len(point1)):
    distance += abs(point1[i] - point2[i])
  
  return distance

a = [1,2,3]
b = [4,5,6]

print(manhattan_distance(a,b))



# using numpy
import numpy as np

a = np.array([1,2,3])
b = np.array([6,7,8])

distance = np.sum(np.abs(a - b))
print(f"Manhattan distance: {distance}")