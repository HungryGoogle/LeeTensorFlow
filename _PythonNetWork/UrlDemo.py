#获取页面内容
# def get_html(url):
#     #import urllib2
#     #import HTMLParser
#     print (u'start crawl %s ...' % url)
#     headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0'}
#     req = urllib2.Request(url=url,headers=headers)
#     try:
#         html = urllib2.urlopen(req).read().decode('utf-8')
#         html=HTMLParser.HTMLParser().unescape(html)#处理网页内容， 可以将一些html类型的符号如" 转换回双引号
#         #html = html.decode('utf-8','replace').encode(sys.getfilesystemencoding())#转码:避免输出出现乱码
#     except urllib2.HTTPError,e:
#         print u"连接失败，错误原因：%s " % e.code
#         return None
#     except urllib2.URLError,e:
#         if hasattr(e,'reason'):
#             print u"连接失败，错误原因:%s " % e.reason
#             return None
#     return html