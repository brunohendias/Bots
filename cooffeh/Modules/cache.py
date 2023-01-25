from json import dumps, loads
from os import popen, path, system
from linecache import getline, clearcache

class Cache:
    title = 'Cache'

    def __init__(self, obj, file_='cache.txt'):
        self.obj = obj
        self.path = './Contents/' + file_

    def __repr__(self):
        return self.title

    def exist(self):
        return path.exists(self.path)

    def delOld(self, name):
        system(f'rm -rf ./Contents/*{name}.txt')
        return clearcache()

    def readline(self, index=1):
        load = self.obj()
        load.__dict__ = loads(getline(self.path, index) or '{}')
        return load

    def writeline(self, obj):
        with open(self.path, 'at+') as f:
            f.write(dumps(obj.__dict__) + '\n')
