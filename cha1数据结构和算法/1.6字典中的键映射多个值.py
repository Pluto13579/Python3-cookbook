#使用collections模块中的defaultdict来构造这样的词典。
#defaultdict会自动为将要访问的键(就算目前字典中并不存在这样的键)创建映射实体。

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d.items())