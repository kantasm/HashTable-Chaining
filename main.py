class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        # self.arr[h] = val
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


if __name__=='__main__':
    t = HashTable()

    t['mar 6'] = 130
    t['mar 6'] = 28
    t['mar 9'] = 200
    t['mar 10'] = 250
    t['dec 1'] = 200

    print(t['mar 10'])

    print(t.arr)

    t['mar 10'] = 255

    print(t.arr)

    del t['mar 10']

    print(t.arr)