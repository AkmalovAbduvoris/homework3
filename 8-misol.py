arr = [(1, 2, 3), (3, 4, 5), (5, 6)]
ok = list()
for i in arr:
    ok.extend(i)
print(set(ok))