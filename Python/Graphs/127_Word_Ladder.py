class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        pattern_to_word = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '_' + word[i + 1:]
                pattern_to_word[pattern].append(word)

        res = 1
        queue = collections.deque([beginWord])
        visited = set([beginWord])

        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                for j in range(len(word)):
                    pattern = word[:j] + '_' + word[j + 1:]
                    for nxt in pattern_to_word[pattern]:
                        if nxt == endWord:
                            return res + 1
                        if nxt not in visited:
                            visited.add(nxt)
                            queue.append(nxt)
            res += 1
        return 0
