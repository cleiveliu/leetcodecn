
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = {}
        self.mark = '@'
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.head
        for c in word:
            if c in cur:
                cur = cur[c]
            else:
                cur[c] = {}
                cur = cur[c]
        cur[self.mark] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.head
        for c in word:
            if c in cur:
                cur = cur[c]
            else:
                return False
        return self.mark in cur and cur[self.mark] == True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.head
        for c in prefix:
            if c in cur:
                cur = cur[c]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)