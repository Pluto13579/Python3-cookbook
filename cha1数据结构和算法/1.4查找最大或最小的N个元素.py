import heapq

nums = [1, 43, 5, 89, -9, 23, 56, -34, 0, 5, 59]
print(heapq.nlargest(3, nums))  #[89, 56, 43]
print(heapq.nsmallest(3, nums)) #[-34, -9, 0]

#两个函数都能接受一个关键字参数：key=None
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(cheap)
print(expensive)

#堆数据结构 堆排序
#heap[0]永远是最小的元素，并且剩余的元素可以通过调用heapq.heappop()方法得到，该方法会先将第一个元素弹出来，然后用下一个最小的元素取代被弹出元素。

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
print(heap)