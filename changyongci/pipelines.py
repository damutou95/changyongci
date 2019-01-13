# -*- coding: utf-8 -*-
import pymysql
import pymysql.cursors
from twisted.enterprise import adbapi
#from scrapy.crawler import Settings as settings
#from changyongci import settings
#don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
class ChangyongciPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool
    @classmethod
    def from_settings(cls,settings):
        dbparams = dict(
            host = settings['MYSQL_HOST'],
            db = settings['MYSQL_DBNAME'],
            user = settings['MYSQL_USER'],
            passwd = settings['MYSQL_PASSWORD'],
            charset = 'utf8',
            #游标设置
            cursorclass = pymysql.cursors.DictCursor,
            #设置编码是否使用UNICODE
            use_unicode = True,

        )
        #通过Twisted提供的容器连接数据库
        dbpool = adbapi.ConnectionPool('pymysql',**dbparams)
        return cls(dbpool)
    #插入数据到数据库
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)  # 调用插入的方法
        query.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
        return item
    def _conditional_insert(self, cursor, item):
        insert_sql ="""
        insert into frequency_wds(frequency_wd,use_rate)
         VALUES(%s,%s)
        """
        cursor.execute(insert_sql, (item['changyongci'],item['shiyongpinlv']))
    def _handle_error(self, failue, item, spider):
      print(failue)

#from twisted.enterprise import adbapi
#import pymysql
#import pymysql.cursors


#class ChangyongciPipeline(object):
  # def __init__(self, dbpool):
   #     self.dbpool = dbpool

    #@classmethod
   # def from_settings(cls, settings):
    #    dbparams = dict(
     #       host=settings['MYSQL_HOST'],
#  db=settings['MYSQL_DBNAME'],
#  user=settings['MYSQL_USER'],
#passwd=settings['MYSQL_PASSWORD'],
# charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
#            cursorclass=pymysql.cursors.DictCursor,
#            use_unicode=True,
#       )
#       dbpool = adbapi.ConnectionPool('pymysql', **dbparams)  # **表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
#       return cls(dbpool)  # 相当于dbpool付给了这个类，self中可以得到

    # pipeline默认调用
#    def process_item(self, item, spider):
#       query = self.dbpool.runInteraction(self._conditional_insert, item)  # 调用插入的方法
#       query.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
#       return item

    # 写入数据库中
    # SQL语句在这里
# def _conditional_insert(self, tx, item):
#       """insert_sql =
#       insert into ciyu(changyongci, shiyongpinlv)
#       VALUES(%s,%s)
#       """
#        tx.execute(insert_sql, (item['changyongci'],item['shiyongpinlv']))

# 错误处理方法
#  def _handle_error(self, failue, item, spider):
#       print(failue)
