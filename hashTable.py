class HashTable:
    def __init__(self):
        self.size = 100
        self.table = [[] for i in range(self.size)]

    def gethashvalue(self, key):
        h = 0
        for char in key:
            h += ord(char)
        h = h % self.size
        return h

    def __setitem__(self, key, value):
        hashvalue = self.gethashvalue(key)
        found = False
        for idx, element in enumerate(self.table[hashvalue]):
            if element[0] == key:
                self.table[hashvalue][idx] = (key, value)
                found = True
        if not found:
            self.table[hashvalue].append((key, value))

    def __getitem__(self, key):
        hashvalue = self.gethashvalue(key)
        for element in self.table[hashvalue]:
            if element[0] == key:
                return element[1]
        return None

    def __delitem__(self, key):
        hashvalue = self.gethashvalue(key)
        for idx, element in enumerate(self.table[hashvalue]):
            if element[0] == key:
                del self.table[hashvalue][idx]


if __name__ == '__main__':
    h = HashTable()
    h['march 6'] = 520
    h['march 6'] = 420
    h['march 7'] = 420
    h['march 17'] = 125
    print(h.table)
    del h['march 7']
    print(h.table)
    print(h['march 6'])
    print(h['march 17'])
