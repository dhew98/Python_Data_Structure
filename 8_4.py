fname = input("Enter file name: ")
fh = open(fname)
l = list()
for line in fh:
    words = line.split()
    for w in words:
        if w not in l:
            l.append(w)
print(sorted(l))
