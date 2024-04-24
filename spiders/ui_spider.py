# -*- coding: utf-8 -*-
"""
Created on 2024-04-24 22:15:26
---------
@summary:
---------
@author: javaswing
"""

from feapder.utils.webdriver import (
    PlaywrightDriver,
    InterceptResponse,
    InterceptRequest,
)

import feapder


class UiSpider(feapder.AirSpider):
    __custom_setting__ = dict(
        RENDER_DOWNLOADER="feapder.network.downloader.PlaywrightDownloader",
        PLAYWRIGHT=dict(
            user_agent=None,  # 字符串 或 无参函数，返回值为user_agent
            proxy=None,  # xxx.xxx.xxx.xxx:xxxx 或 无参函数，返回值为代理地址
            headless=False,  # 是否为无头浏览器
            driver_type="firefox",  # chromium、firefox、webkit
            timeout=30,  # 请求超时时间
            window_size=(1024, 800),  # 窗口大小
            executable_path=None,  # 浏览器路径，默认为默认路径
            download_path=None,  # 下载文件的路径
            render_time=0,  # 渲染时长，即打开网页等待指定时间后再获取源码
            wait_until="networkidle",  # 等待页面加载完成的事件,可选值："commit", "domcontentloaded", "load", "networkidle"
            use_stealth_js=False,  # 使用stealth.min.js隐藏浏览器特征
            # page_on_event_callback=dict(response=on_response),  # 监听response事件
            # page.on() 事件的回调 如 page_on_event_callback={"dialog": lambda dialog: dialog.accept()}
            storage_state_path=None,  # 保存浏览器状态的路径
            url_regexes=["/pubapi/projectcomment", "/pubapi/promaybelike"],  # 拦截接口，支持正则，数组类型
            save_all=True,  # 是否保存所有拦截的接口
        ),
    )

    def start_requests(self):
        yield feapder.Request("https://www.ui.cn/detail/499947.html", render=True)

    def parse(self, request, response):
        driver: PlaywrightDriver = response.driver
        data = driver.get_all_json("/pubapi/projectcomment")
        print("/pubapi/projectcomment 接口返回的数据", data)
        data = driver.get_all_json("/pubapi/promaybelike")
        print("/pubapi/promaybelike 接口返回的数据", data)
        print("------ 测试save_all=True ------- ")


if __name__ == "__main__":
    UiSpider().start()
