class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = {}

        indegree = [0] * numCourses

        for i in range(numCourses):
            graph[i] = []
        
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] +=1
        

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
            
        
        res =[]
        while queue:
            curr_course = queue.popleft()

            res.append(curr_course)

            for nei in graph[curr_course]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    queue.append(nei)
        

        if len(res) == numCourses:
            return res
        else:
            return []

        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
