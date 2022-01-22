import requests
from lxml import etree
from time import sleep
a=0
s1=''
l1=[]
out=''
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}
p=input('汉字:(请严格用“、”隔开!)\n')
if p[-1]!='、':
    p=p+'、'
for i in p:
    if i=='、':
        l1.append(s1)
        s1=''
    else:
        s1=s1+i
for s in l1:
    sleep(0.5)
    urls='https://hanyu.baidu.com/s'
    param={
        'wd':s,
        'ptype':'zici'
    }
    res=requests.get(url=urls,headers=headers,params=param).text
    tree=etree.HTML(res)
    try:
        pinyin=tree.xpath('//div[@id="pinyin"]//span/b/text()')[0]
        if pinyin[0] == '[':
            pinyin=pinyin[2:-2]
        if l1[-1] != s:
            print(pinyin+'、',end='')
            out=out+pinyin+'、'
        if l1[-1] == s:
            print(pinyin,end='')
            out=out+pinyin
    except:
        print('ERROR、',end='')
        out=out+'ERROR、'
        if l1[-1] == s:
            print('ERROR',end='')
            out=out+'ERROR'
with open('./pinyin.txt','w',encoding='utf-8') as fp:
    fp.write(out)
    print('\n拼音保存成功！')
input('')
