class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items)==0

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def print_stack(self):
        print("Stack:", self.items)


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def print_queue(self):
        print("Queue:", self.items)


class Queue_with_priority:
    def __init__(self):
        self.items = []

    def enqueue(self, priority, item):
        self.items.append((priority, item))
        self.items.sort(key=lambda x: x[0])

    def dequeue(self):
        if not self.is_empty():
            def get_priority(element):
                return element[0]
            highest_priority_item = min(self.items, key=get_priority)
            self.items.remove(highest_priority_item)
            return highest_priority_item
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def print_queue(self):
        print("Priority Queue:")
        for priority, item in self.items:
            print(f"Priority: {priority}, Item: {item}")




stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.print_stack()
print("Popped:", stack.pop())
stack.print_stack()
print("Size:", stack.size())

queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
queue.print_queue()
print("Dequeued:", queue.dequeue())
queue.print_queue()
print("Size:", queue.size())

priority_queue = Queue_with_priority()
priority_queue.enqueue(2, "Task2")
priority_queue.enqueue(1, "Task1")
priority_queue.enqueue(3, "Task3")
priority_queue.print_queue()
print("Dequeued:", priority_queue.dequeue())
priority_queue.print_queue()
print("Size:", priority_queue.size())