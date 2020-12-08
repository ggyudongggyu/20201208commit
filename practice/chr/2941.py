n = input()
alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj','s=','z=']
for word in alp:
    n = n.replace(word, "0")
print(len(n))
