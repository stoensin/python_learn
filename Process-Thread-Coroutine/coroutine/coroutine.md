
# 协成

> 协程的话相当于语言自己实现一个函数调度,在一个函数运行时,中断函数,
> 并且保存函数上下文,之后在运行其他函数,之后再返回运行原函数
> 这是一个用协程实现的一个典型的生产者-消费者模型:

```
# -*- coding:utf-8 -*-
def consumer():
    n = 0
    print "consumer init"
    while True:
        n = yield n
        if not n:
            raise Exception('no production')
        n -= 1
        print "consuption 1,left %d" % n
def produce(c):
    n = 0
    next(c)
    while n < 6:
        n +=2
        print "produce 2,left %d" % n
        n = c.send(n)
        print "left %d" % n
    c.close()
c = consumer()
produce(c)
```
> 每次生产一次,中断生产函数,运行消费者函数,之后再生产,如此下去.
