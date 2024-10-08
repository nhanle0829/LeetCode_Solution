class Codec:
    def __init__(self):
        self.encoder = {}
        self.decoder = {}
        self.url_base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encoder:
            shortUrl = self.url_base + str(len(self.encoder) + 1)
            self.encoder[longUrl] = shortUrl
            self.decoder[shortUrl] = longUrl
        return self.encoder[longUrl]

    def decode(self, shortUrl: str) -> str:
        return self.decoder[shortUrl]

