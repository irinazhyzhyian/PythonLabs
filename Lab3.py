import string
n = int(input())
d = {}
for i in range(n):
    words = [word.strip(string.punctuation) for word in input().split()]
    for word in words[1:]:
        if word in d:
            d[word].append(words[0])
        else:
            d[word] = [words[0]]
m = int(input())
cities = []
for i in range(m):
    cities.append(input())
for city in cities:
    print(" ".join(d[city]))
