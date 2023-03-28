class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.stop = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for letter in word:
            idx = ord(letter) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.stop = True

    def search(self, word: str) -> bool:
        target = len(word)
        stack = [(self.root, 0)]
        while stack:
            node, cur_len = stack.pop()
            if cur_len == target and node.stop == True:
                return True

            if cur_len < target:
                next_letter = word[cur_len]
                if next_letter == '.':
                    for child in node.children:
                        if child:
                            stack.append((child, cur_len + 1))
                else:
                    idx = ord(next_letter) - ord('a')
                    if node.children[idx]:
                        stack.append((node.children[idx], cur_len + 1))

        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)