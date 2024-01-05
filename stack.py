
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