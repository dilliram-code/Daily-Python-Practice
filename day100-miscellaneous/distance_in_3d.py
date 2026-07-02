import math

def euclidean_distance(point1, point2):
  
  distance = 0
  for i in range(len(point1)):
    distance += (point1[i] - point2[i]) ** 2
    
  return math.sqrt(distance)

a = [170, 65, 22]
b = [172, 68, 21]

print(euclidean_distance(a,b))
  