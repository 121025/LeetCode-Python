#428ms

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        temp = []
        
        def dfs(num, limit):
            if limit == 0:
                results.append(temp[:])
                
            for i in range(num, n + 1):
                temp.append(i)
                dfs(i + 1, limit - 1)
                temp.pop()
                
        dfs(1, k)
        return results
