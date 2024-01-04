# First day of contribute everyday challange

This is generated task from ChatGPT

## Task

 - Task: Implement a basic data structure (like a stack, queue, or linked list) from scratch.
 - Challenge: Add additional functions to manipulate the data structure (like sorting for a list, or enqueue/dequeue for a queue).

### Stack Implementation:

#### Basic Structure:
 - Create a class named *Stack*.
 - Use an internal data structure (like a list in Python) to store the elements of the stack.

#### Core Methods:
 - *push(element)*: Add an element to the top of the stack.
 - *pop()*: Remove and return the element at the top of the stack. If the stack is empty, return a message indicating it or handle the underflow condition.
 - *peek()*: Return the element at the top of the stack without removing it. Again, handle the scenario where the stack is empty.

#### Auxiliary Methods:
 - *is_empty()*: Check if the stack is empty.
 - *size()*: Return the number of elements in the stack.

#### Error Handling:
 - Include appropriate error handling for scenarios like popping from an empty stack.

#### Testing:
 - Write a series of test cases to validate your implementation. This could include pushing and popping elements, checking the size of the stack, and ensuring error handling works as expected.

### Advanced Enhancements (Optional):

- Dynamic Array Implementation: If you're using an array/list, implement a dynamic array that expands when the stack reaches its capacity.
- Min/Max Tracking: Modify your stack to keep track of the minimum or maximum element present at any given time.
- Time Complexity Annotations: Add comments indicating the time complexity of each method.