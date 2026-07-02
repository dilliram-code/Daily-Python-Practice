# cosine similarity using core python
import math

def cosine_similarity(a,b):
  
  dot = 0
  sum_sq_a = 0
  sum_sq_b = 0
  
  for i in range(len(a)):
    dot += a[i] * b[i]
    sum_sq_a += a[i] ** 2       # square the element
    sum_sq_b += b[i] ** 2       # square the element
    
  cosine_value = dot / (math.sqrt(sum_sq_a * sum_sq_b))
    
  return cosine_value

a = [1,2,3]
b = [4,5,6]

print(cosine_similarity(a,b))



# numpy implementation
import numpy as np

A = np.array([1,2,3])
B = np.array([4,5,6])

similarity = np.dot(A,B) / (np.linalg.norm(A) * np.linalg.norm(B))

print(f"Similarity: {similarity}")