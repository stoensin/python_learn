
# 设计模式

## 《Design Patterns》一书把设计模式分为了3大类：
1. 创建型模式（creational pattern）
2. 结构型模式（structural pattern）
3. 行为型模式（behavioral patterns）。


## 一. 创建型模式（creational pattern）
```
对类的实例化过程进行了抽象，能够使软件模块做到与对象创建和组织的无关性。
为了使体系结构更加清晰，一些软件在设计上要求当创建类的具体实例时，能够根据具体的语境来动态地决定怎样创建对象，
创建哪些对象，以及怎样组织和表示这些对象，而创建型模式所要描述的就是该如何来解决这些问题。
```
> 创建型模式包括以下几种：
>> 1、Simple Factory模式
>> 专门定义一个类来负责创建其它类的实例，被创建的实例通常都具有共同的父类。

>> 2、Factory Method工厂模式
>> 将对象的创建交由父类中定义的一个标准方法来完成，而不是其构造函数，究竟应该创建何种对象由具体的子类负责决定

>> 3、Abstract Factory模式
>> 提供一个共同的接口来创建相互关联的多个对象。

>> 4、Singleton模式
>> 保证系统只会产生该类的一个实例，同时还负责向外界提供访问该实例的标准方法。

>> 5、Builder模式
>> 将复杂对象的创建同它们的具体表现形式（representation）区别开来，这样可以根据需要得到具有不同表现形式的对象。

>> 6、Prototype模式
>> 利用一个能对自身进行复制的类，使得对象的动态创建变得更加容易。


## 文档
- [Python 设计模式: 工厂模式(factory pattern)](https://mozillazg.github.io/2016/08/python-factory-pattern.html)
- [Python 设计模式: 建造者模式(builder pattern)](https://mozillazg.github.io/2016/08/python-builder-pattern.html)
- []()
- []()
- []()

####  
- [用python实现设计模式](http://python-web-guide.readthedocs.io/zh/latest/design/design.html)
- [python实践设计模式](http://www.uml.org.cn/sjms/201305283.asp)
- [Python设计模式1-创建型模式](http://www.jianshu.com/p/2450b785c329)