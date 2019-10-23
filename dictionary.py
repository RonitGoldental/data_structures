class Hashtable:
    def __init__(self):
        self.size = 10
        self.keys = [None]*self.size
        self.values = [None]*self.size

    def hashfunction(self,key):
        sum = 0
        for letter in range (len(key)):
            sum += ord(key[letter])
        return sum%self.size

    def put(self, key,value):
        index = self.hashfunction(key)
        while self.values[index]:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index+1)%self.size
        self.values[index] = value
        self.keys[index] = key

    def get(self,key):
        index = self.hashfunction(key)
        while self.keys[index]:
            if self.keys[index] == key:
                return self.values[index]
            index = (index+1)%self.size
        return None

if __name__=="__main__":
    table = Hashtable()
    table.put("apple",10)
    table.put("orange", 20)
    table.put("car", 30)
    table.put("table", 40)
    print(table.get("H"))
    print(table.get("apple"))
