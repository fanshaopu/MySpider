#-*- coding:utf-8 -*-
# the downloader module of my myspider
import urllib2
import urllib
#import requests
import cookielib
import sys

#reload(sys)
#sys.setdefaultencoding('GBK')
loginurl = 'http://bbs.ngacn.cc/nuke.php?func=login&normal_login'

class Downloader:
        def __init__(self):
                self.username = 'iconsky'
                self.password = '123654'
                self.expires= '3600'
                self.domain = ''
                self.values = {'login_type':'use_name','username':self.username, 'password':self.password, 'expires':self.expires}
                self.headers = headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) chrome/31.0.1650.57 Safari/537.36'}

                self.cj = cookielib.CookieJar()
                self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
                urllib2.install_opener(self.opener)

        def login(self):
                '''登陆网站'''
                
                req = urllib2.Request(loginurl,urllib.urlencode(self.values),headers=self.headers)
                response = self.opener.open(req)

                thePage = response.read()
                #print thePage
                print '---cookie---'
                for item in self.cj:
                        print item.name +":"+item.value
                        
                url = 'http://bbs.nga.cn/'
                response = self.opener.open(url)
                content = response.read()
                print content


        def download(self, url):
                response = self.opener.open(url)
                content = response.read()
                print content
                return content



if __name__ == '__main__':
    url = 'http://bbs.ngacn.cc/'
    url2 = 'http://bbs.nga.cn/read.php?tid=8481139'
    downloader = Downloader()
    downloader.login()
    #downloader.download(url2)
    pass
