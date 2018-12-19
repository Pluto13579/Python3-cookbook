#在数据字典中执行一些计算操作（比如求最大值，最小值，排序等等）。

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HBQ': 37.20,
    'FB': 10.75
}

#通常先使用zip()函数先将键和值反转过来。
min_price = min(zip(prices.values(), prices.keys()))    # min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))    # max_price is (612.78, 'AAPL')
price_sorted = sorted(zip(prices.values(), prices.keys()))  # prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]

#需要注意的是zip()函数创建的是一个只能访问一次的迭代器。
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))    #OK (10.75, 'FB')
print(max(prices_and_names))    #ValueError: max() arg is an empty sequence

#在执行 min() 和 max() 操作的时候，如果恰巧最小或最大值有重复的，那么拥有最小或最大键的实体会返回。
prices = { 'AAA' : 45.23, 'ZZZ': 45.23 }
min(zip(prices.values(), prices.keys()))    #(45.23, 'AAA')
max(zip(prices.values(), prices.keys()))    #(45.23, 'ZZZ')