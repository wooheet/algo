class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        self.s1.append(x)

    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()


q = int(input())
queue = Queue()

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        queue.enqueue(query[1])
    elif query[0] == 2:
        queue.dequeue()
    elif query[0] == 3:
        front = queue.dequeue()
        print(front)
        queue.enqueue(front)


# class Queue:
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
#
#     def enqueue(self, value):
#         self.stack1.append(value)
#
#     def dequeue(self):
#         if not self.stack2:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#         return self.stack2.pop()
#
#     def peek(self):
#         if not self.stack2:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#         return self.stack2[-1]



# A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.
#
# A basic queue has the following operations:
#
# Enqueue: add a new element to the end of the queue.
# Dequeue: remove the element from the front of the queue and return it.
#
# In this challenge, you must first implement a queue using two stacks. Then process q queries, where each query is one of the following 3 types:
#
# 1 x: Enqueue element  into the end of the queue.
# 2: Dequeue the element at the front of the queue.
# 3: Print the element at the front of the queue.
#
# Input Format
#
# The first line contains a single q integer, , denoting the number of queries.
# Each line i of the q subsequent lines contains a single query in the form described in the problem statement above. All three queries start with an integer denoting the query type, but only query 1 is followed by an additional space-separated value, x, denoting the value to be enqueued.
#
# Output Format
#
# For each query of type 3, print the value of the element at the front of the queue on a new line.
#
# sample input
#
# STDIN   Function
# -----   --------
# 10      q = 10 (number of queries)
# 1 42    1st query, enqueue 42
# 2       dequeue front element
# 1 14    enqueue 42
# 3       print the front element
# 1 28    enqueue 28
# 3       print the front element
# 1 60    enqueue 60
# 1 78    enqueue 78
# 2       dequeue front element
# 2       dequeue front element
#
#
# sample output
#
# 14
# 14
