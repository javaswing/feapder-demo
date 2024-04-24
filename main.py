# -*- coding: utf-8 -*-
"""
Created on 2024-04-24 22:09:52
---------
@summary: 爬虫入口
---------
@author: javaswing
"""

from feapder import ArgumentParser

import spiders
from spiders.first_spider import FirstSpider
from spiders.ui_spider import UiSpider


def crawl_first():
    """
    AirSpider爬虫
    """
    spider = FirstSpider()
    spider.start()
    # FirstSpider().start()


def crawl_ui():
    """
    AirSpider爬虫
    """
    spider = spiders.ui_spider.UiSpider()
    spider.start()
    # UiSpider().start()


if __name__ == "__main__":
    parser = ArgumentParser(description="测试爬虫")

    parser.add_argument(
        "--crawl_first", action="store_true", help="First爬虫", function=crawl_first
    )
    parser.add_argument(
        "--crawl_ui", action="store_true", help="UI爬虫", function=crawl_ui
    )

    parser.start()

    # crawl_first()
    # crawl_ui()

    # main.py作为爬虫启动的统一入口，提供命令行的方式启动多个爬虫，若只有一个爬虫，可不编写main.py
    # 将上面的xxx修改为自己实际的爬虫名
    # 查看运行命令 python main.py --help
    # AirSpider与Spider爬虫运行方式 python main.py --crawl_xxx
    # BatchSpider运行方式
    # 1. 下发任务：python main.py --crawl_xxx 1
    # 2. 采集：python main.py --crawl_xxx 2
    # 3. 重置任务：python main.py --crawl_xxx 3

