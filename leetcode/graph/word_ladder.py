from collections import deque
import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in wordList:
            return 0

        q = deque([(beginWord, 1)])

        explored = set([beginWord])

        while q:
            cur_word, step = q.popleft()
            if cur_word == endWord and step > 0:
                return step

            step += 1
            for idx in range(len(cur_word)):
                for letter in string.ascii_lowercase:
                    next_word = cur_word[:idx] + letter + cur_word[idx + 1:]
                    if next_word == endWord:
                        return step
                    if next_word in explored or next_word not in word_set or next_word == cur_word:
                        continue
                    else:
                        q.append((next_word, step))
                        explored.add(next_word)

        return 0