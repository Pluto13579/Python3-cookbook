#第一个pop()操作返回优先级最高的元素。
#如果两个有着相同优先级的元素，pop操作按照他们被插入到队列的顺序返回的。
#队列包含了一个 (-priority, index, item) 的元组。 优先级为负数的目的是使得元素按照优先级从高到低排序。 这个跟普通的按优先级从低到高排序的堆排序恰巧相反。
#index 变量的作用是保证同等优先级元素的正确排序。 通过保存一个不断增加的 index 下标变量，可以确保元素按照它们插入的顺序排序。 而且， index 变量也在相同优先级元素比较的时候起到重要作用。
#使用三元组(priority, index, item)可以进行优先级比较。
import heapq

class PriortyQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    
    def push(self, item, priorty):
        heapq.heappush(self._queue, (-priorty, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriortyQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
q.pop() #Item('bar')
q.pop() #Item('spam')
q.pop() #Item('foo')
q.pop() #Item('grok')

#三元组(priority, index, item)
a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))