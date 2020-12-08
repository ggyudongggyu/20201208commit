a = raw_input()
a1 = ""
a2 = ""
a3 = ""
i = 0
while i < len(a):
    if a[i] != '.':
        a1 += a[i]
        i += 1
    else:
        i += 1
        break


while i< len(a):
    if a[i] != '.':
        a2 += a[i]
        i += 1
    else:
        i += 1
        break
while i< len(a):
    a3 += a[i]
    i += 1

print "%04d.%02d.%02d" % (int(a1), int(a2), int(a3))
