# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

 

# Example 1:

# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2

from typing import List


class Solution():
    def numProvinces(self, graph: List[List[int]]) -> int:
        """
        [[1,1,0], -> city 0. City 0 is connected to itself and city 1.
        [1,1,0],
        [0,0,1]]


        Approach:
        for each city, 
        run dfs on that city if it has not been visited.
            for each connectedCity in city, 
            if that connected city has not yet been visited,
            and if the connected city is a 1 (is a connection)
                run dfs on that connected city.
        """

        # run dfs on any city which has not yet been visited.
        def dfs(city):
            visited.add(city)
            for connectedCity in range(len(graph)): # we can use graph length here because grid is a perfect square
                # run dfs on connectedCity if not yet visited
                if graph[city][connectedCity] == 1 and connectedCity not in visited:
                    dfs(connectedCity)

        numProvinces = 0
        visited = set()
        
        for city in range(len(graph)):
            if city not in visited:
                numProvinces += 1
                dfs(city)


        return numProvinces