
class Stack:
      
      def __init__(self):
            self.capacity = 5
            self.basicStack = self.create_array()
            
      def create_array(self):
            new_array = []
            return new_array
      
      def push(self, item):
            if self.size() == self.capacity:
                  print("Resize init...")
                  self._resize()
                  print(f"New capacity: {self.capacity}")
            self.basicStack.insert(0,item)
            
      def pop(self):
            try:
                  value = self.basicStack.pop(0)
                  return value
            except:
                  return "Nothing to pop."
      
      def peek(self):
            if not self.is_empty():
                  return self.basicStack[0]
            return "Nothing to peek."      
            
      def is_empty(self):
            if len(self.basicStack) > 0:
                  return False
            return True
            
      def size(self):
            return len(self.basicStack)
      
      def _get(self):
            return self.basicStack
      
      def _resize(self):
            new_cap = self.capacity * 2
            new_array = self.create_array()
            
            for item in self.basicStack:
                  new_array.insert(0,item)
            
            self.basicStack = new_array
            self.capacity = new_cap