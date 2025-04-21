class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        
        def helper(pth: List[int],node: int) -> None:
            pth.append(node)
            if node == len(graph)-1:
                ans.append(pth[:])
                return 
            for v in graph[node]:
                helper(pth[:],v)
            return 

        helper([],0)
        return ans