# Lab 5: Breadth First Search and Priority Queue


# =====================================
# Task 1: Implement BFS on the Graph
# =====================================

graph = {
    0: [1, 4],
    1: [0, 4, 2, 3],
    2: [1, 3],
    3: [4, 1, 2],
    4: [0, 1, 3]
}


def bfs(graph, start):
    queue = deque([start])
    visited = [start]

    while queue:
        node = queue.popleft()

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    return visited


print("Task 1: BFS Traversal")
print(bfs(graph, 0))


# =====================================
# Task 2: BFS Using Queue
# Start Node: A
# Goal Node: G
# =====================================

tree = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'F': [],
    'D': ['G'],
    'E': ['C', 'H', 'I'],
    'K': ['N', 'M'],
    'J': [],
    'G': [],
    'C': [],
    'H': [],
    'I': ['L'],
    'N': [],
    'M': [],
    'L': []
}


def bfs_goal(tree, start, goal):
    queue = deque([start])
    visited = [start]

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        if node == goal:
            print("\nGoal found!")
            return

        for neighbour in tree[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


print("\nTask 2: BFS from A to G")
bfs_goal(tree, 'A', 'G')


# =====================================
# Task 3: Implement Priority Queue
# =====================================

class PriorityQueue:

    def _init_(self):
        self.items = []

    def insert(self, item, priority):
        self.items.append((priority, item))
        self.items.sort()

    def remove(self):
        if len(self.items) == 0:
            print("Priority Queue is empty")
            return None

        priority, item = self.items.pop(0)
        return item

    def display(self):
        print(self.items)


print("\nTask 3: Priority Queue")

pq = PriorityQueue()

pq.insert("A", 3)
pq.insert("B", 1)
pq.insert("C", 2)

print("Priority Queue:")
pq.display()

print("Removed item:", pq.remove())

print("Queue after removing an item:")
pq.display()