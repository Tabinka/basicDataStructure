
class Stack:
      
      def __init__(self):
            self.basicStack = []
      
      def push(self, item):
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
      
      