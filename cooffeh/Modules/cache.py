from json import dumps, loads
from os import popen, path
from linecache import getline

class Cache:
    title = 'Cache'

    def __init__(self, obj, file_='cache.txt'):
        self.obj = obj
        self.path = './Contents/' + file_

    def __repr__(self):
        return self.title

    def exist(self):
        return path.exists(self.path)

    def delOld(self):
        return popen(f'rm -rf ./Contents/*.txt')

    def readline(self, index=0):
        load = self.obj()
        line = getline(self.path, index)
        load.__dict__ = {} if not line else loads(line)
        return load

    def writeline(self, obj):
        with open(self.path, 'at+') as f:
            f.write(dumps(obj.__dict__) + '\n')
