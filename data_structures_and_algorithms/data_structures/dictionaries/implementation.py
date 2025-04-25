class hashTable:
    def __init__(self,size):
        self.size = size
        self.data = [[] for i in range(self.size)]

    def __str__(self):
        return str(self.__dict__)

    def hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])* i) % self.size
        return hash

    def set(self, key, value):
        hash = self.hash(key)
        if not self.data[hash]:
            self.data[hash] = [[key, value]]
        else:
            self.data[hash].append([key,value])


    def get(self, key):
        hash = self.hash(key)
        current_bucket = self.data[hash]
        if current_bucket:
            for i in range(len(current_bucket)):
                if current_bucket[i][0] == key:
                    return current_bucket[i][1]
        return -1

    def keys(self):
        keys_array = []
        for i in range(self.size):
            if self.data[i]:
                keys_array.append(self.data[i][0][0])
        return keys_array

    def values(self):
        values_array = []
        for i in range(self.size):
            if self.data[i]:
                values_array.append(self.data[i][0][1])
        return values_array


hashtable = hashTable(2)
hashtable.set('water', 50)
hashtable.set('grapes', 10000)
hashtable.set('oranges', 200)

print(hashtable)

print(hashtable.keys())
print(hashtable.values())