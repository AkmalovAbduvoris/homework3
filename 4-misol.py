tup =  [(), (), ('',), (), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d')]
arr = list()
for i in tup:
    if i:
        arr.append(i)
print(arr)