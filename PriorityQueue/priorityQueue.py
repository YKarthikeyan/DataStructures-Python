from heapq import heappush, heappop

class PriorityQueue(object):
    def __init__(self, isMinHeap):
        if isMinHeap:
            self.mul = 1
        else:
            self.mul = -1
        self.pq = []
        self.entry_finder = {}

    def add_task(self, priority, task):
        if task in self.entry_finder:
            raise('task already present')
        entry = [self.mul*priority, False, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def contains_task(self, task):
        if task in self.entry_finder:
            return True
        else:
            return False

    def get_task_priority(self, task):
        if task not in self.entry_finder:
            raise ValueError('task not present')
        return self.entry_finder[task][0]

    def pop_task(self):
        while self.pq:
            priority, removed, task = tuple(heappop(self.pq))
            if removed is False:
                del self.entry_finder[task]
                return task
        raise KeyError("pop from an empty priority queue")

    def change_task_priority(self, priority, task):
        if task not in self.entry_finder:
            raise KeyError('task not found')
        self.remove_task(task)
        self.add_task(priority, task)

    def remove_task(self, task):
        entry = self.entry_finder.pop(task)
        entry[1] = True

    def peek_task(self):
        while self.pq:
            priority, removed, task = tuple(heappop(self.pq))
            if removed is False:
                 heappush(self.pq, [priority, False, task])
                 return task
        raise KeyError("pop from an empty priority queue")

    def is_empty(self):
        try:
            self.peek_task()
            return False
        except KeyError:
            return True

    def __str__(self):
        return str(self.entry_finder) + "\n" + str(self.pq)




if __name__ == '__main__':
    task1 = "A"
    task2 = "B"
    task3 = "C"
    task4 = "D"

    #MIN HEAP

    min_pq = PriorityQueue(True)
    min_pq.add_task(1, task1)
    min_pq.add_task(6, task2)
    min_pq.add_task(3, task3)
    min_pq.add_task(10, task4)
    print(min_pq.contains_task(task3))
    print(min_pq.get_task_priority(task3))
    print(min_pq)
    while min_pq.is_empty() is False:
        print(min_pq.pop_task())

    #MAX HEAP

    # max_pq = PriorityQueue(False)
    # max_pq.add_task(1, task1)
    # max_pq.add_task(3, task2)
    # max_pq.add_task(6, task3)
    # max_pq.add_task(7, task4)
    # while max_pq.is_empty() is False:
    #     print(max_pq.pop_task())