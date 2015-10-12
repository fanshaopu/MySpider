#-*- coding:utf-8 -*-
# the pipeline module of my spider
# to store the web pages into local files

class Pipeline:

	def filepipeline(self, url, content):
		filename = url.split('//')[-1].replace('/', '%').replace('?', '#')
		fw = open(filename, 'w')
		fw.write(content)
		fw.close()

if __name__ == '__main__':
	pipeline = Pipeline()
	url = 'http://www.baidu.com'
	content = 'beijing'
	pipeline.filepipeline(url, content)
