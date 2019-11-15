class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mos = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        m_words = []
        for word in words:
            temp = ''.join(map(lambda x:mos[ord(x)-ord('a')], word))
            m_words.append(temp)
        return len(set(m_words))
        