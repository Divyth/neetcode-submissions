class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordSet = set(wordList)
        q = deque()
        if endWord not in wordSet:
            return 0

        q.append((beginWord, 1))
        
        while q:
            word, level = q.popleft()

            if word == endWord:
                return level
            
            for i in range(len(word)):
                
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == word[i]:
                        continue
                    newWord = word[:i] + ch + word[i+1:]

                    if newWord in wordSet:
                        q.append((newWord, level + 1))
                        wordSet.remove(newWord)

        return 0