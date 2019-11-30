class Codec:
    def encode(self, lu):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        return lu

    def decode(self, su):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return su


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
