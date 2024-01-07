# Create Stack
import stack

myStack = stack.Stack()

myStack.push(10)
myStack.push(20)
myStack.push(30)
myStack.push(100)
myStack.push(200)
myStack.push(100)


## Test scenarios for functions

print(f"Size of a stack: {myStack.size()}")
print(f"Peek function returns: {myStack.peek()}")
#print(f"Pop function returns: {myStack.pop()}")
print(f"Stack is empty (True/False): {myStack.is_empty()}")

print(f"What Array looks like now: {myStack._get()}")