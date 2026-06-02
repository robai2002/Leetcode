class Codec:

    def __init__(self):
        self.map = {}
        self.id = 0
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        self.id += 1

        short = str(self.id)

        self.map[short] = longUrl

        return self.base + short

    def decode(self, shortUrl: str) -> str:
        short = shortUrl.split("/")[-1]

        return self.map[short]