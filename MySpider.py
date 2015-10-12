#-*- coding:utf-8 -*-
# the interface moduler of my spider
from Downloader import Downloader
from Scheduler import Scheduler
from Pipeline import Pipeline 
from Pageprocessor import Pageprocessor
import time

class MySpider:
    def __init__(self):
        self.starturl = ['http://bbs.nga.cn/read.php?tid=8481139']
        self.sleeptime = 5   # 休眠时间
    
    def start(self):
        # 下载模块
        downloader = Downloader()    
        downloader.login()
        # 调度模块
        scheduler = Scheduler(self.starturl)
        # 处理模块
        pageprocessor = Pageprocessor()
        # 输出模块
        pipeline = Pipeline()

        print 'spider is starting...'
        while not scheduler.isEmpty():
            # 休眠
            time.sleep(self.sleeptime)
            
            url = scheduler.pop()
            print url
            content = downloader.download(url)


            # 保存到文件中
            pipeline.filepipeline(url, content)
            print url + ' saved'
        

if __name__ == '__main__':
    spider = MySpider()
    spider.start()
    
