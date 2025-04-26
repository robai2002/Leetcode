class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:return 0
        #make graph 
        graph = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                graph[pattern].add(word)
        
        seen = set()
        queue = deque()
    
        queue.append(beginWord)
        seen.add(beginWord)
        ans = 0
        while queue:
            ans += 1
            for i in range(len(queue)):
                word = queue.popleft()

                if word ==endWord:return ans
                
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for s in graph[pattern]:
                        if s not in seen:
                            seen.add(s)
                            queue.append(s)
        return 0