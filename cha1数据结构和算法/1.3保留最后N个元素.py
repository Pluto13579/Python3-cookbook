#collections.deque 
#使用deque(maxlen=N)构造函数会新建一个固定大小的队列。当新的元素加入并且这个队列已满的时候，最老的元素会自动被移除掉。
#如果不设置最大队列大小，那么就会得到一个无限大小队列。

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

#Example use on a file
if __name__ == '__main__':
    with open(r'f:/Git/Python3-cookbook/cha1数据结构和算法/somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)    #deque([1,2,3],maxlen=3)
q.append(4)
print(q)    #deque([2,3,4],maxlen=3)