from json import dumps, loads
from os.path import exists

class Cache:
    title = 'Cache'

    def __init__(self, obj, file_='cache.txt'):
        self.obj = obj
        self.path = './Contents/' + file_

    def __repr__(self):
        return self.title

    def exist(self):
        return exists(self.path)

    def readline(self, index=0):
        load = self.obj()
        with open(self.path, 'rt+') as f:
            lines = f.readlines()
            tot = len(lines)
            if index < 0:
                index = tot + index
            elif index > tot:
                index = 0
            line = lines[index]
            load.__dict__ = loads(line)
        return load

    def writeline(self, obj):
        with open(self.path, 'at+') as f:
            f.write(dumps(obj.__dict__) + '\n')
