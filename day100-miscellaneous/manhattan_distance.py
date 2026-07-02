import math 

def manhattan_distance(point1, point2):
  
  distance = 0
  
  for i in range(len(point1)):
    distance += abs(point1[i] - point2[i])
  
  return distance

a = [1,2,3]
b = [4,5,6]

print(manhattan_distance(a,b))