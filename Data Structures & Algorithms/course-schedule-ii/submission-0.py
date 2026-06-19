from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # 1. Build the graph and track in-degrees
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        
        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degree[dest] += 1
            
        # 2. Queue all courses with no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        order = []
        
        # 3. Process courses
        while queue:
            curr = queue.popleft()
            order.append(curr)
            
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # 4. If all courses are in order, return it; else return []
        return order if len(order) == numCourses else []
