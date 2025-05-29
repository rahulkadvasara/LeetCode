# 225. Implement Stack using Queues
# Easy

# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
# Implement the MyStack class:
# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:
# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

# Example 1:
# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]
# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False
 
# Constraints:
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, top, and empty.
# All the calls to pop and top are valid.
 
# Follow-up: Can you implement the stack using only one queue?



# sol 1 

# class MyStack:

#     def __init__(self):
#         self.queue = []

#     def push(self, x: int) -> None:
#         self.queue.append(x)

#     def pop(self) -> int:
#         if not self.queue:
#             return None
#         # Move all elements except the last one to the front
#         for _ in range(len(self.queue) - 1):
#             self.queue.append(self.queue.pop(0))
#         return self.queue.pop(0)

#     def top(self) -> int:
#         if not self.queue:
#             return None
#         # Move all elements except the last one to the front
#         for _ in range(len(self.queue) - 1):
#             self.queue.append(self.queue.pop(0))
#         top_element = self.queue.pop(0)
#         self.queue.append(top_element)  # Push it back to the queue
#         return top_element
    
#     def empty(self) -> bool:
#         return len(self.queue) == 0
    


# sol 2

# class MyStack:

#     def __init__(self):
#         self.queue = []

#     def push(self, x: int) -> None:
#         self.queue.append(x)

#     def pop(self) -> int:
#         if not self.queue:
#             return None
#         # Move all elements except the last one to the front
#         for _ in range(len(self.queue) - 1):
#             self.queue.append(self.queue.pop(0))
#         return self.queue.pop(0)

#     def top(self) -> int:
#         if not self.queue:
#             return None
#         return self.queue[-1]

#     def empty(self) -> bool:
#         return len(self.queue) == 0
    


# sol 3

# class MyStack:

#     def __init__(self):
#         self.queue1 = []
#         self.queue2 = []

#     def push(self, x: int) -> None:
#         self.queue1.append(x)

#     def pop(self) -> int:
#         if not self.queue1:
#             return None
#         while len(self.queue1) > 1:
#             self.queue2.append(self.queue1.pop(0))
#         popped_value = self.queue1.pop(0)
#         self.queue1, self.queue2 = self.queue2, []  # Swap queues
#         return popped_value

#     def top(self) -> int:
#         if not self.queue1:
#             return None
#         while len(self.queue1) > 1:
#             self.queue2.append(self.queue1.pop(0))
#         top_value = self.queue1.pop(0)
#         self.queue2.append(top_value)  # Move the last element to queue2
#         self.queue1, self.queue2 = self.queue2, []  # Swap queues
#         return top_value
    
#     def empty(self) -> bool:
#         return len(self.queue1) == 0
    


# sol 4

# class MyStack:

#     def __init__(self):
#         self.q = deque()

#     def push(self, x: int) -> None:
#         self.q.append(x)
#         for _ in range(len(self.q) - 1):
#             self.q.append(self.q.popleft())

#     def pop(self) -> int:
#         return self.q.popleft()
        
#     def top(self) -> int:
#         return self.q[0]

#     def empty(self) -> bool:
#         return len(self.q) == 0
    


# sol 5

# class MyStack:

#     def __init__(self):
#         self.q1 = deque()
#         self.q2 = deque()

#     def push(self, x: int) -> None:
#         self.q1.append(x)

#     def pop(self) -> int:
#         while len(self.q1) > 1:
#             self.q2.append(self.q1.popleft())

#         popped_val = self.q1.popleft()
#         self.q1, self.q2 = self.q2, self.q1

#         return popped_val
        
#     def top(self) -> int:
#         while len(self.q1) > 1:
#             self.q2.append(self.q1.popleft())

#         top_val = self.q1[0]
#         self.q2.append(self.q1.popleft())
#         self.q1, self.q2 = self.q2, self.q1

#         return top_val

#     def empty(self) -> bool:
#         return len(self.q1) == 0