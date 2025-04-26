import time

class Cache:
    def __init__(self):
        self.data = {}

    def get(self, key):
        entry = self.data.get(key)
        if entry and (time.time() - entry['timestamp']) < 30:
            return entry['value']
        return None

    def set(self, key, value):
        self.data[key] = {'value': value, 'timestamp': time.time()}
