class TrieNode:
    def __init__(self):
        self.children = {}  # children[character] = TreeNode()
        self.endOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            # if exist -> add to it's children;  not exist -> create new node
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            # if not exist -> return False; if exist with the end mark -> return True
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            # if not exist -> return False; if exist with the end mark -> return True
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

    # Time: insert, search, O(26*len(word))

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)