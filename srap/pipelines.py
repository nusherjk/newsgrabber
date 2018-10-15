
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ToDo
#create a filter function to be able make item['released'] timestamp input in MYSQL database(done)
#filter each item into VARCHAR data(done)
#Database input check(done)
#Database Update: update the data in database if the data is repeated/updated. ***CRITICAL***
#create database which takes item[released] works as a timestamp and check (done)
import pymysql
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request

class SQLinsertitems(object):
    def process_item(self,item,spider):
        connection = pymysql.connect(host='localhost', 
                                     user='root', #your username
                                     password='', #password
                                     db='pa', #database name
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO pad (papername, newstitle, releasedate, url, newscontent, imagelink, vidlink)  VALUES ( %s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, (item['papername'],item['title'],self.timestamp_proccessor(item['released']), item['url'], item['content'], item['imgl'], 'NULL'))
            connection.commit()
        except pymysql.Error as e:
            return str(e)
        finally:
            connection.close()
#
    def timestamp_proccessor(self,string):
        uf = string
        date = uf.split('T')
        timel = date[1].split('+')
        time = timel[0]
        data = date[0] + ' ' +time

        return data


class AggregatorPipeline(object):
    def process_item(self, item, spider):
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='pa',
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO pad (papername, newstitle, releasedate, url, newscontent, imagelink, vidlink)  VALUES ( %s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, (
                item['papername'], item['title'], self.timestamp_proccessor(item['released'])+'06:00', item['url'],
                item['content'], item['imgl'], 'NULL'))
            connection.commit()
        except pymysql.Error as e:
            return str(e)
        finally:
            connection.close()

    #
    def timestamp_proccessor(self, string):
        uf = string
        date = uf.split('T')
        timel = date[1].split('+')
        time = timel[0]
        data = date[0] + ' ' + time

        return data


class Dateproccessor(object):

    def process_item(self, item, spider):
        #date = item['released']
        #insert
        #into
        #tablename(timestamp_value)
        #values(TO_TIMESTAMP(:ts_val, 'YYYY-MM-DD HH24:MI:SS'));
        # data-published="2018-05-01T00:00:00+06:00"
        pass



