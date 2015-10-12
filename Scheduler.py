#-*- coding:utf-8 -*-
# the scheduler module of my spider
# the url schedule
import Queue

class Scheduler:
        def __init__(self):
                self.urls = set()
                self.queue = Queue.Queue()

        def __init__(self, starturls):
                self.urls = set()
                self.queue = Queue.Queue()
                for url in starturls:
                        self.push(url)

        def push(self, url):
                
                if url in self.urls:
                        return
                else:
                        self.queue.put(url)
                        self.urls.add(url)

        def pop(self):
                return self.queue.get()

        def isEmpty(self):
                return self.queue.empty()

if __name__ == '__main__':
        starturl = ['www']
        scheduler = Scheduler(starturl)
        print scheduler.pop()
        
