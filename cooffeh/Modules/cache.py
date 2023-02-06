class Cache:
    contents = []

    def __repr__(self):
        return 'Cache'

    def read(self, index:int=0):
        return self.contents[index]

    def add(self, obj):
        self.contents.append(obj)

    def clear(self):
        self.contents = []
