# dfs ========================================================
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        _END = '_END'
        trie = {}
        def build(word):
            curr = trie
            for c in word:
                curr = curr.setdefault(c, {})
            curr[_END] = _END
        for word in set(products):
            build(word)
        res = []
        curr = trie
        def dfs(curr, word):
            if len(words) == 3:return
            if _END in curr:words.append(word)
            if len(words) == 3:return
            for key in sorted(curr.keys()):
                if key != _END:
                    dfs(curr[key], word+key)

        w = ""
        for c in searchWord:
            w += c
            words = []
            if c not in curr:break
            dfs(curr[c],w)
            if not words:break
            res.append(words)
            curr = curr[c]
        return res + [[] for _ in range(len(searchWord)-len(res))]


# Trie
class TrieNode():
    def __init__(self):
        self.children = {}  # mapping charactor to TrieNode
        self.words = []


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.words.append(word)
            node.words.sort()

            while len(node.words) > 3:
                node.words.pop()

    def search(self, word):
        res = []
        node = self.root
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            res.append(node.words[:])
        l_remain = len(word) - len(res)
        for _ in range(l_remain):
            res.append([])
        return res


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for p in products:
            trie.insert(p)
        res = trie.search(searchWord)
        return res