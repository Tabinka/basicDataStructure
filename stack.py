
class Stack:
      
      def __init__(self):
            self.basicStack = []
      
      def push(self, item):
            self.basicStack.append(item)
            
      def get(self):
            print(self.basicStack)