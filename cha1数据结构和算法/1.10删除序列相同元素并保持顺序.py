#保持元素顺序的同时消除重复的值

#如果仅仅消除元素，通常可以简单的构造一个集合
#但是这种方法不能维护元素的顺序，生成的结果中的元素位置被打乱
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(set(a))   #{1, 2, 5, 9, 10}

#序列上的值都为hashable类型，可以利用集合或者生成器来解决这个问题
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))  #[1, 5, 2, 9, 10]

#非hashable(dict)序列中重复元素
def dedupe(items, key=None):    #这里的key参数指定了一个函数，将序列元素转变为hashable类型
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe(a, key=lambda d: (d['x'],d['y']))))  #[{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
print(list(dedupe(a, key=lambda d: d['x'])))   #[{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]