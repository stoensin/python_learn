#-*- coding: utf8 -*-

import sys
from lib import SimpleDBTool, DBTool


def do_query(dbtype, sql):
    try:
        res = dbkit.query(dbtype, sql)
    except BaseException, e:
        res=dbkit.process_exception(dbtype, e)
        if not res: return None
        res=dbkit.query(dbtype, sql)
    return res

def mongo_find_one(vals=None):
    mongo = dbkit.get_mongo_collection('mail')
    try :
        res = mongo.find_one(vals)
    except BaseException as e:
        res=dbkit.process_exception('mongo', e)
        if not res: return None
        mongo = dbkit.get_mongo_collection('mail')
        res = mongo.find_one({"addr": '1@qq.com'})
    return res

if __name__ == "__main__":
    sql = 'SELECT username FROM core_customer Limit 1;'
    res = SimpleDBTool.query('edm_web', sql)
    print res
    # (('test',),)

    res = SimpleDBTool.redis.incr('test:123', 2)
    print res
    # 2

    ###########################################
    dbkit = DBTool.DBToolKit()
    res = dbkit.init_pool('edm_web')
    if not res: sys.exit(1)
    res = do_query('edm_web', sql)
    print res
    # (('test',),)

    redis = dbkit.get_redis_connection()
    res = redis.incr('test:123', 2)
    print res
    # 4

    res = dbkit.init_mongo()
    res = mongo_find_one({"addr": '1@qq.com'})
    print res
    # None







