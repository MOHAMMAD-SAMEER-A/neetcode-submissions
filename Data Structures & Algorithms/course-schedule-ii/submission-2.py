from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. Build the adjacency list and in-degree count
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degree[dest] += 1
            
        # 2. Add all courses with no prerequisites (in-degree 0) to the queue
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        order = []
        
        # 3. Process the queue
        while queue:
            u = queue.popleft()
            order.append(u)
            
            for v in adj[u]:
                in_degree[v] -= 1
                # If in-degree becomes 0, all prerequisites for course 'v' are met
                if in_degree[v] == 0:
                    queue.append(v)
                    
        # 4. If order contains all courses, return it; otherwise, a cycle exists
        return order if len(order) == numCourses else []