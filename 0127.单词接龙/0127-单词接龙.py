class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        ws = set(wordList)

        head = {beginWord}
        tail = {endWord}

        res = 1
        chars = list("abcdefghijklmnopqrstuvwxyz")

        while head:
            if len(head) > len(tail):
                head, tail = tail, head

            q = set()
            for word in head:
                for i in range(len(word)):
                    for c in chars:
                        new_word = word[:i] + c + word[i + 1 :]

                        if new_word in tail:
                            return res + 1

                        if new_word in ws:
                            q.add(new_word)
                            ws.remove(new_word)
            head = q
            res += 1
        return 0
