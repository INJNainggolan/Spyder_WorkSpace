#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 11:30:22 2017

@author: nainggolan
"""

# -*- coding: UTF-8 -*-
__author__= 'JK'
import urllib
import urllib2
import re
import  thread
import time

#糗事百科
class QSBK:

    #初始化方法，定义一些变量
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
        #初始化headers
        self.headers = {'User-Agent':self.user_agent}
        #存放段子的变量
        self.stories=[]
        #存放程序是否继续运行的变量
        self.enable = False
    #传入某一页的索引获得页面代码   
    def getPage(self,pageIndex):
        try:
            url='http://www.qiushibaike.com/hot/page/'+str(pageIndex)
            request = urllib2.Request(url,headers =self.headers)
            response = urllib2.urlopen(request)
            #将页面转换为UTF-8编码
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError as e:
            if hasattr(e,'reason'):
                print '连接糗事百科失败，错误原因',e.reason
                return None
    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print '页面加载失败'
            return None
        # h2>(.*?)</.*?content">(.*?)</div(.*?)number">(.*?)<
        pattern = re.compile(r'h2>(.*?)</h2.*?content">(.*?)</div(.*?)number">(.*?)</i.*?number">(.*?)</',re.S)
        items = re.findall(pattern,pageCode)
        #用来存储每一页的段子
        pageStories = []
        #遍历正则表达式匹配信息
        for item in items:
            #是否含有图片
            haveImag = re.search('img',item[2])
            #如果不含有图片，把它加入list中去
            if not haveImag:
                replacrBR= re.compile('<br/>')
                text = re.sub(replacrBR,'\n',item[1])
                #item[0]是发布者姓名，item[1]是发布内容，item[2]是点赞数
                pageStories.append([item[0].strip(),text.strip(),item[3].strip(),item[4].strip()])
        return pageStories

    def loadPage(self):
        if self.enable ==True:
            if len(self.stories)<2:
                #获取新一页
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex+=1

    def getOneStoryself(self,pageStories,pageIndex):
        #遍历每一页的段子
        for story in pageStories:
            #等待用户输入
            input = raw_input()
            self.loadPage()
            #如果输入Q则程序结束
            if input =='Q':
                self.enable =False
                return
            print u"第%d页\t发布人:%s\t赞:%s\t 评论:%s\n%s" %(pageIndex,story[0],story[2],story[3],story[1])


    def start(self):
        print u'正在读取糗事百科，按回车查看新段子，Q退出'

        self.enable = True
        self.loadPage()
        nowpage = 0
        while self.enable:
            if len(self.stories)>0:
                pageStories = self.stories[0]
                nowpage +=1
                #将全局list中第一个元素删除，因为已经取出
                del self.stories[0]

                self.getOneStoryself(pageStories,nowpage)



if __name__ == '__main__':
    spider = QSBK()
    print spider.start()