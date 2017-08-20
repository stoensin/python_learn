# -*- coding: utf-8 -*-
#

import sys
import traceback
import time
import redis
import psycopg2
import MySQLdb
import pymongo
from DBUtils.PooledDB import PooledDB

from . import settings

# 数据库对象
class DatabaseObj(object):

    def __init__(self):
        self.pool = None
        self.mongo_connect = None

class DBBase(object):

    def __init__(self, creater, dbtype, params=None, charset='UTF8', outerr=True):
        self.db = DatabaseObj()
        self.creater = creater
        self.dbtype = dbtype
        self.params = params or {}
        self.charset = charset
        self.outerr = outerr

    def init_pool(self):
        if self.creater=='mysql': self.params.update(creator=MySQLdb, charset=self.charset)
        if self.creater=='postgresql': self.params.update(creator=psycopg2, failures=(psycopg2.InterfaceError, ))
        try:
            self.db.pool = PooledDB(maxusage=1000, **self.params)
        except BaseException as e:
            if self.outerr:
                sys.stderr.write('init %s pool except' % self.dbtype)
                sys.stderr.write(traceback.format_exc())
            return False
        return True

    # 取得数据库连接
    def __get_connect(self):
        conn = self.db.pool.connection()
        return conn

    # 查询数据库
    def query(self, sql, args=None):
        # 取得数据库连接、游标
        conn = self.__get_connect()
        cr = conn.cursor()
        # 执行查询，并取得结果
        cr.execute(sql, args)
        res = cr.fetchall()
        # 关闭游标、连接
        cr.close()
        conn.close()
        return res

    # 执行数据库操作
    def do(self, sql, args=None):
        conn = self.__get_connect()
        cr = conn.cursor()
        # 执行操作
        cr.execute(sql, args)
        cr.close()
        conn.close()
        return True

    # 执行数据库操作
    def doMany(self, sql, args=None):
        conn = self.__get_connect()
        cr = conn.cursor()
        # 执行操作
        cr.executemany(sql, args)
        # 关闭游标、数据库连接
        cr.close()
        conn.close()
        return True

    # 维护 数据库 连接
    def maintain_pool(self, trycount=5, timeout=3) :
        i = 0
        while True:
            i += 1
            sys.stderr.write('try connect %s : %d' % (self.dbtype, i))
            try:
                conn = self.__get_connect(self.dbtype)
                break
            except BaseException, e:
                pass
            if i==trycount:
                sys.stderr.write('reconnect %s failure\n' % self.dbtype)
                self.error(traceback.format_exc())
                return False
            time.sleep(timeout)
        self.error('reconnect %s success' % self.dbtype)
        return conn

    ############################################################
    # 处理异常
    def process_exception(self, e):
        if self.creater == 'mysql' and type(e) == MySQLdb._mysql.OperationalError :
            return self.maintain_pool()
        if self.creater == 'postgresql' and type(e) in (psycopg2.OperationalError, psycopg2.InterfaceError) :
            return self.maintain_pool()
        if self.dbtype == 'mongo' :
            return self.maintain_mongoPool()
        return False

    ############################################################
    # MongoDB 操作
    # 初始化 MongoDB 连接
    def init_mongo(self):
        try:
            self.db.mongo_connect = pymongo.Connection(
                self.params['host'],
                self.params['port'],
            )
            self.db.pool = self.db.mongo_connect[self.params['dbname']]
            self.db.pool.authenticate(self.params['user'], self.params['pass'])
        except Exception, e :
            if self.outerr :
                self.error('init mongodb connect except')
                self.error(traceback.format_exc())
            return False
        return True

    # 取得 MongoDB 的 Collection 对象
    def get_mongo_collection(self, cname) :
        return self.db.pool[cname]

    # 维护 MongoDB 连接
    def maintain_mongoPool(self, trycount=5) :
        self.error('maintain mongodb exception')
        i = 0
        while self.init_mongo(outerr=False) == False:
            i += 1
            self.error('try connect mongodb : %d' % i)
            if i == trycount :
                self.error('reconnect mongodb failure')
                self.error(traceback.format_exc())
                return False
            time.sleep(3)
        self.error('reconnect mongodb success')
        return True


class MysqlPool(DBBase):
    pass

class PgsqlPool(DBBase):
    pass

class MongoPool(DBBase):
    pass

######################################################
# def getDBObject(creater, dbtype, charset='UTF8', outerr= True):
#     """ 工厂方法 获取对应数据库的对象"""
#     _settings = settings.DATABASES
#     if creater in ('mysql', 'postgresql'):
#         obj = DBBase(creater, dbtype, _settings[creater][dbtype], charset, outerr)
#         obj.init_pool()
#         return obj
#     elif creater=='mongo':
#         obj = DBBase(creater, dbtype, _settings[creater], charset, outerr)
#         obj.init_mongo()
#         return obj

def getDBObject(creater, dbtype, charset='UTF8', outerr= True):
    """ 工厂方法 获取对应数据库的对象"""
    _settings = settings.DATABASES
    if creater == 'mysql':
        obj = MysqlPool(creater, dbtype, _settings[creater][dbtype], charset, outerr)
        obj.init_pool()
        return obj
    if creater == 'postgresql':
        obj = PgsqlPool(creater, dbtype, _settings[creater][dbtype], charset, outerr)
        obj.init_pool()
        return obj
    elif creater=='mongo':
        obj = MongoPool(creater, dbtype, _settings[creater], charset, outerr)
        obj.init_mongo()
        return obj

######################################################
# redis 连接
def get_redis_connection():
    redis_set = settings.REDIS_SET
    __redis_pool = redis.ConnectionPool(
        host=redis_set['host'], port=redis_set['port'], db=0
    )
    return redis.StrictRedis(connection_pool=__redis_pool)

