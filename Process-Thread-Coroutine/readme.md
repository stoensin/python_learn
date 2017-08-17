

1. CPU密集型操作
2. IO密集型操作
3. 网络请求密集型操作

### IO密集型测试(包含网络请求密集型操作)
> 测试IO密集型(爬虫或数据库访问)——（主要测试多线程与协程，单线程与多进程就不测了，因为没有必要）
> 当并发数不断增大时，协程的效率确实比多线程要高，但在并发数不是那么高时，两者差异不大。
> [Python多线程鸡年不鸡肋](https://thief.one/2017/02/17/Python%E5%A4%9A%E7%BA%BF%E7%A8%8B%E9%B8%A1%E5%B9%B4%E4%B8%8D%E9%B8%A1%E8%82%8B/)

### CPU密集型
> CPU密集型，选择科学计算的一些功能，计算所需时间。（主要测试单线程、多线程、协程、多进程）
> 在CPU密集型的测试下，多进程效果明显比其他的好，多线程、协程与单线程效果差不多。这是因为只有多进程完全使用了CPU的计算能力。在代码运行时，我们也能够看到，只有多进程可以将CPU使用率占满。

- [CPU-bound(计算密集型) 和I/O bound(I/O密集型)](http://www.cnblogs.com/balaamwe/archive/2012/07/27/2611622.html)
- [CPU密集型和I/O密集型区别](http://www.lao8.org/article_1638/cpu_mijixing)

- [Linux信号基础](http://www.cnblogs.com/vamei/archive/2012/10/04/2711818.html)
- [Python标准库07 信号 (signal包，部分os包)](http://www.cnblogs.com/vamei/archive/2012/10/06/2712683.html)

- [Python 中的进程、线程、协程、同步、异步、回调](https://segmentfault.com/a/1190000001813992)
- [编程中的进程、线程、协程、同步、异步、回调](https://wangdashuaihenshuai.github.io/2015/10/17/%E7%BC%96%E7%A8%8B%E4%B8%AD%E7%9A%84%E8%BF%9B%E7%A8%8B%E3%80%81%E7%BA%BF%E7%A8%8B%E3%80%81%E5%8D%8F%E7%A8%8B%E3%80%81%E5%90%8C%E6%AD%A5%E3%80%81%E5%BC%82%E6%AD%A5%E3%80%81%E5%9B%9E%E8%B0%83/)