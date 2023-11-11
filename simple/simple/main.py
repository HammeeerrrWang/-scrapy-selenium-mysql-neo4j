# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName     :main.py
# @Time         :2023/11/9 21:47
# @Author       :solr.Sky

from scrapy.cmdline import execute

if __name__ == '__main__':
    execute(['scrapy', 'crawl', 'hw_phone'])