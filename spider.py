import sys
import urllib
import urllib2
import numpy as np
#from PIL import Image
#from io import BytesIO
#import cStringIO
import cookielib
import re

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener)

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
myheaders = { 'User-Agent' : user_agent }
urlimage="http://yjsymis.hrbeu.edu.cn/gsmis/Image.do"
imageReq = urllib2.Request(urlimage,headers=myheaders)
imageRes = opener.open(imageReq)
fileout = open('D:/2.jpg','wb')   #验证码保存在此
fileout.write(imageRes.read())
fileout.close()
#image = Image.open( cStringIO.StringIO(imageRes.read() ) )
#image.save('D:/1.jpg')
#image.show()

str = input("Enter your input: ")           #输入验证码
print str
values={}
values['id']='username'                #登录用户名和密码
values['password']='password'
values['checkcode']=str
data = urllib.urlencode(values)
url="http://yjsymis.hrbeu.edu.cn/gsmis/indexAction.do"
request = urllib2.Request(url,data,myheaders)
response=opener.open(request)

#print response.read().decode('GBK')
print '-----------------------------------------------------'
#opener.close()
#print response.headers

course="http://yjsymis.hrbeu.edu.cn/gsmis/py/pyYiXuanKeCheng.do"
course2 = "http://yjsymis.hrbeu.edu.cn/gsmis/toModule.do?prefix=/py&page=/pySelectCourses.do?do=xsXuanKe"
myheaders['Upgrade-Insecure-Requests']='1'
myheaders['Accept']='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
myheaders['Referer']='http://yjsymis.hrbeu.edu.cn/gsmis/peiyang/xuanke/PyXuanKeMenu.jsp'
#data2 = urllib.urlencode(values)
request2 = urllib2.Request(course2,data,myheaders)
request3 = urllib2.Request(course,data,myheaders)
#print request2.get_data()
#response2=opener.open(request2)
try:
    response2=opener.open(request2)
    response2 = opener.open(request3)
    #print response2.headers
except urllib2.URLError as e:
    print e
    if hasattr(e, 'code'):
        print 'Error code:', e.code
    elif hasattr(e, 'reason'):
        print 'Reason:', e.reason
finally:
    str = response2.read().decode('GBK')
    #reg='<td><div align="center">(.*?)</div>&nbsp;</td>'
    reg = '<td>(.*?)&nbsp;'
    reg2 = '<tr class="tablefont2" style=\'word-break:break-all;\' onMouseOut="this.style.backgroundColor=\'#FFFFFF\' " onMouseOver="this.style.backgroundColor=\'#FFF0C5\'" bgcolor="#FFFFFF">(.*?)</tr>'
    pattern = re.compile(reg2,re.M|re.I|re.S)
    all = re.findall(pattern,str)
    #print all
    for x in all:
        #print x
        pattern2 = re.compile(reg,re.M|re.I|re.S)
        msg = re.findall(pattern2,x)
        if len(msg)>8:
            if msg[1]!=None:
                print 'coures:'+ msg[1].strip() + ' teacher:' + msg[8].strip()[20:-6]
        #print teacher
        #print "\n"
    #match = re.search(pattern,str)
    #match.find()
    #print match.group(1)

    #print str
    #print response2.headers
    #if response2:
        #response2.close()
#response=opener.open(request)
#print response2.read(100)
#print response2.read().decode('GBK')