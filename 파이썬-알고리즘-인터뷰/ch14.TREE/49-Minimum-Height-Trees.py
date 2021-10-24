# 가장 가운데 값 -> root => 최소 높이
# leaf node 제거하면서 남는 값 찾기

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <=1:
            return [0]

        # 트리 = 무방향 graph
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        leaves = []
        # leaf node 찾아서 leaves에 추가
        for i in range(n+1):
            if len(graph[i]) == 1:
                leaves.append(i)
        
        # root가 남을 때까지 leaf node 반복해서 제거
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
            
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # 새로운 leaf node로 교체    
            leaves = new_leaves
        
        return leaves