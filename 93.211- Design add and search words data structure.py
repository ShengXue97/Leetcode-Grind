class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(cur, w):
            if not w:
                return cur.endOfWord
            if w[0] == ".":
                isFound = False
                for v in cur.children.values():
                    isFound = dfs(v, w[1:])
                    if isFound:
                        break
                return isFound
            if w[0] not in cur.children.keys():
                return False
            return dfs(cur.children[w[0]], w[1:])
        return dfs(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)