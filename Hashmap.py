class hashmap:
    def __init__(self):
        self.max = 10
        self.arr = [None for i in range(self.max)]

    def getHash(self, key):
        h = 0
        for l in key:
            h += ord(l)
        return h % self.max

    def __setitem__(self, key, value):
        h = self.getHash(key)
        self.arr[h] = value

    def __getitem__(self, item):
        h = self.getHash(item)
        return self.arr[h]

t = hashmap()
t['march 6'] = 138
t['march 5'] = 137
t['march 4'] = 136
t['march 3'] = 135

#print(t['march 6'])
#print(t.arr)
data = {}
lst = []
sum = 0
hand = open('nyc_weather.csv', 'r')
for lines in hand:
    line = lines.strip().split(',')
    data[line[0]] = line[1]
dic = {}
hand = open('poem.txt')
for lines in hand:
    line = lines.strip().split(' ')
    for words in line:
        if words in dic.keys():
            dic[words] = int(dic[words]) + 1
        else: dic[words] = 1

print(dic)

