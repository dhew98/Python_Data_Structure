name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
d = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        w = words[5].split(':')
        x = w[0]
        d[x] = d.get(x, 0)+1
for k, v in sorted(d.items()):
    print(k, v)
