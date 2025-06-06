from collections import defaultdict, deque

class Solution(object):
    def largestPathValue_DFS(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        max_color = 0
        for i in range(len(colors)):
            actual = self.max_color_DFS(colors, edges, i, [], max_color)
            if actual == -1:
                return -1
            if actual > max_color:
                max_color = actual
        return max_color
            
    def max_color_DFS(self, colors, edges, nodo, path, max):
        path.append(nodo)
        for salida,llegada in edges:
            if salida == nodo:
                if llegada in path:
                    return -1
                actual = self.max_color_DFS(colors, edges, llegada, path, max)
                if actual == -1:
                    return -1
                if actual > max:
                    max = actual
        colores = {}
        for n in path:
            if colors[n] not in colores:
                colores[colors[n]] = 0
            colores[colors[n]] += 1
        actual = 0
        for c in colores.values():
            if c > actual:
                actual = c
        path.remove(nodo)
        if actual > max:
            max = actual
        return max
    
    def largestPathValue_DFS_Memoization(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(colors)
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        memo = [[0] * 26 for _ in range(n)]
        vis = [0] * n  # 0 = no visitado, 1 = visitando, 2 = visitado
        self.ciclo = False
        self.max_value = 0

        def max_color(node):
            if vis[node] == 1:
                self.ciclo = True
                return [0] * 26
            if vis[node] == 2:
                return memo[node]

            vis[node] = 1
            local_count = [0] * 26
            for vecino in adj[node]:
                res = max_color(vecino)
                if self.ciclo:
                    return [0] * 26
                for i in range(26):
                    local_count[i] = max(local_count[i], res[i])

            color_idx = ord(colors[node]) - ord('a')
            local_count[color_idx] += 1
            memo[node] = local_count
            vis[node] = 2

            self.max_value = max(self.max_value, max(local_count))
            return local_count

        for i in range(n):
            if vis[i] == 0:
                max_color(i)
                if self.ciclo:
                    return -1

        return self.max_value


    def largestPathValue_DP(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(colors)
        adj = defaultdict(list)
        in_degree = [0] * n

        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1

        count = [[0] * 26 for _ in range(n)]

        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)

        for i in range(n):
            color_idx = ord(colors[i]) - ord('a')
            count[i][color_idx] = 1

        visited = 0
        max_color = 0

        while queue:
            node = queue.popleft()
            visited += 1

            for neighbor in adj[node]:
                for c in range(26):
                    extra = 1 if c == ord(colors[neighbor]) - ord('a') else 0
                    count[neighbor][c] = max(count[neighbor][c], count[node][c] + extra)

                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if visited < n:
            return -1

        for i in range(n):
            max_color = max(max_color, max(count[i]))

        return max_color

    
sol = Solution()
colors = "abaca"
edges = [[0,1],[0,2],[2,3],[3,4]]
print(sol.largestPathValue(colors, edges))