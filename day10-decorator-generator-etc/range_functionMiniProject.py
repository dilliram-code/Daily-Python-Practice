class MyRange_Class:
  def __init__(self, start, end):
    self.start = start
    self.end = end
    
  def __iter__(self):
    return My_Iterator(self)    # return the object of this class.
  
class My_Iterator:
  def __init__(self, iterable_obj):  # receive the object from upper class
    self.iterable = iterable_obj
  def __iter__(self):
    return self 
  def __next__(self):
    if self.iterable.start >= self.iterable.end:
      raise StopIteration
    
    current = self.iterable.start
    self.iterable.start += 1
    return current
  
# range1 = MyRange_Class(1,10)
for i in MyRange_Class(1,10):
  print(i)
  