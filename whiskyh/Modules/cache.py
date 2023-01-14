from json import dumps, loads
from os.path import exists

class Cache:
    title = 'Cache'

    def __init__(self, file_='cache.txt'):
        self.path = './Contents/' + file_

    def __repr__(self):
        return self.title
    
    def readline(self, obj, index=0):
        new = obj()
        if exists(self.path):
            with open(self.path, 'rt+') as f:
                lines = f.readlines()
                tot = len(lines)
                if index < 0:
                    index = tot + index
                elif index > tot:
                    index = 0
                line = lines[index]
                new.__dict__ = loads(line)
        return new

    def writeline(self, obj):
        with open(self.path, 'at+') as f:
            f.write(dumps(obj.__dict__) + '\n')
