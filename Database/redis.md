

```
import redis
redis_pool = redis.ConnectionPool(host='localhost', port=6379, db=0) 
redis = redis.StrictRedis(connection_pool=redis_pool)  # 定义了一个连接池类，该类返回连接池中的一个连接给调用者

r = redis.Redis(host='localhost', port=6379, db=0)
```

# 文档
- [使用Python操作Redis](http://debugo.com/python-redis/)
- [Python—操作redis](http://www.cnblogs.com/melonjiang/p/5342505.html)