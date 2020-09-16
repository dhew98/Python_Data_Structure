name = input("Enter file:")
handle = open(name)
d = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith('From'):
        words = line.split()
        w = words[1]
        d[w] = d.get(w, 0)+1
m = 0
for k, v in d.items():
    if v >= m:
        m = v
        s = k
print(s, m)
