from typing import List
class Minstack:
  def __init__(self, stack: List[int], minElementStack: List[int]) -> None:
    self.stack = stack
    self.minElementStack = minElementStack

  def push(self, el):
    self.stack.append(el)
    self.minElementStack.append(min(el, self.minElementStack[-1]))

  def pop(self):
    self.minElementStack.pop()
    return self.stack.pop()
    
  def top(self):
    return self.stack[-1]
  
  def minElement(self):
    return self.minElementStack[-1]