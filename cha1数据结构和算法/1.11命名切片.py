# 内置的slice()函数创建了一个切片对象。所有使用切片的地方都可以使用切片对象。
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4], items[a])
items[a] = [10, 11]
print(items)
del items[a]
print([items])

# 如果你有一个切片对象a，你可以分别调用它的 a.start , a.stop , a.step 属性来获取更多的信息。
a = slice(5, 50, 2)
a.start     # 5
a.stop      # 50
a.step      # 2

# 还可以通过调用切片的 indices(size) 方法将它映射到一个已知大小的序列上。
s = 'HelloWorld'
a.indices(len(s))       # (5, 10, 2)
for i in range(*a.indices(len(s))):
    print(i, s[i])