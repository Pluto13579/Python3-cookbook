#任意的序列(或者是可迭代对象)可以通过一个简单的赋值语句解压并赋值给多个变量。
#唯一的前提就是变量的数量必须跟序列元素的数量是一样的。
#包括字符串，文件对象，迭代器和生成器。
#解压一部分时可以使用任意变量名占位，到时候丢掉即可。
p = (4,5)
x, y = p
print(x, y) #x=4, y=5
data = ['ACME', 50, 91.1, (2018, 12, 11)]
name, shares, price, (year, mon, day) = data
print(name, price, year, mon, day)  #name=ACME, price=91.1, year=2018, mon=12, day=11
