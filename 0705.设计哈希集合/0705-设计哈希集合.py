class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [False] * (2**14) # 2**14 = 16000?

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        h_val = self._hash(key)
        if self.contains(key):
            return 
        if self.data[h_val] is False:
            self.data[h_val] = key
        elif isinstance(self.data[h_val], list):
            self.data[h_val].append(key)
        else:
            self.data[h_val] = [self.data[h_val],key]
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        h_val = self._hash(key)
        if self.data[h_val] is not False:
            if self.data[h_val] == key:
                self.data[h_val] = False
            elif isinstance(self.data[h_val], list):
                tem = self.data[h_val]
                for a in tem:
                    if a == key:
                        tem.remove(key)
                        if tem == []:
                            self.data[h_val] = False
                        break

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        h_val = self._hash(key)
        if self.data[h_val] is not False:
            if isinstance(self.data[h_val], list):
                for a in self.data[h_val]:
                    if a == key:
                        return True
                return False
            elif self.data[h_val] == key:
                return True
            else:
                return False
        return False
    def _hash(self,key):
        h_val = 0
        for c in str(key):
            h_val += ord(c)
        return h_val & (2**14 -1)
    

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)