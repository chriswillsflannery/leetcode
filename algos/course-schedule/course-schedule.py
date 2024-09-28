class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        [[0,1],[0,2],[1,3],[1,4],[3,4]]
        0 has prereqs 1 and 2
        1 has prereqs 3 and 4
        3 has prereq 4

        (0) - (1) - (3)
           \       \ |
            (2)     (4)
        """

        # we can use an adjacency list to figure this out
        """
        0: [1,2]
        1: [3,4]
        2: []
        3: [4]
        4: []
        """

        # run DFS on every node 0 to n-1 to build adjacency list
        preMap = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        # store all courses along current DFS path
        visiting = set()

        def dfs(course):
            if course in visiting: # visiting course twice (loop detected)
                return False # this course is impossible to complete
            if preMap[course] == []
                return True
            visiting.add(course)
            for pre in preMap[course]:
                if not dfs(pre): # if it returns false
                    return False
                visiting.remove(course)
                preMap[course] = []
                return True
        
        for c in range(numCourses):
            if not dfs(c): # if it returns false
                return False
        return True
