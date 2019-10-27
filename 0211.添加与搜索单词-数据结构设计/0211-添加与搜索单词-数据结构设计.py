class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = {}
        self.mark = '$'
    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.head
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur[self.mark] = True
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def h(node, word):
            if not word:
                if isinstance(node,dict) and self.mark in node and node[self.mark] == True:
                    return True
                else:
                    return False
            if word[0] == '.':
                if isinstance(node,dict):
                    return any(h(node[c],word[1:]) 
                            for c in node.keys())
                else:
                    return False
            return isinstance(node,dict) and word[0] in node and h(node[word[0]], word[1:])
            
        cur = self.head
        for i,c in enumerate(word):
            if c in cur:
                cur = cur[c]
            else:
                if c == '.':
                    return h(cur, word[i:])
                else:
                    return False
        return self.mark in cur and cur[self.mark] == True
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)