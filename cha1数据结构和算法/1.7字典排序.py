#collections模块中的OrderDict类可以用来控制一个字典中元素的顺序。
#OrderedDict内部维护着一个根据键插入顺序排序的双向链表。每当插入一个新元素都会放到链表的尾部。
#对于一个已存在的键的重复赋值不会改变键的顺序。
#需要注意的是一个OrderedDict的大小是一个普通字典的两倍，因为内部维护着另外一个链表。
#  
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for key in d:   # Outputs "foo 1", "bar 2", "spam 3", "grok 4"
    print(key, d[key])

#也可精确控制json编码后字段的顺序，可以先使用OrderedDict来构建这样的数据：
import json

json.dumps(d)   #{"foo": 1, "bar": 2, "spam": 3, "grok": 4}