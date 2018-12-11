#星号表达式，解压出来的永远是列表类型。
#可用在开头也可用在结尾。
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name, email, phone_numbers)   #name=Dave,email=dave@example.com,phone_numbers=['773-555-1212', '847-555-1212']
#星号表达式在迭代元素为可变长元祖的序列时是很有用的。
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

#星号解压语法在字符串操作的时候也会很有用，比如字符串的分割。
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(*fields)  #*fields=['*', '-2', '-2', 'Unprivileged', 'User']

#解压一些元素后丢弃它们，可以使用一个普通的废弃名称，比如_或者ign(ignore)。
record = ('ACME', 50, 123.45, (12, 11, 2018))
name, *_, (*_, year) = record
print(name, year)   #name=ACME,year=2018

#在很多函数式语言中，星号解压语法跟列表处理有许多相似之处。
items = [1, 2, 3, 4, 5]

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum(items))
