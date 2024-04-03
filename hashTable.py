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

    def __delitem__(self, key):
        hashvalue = self.gethashvalue(key)
        for idx, element in enumerate(self.table[hashvalue]):
            if element[0] == key:
                del self.table[hashvalue][idx]


def readfiletohash(filename):
    h = HashTable()
    with open(filename, "r") as f:
        for line in f:
            tokens = line.split(',')
            try:
                temperature = int(tokens[1])
                h[tokens[0]] = temperature
            except:
                print("Invalid temperature.Ignore the row")
    return h


def readfiletoarray(filename):
    arr = []
    with open(filename, "r") as f:
        for line in f:
            tokens = line.split(',')
            try:
                temperature = int(tokens[1])
                arr.append(temperature)
            except:
                print("Invalid temperature.Ignore the row")
    return arr


def countwords(filename):
    words = {}
    with open(filename, "r") as f:
        for line in f:
            tokens = line.split(' ')
            for word in tokens:
                word = word.replace('\n', '')
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1
    return words


if __name__ == '__main__':
    h = readfiletohash('input/nyc_weather.csv')
    print(h.table)
    arr = readfiletoarray('input/nyc_weather.csv')
    print(f'Average temperature in first week of Jan: {sum(arr[:7]) / len(arr[:7]):.2f}')
    print(f'Maximum temperature in first 10 days of Jan: {max(arr[:10])}')
    print(f'Temperature on Jan 9: {h["Jan 9"]}')
    print(f'Temperature on Jan 4: {h["Jan 4"]}')

    print('============= Word Counts ==============')
    print(countwords('input/poem.txt'))
