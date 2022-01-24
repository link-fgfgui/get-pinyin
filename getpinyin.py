import requests,time
from lxml import etree
a,s1,l1,list_other,out,dic_other,headers=0,'',[],[],'',{},{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}
p=input('汉字:(支持批量输入,请严格用“、”隔开!)\n')
if p[-1]!='、':
    p=p+'、'
for i in p:
    if i=='、':
        l1.append(s1)
        s1=''
    else:
        s1=s1+i
for s in l1:
    time.sleep(0.5)
    urls='https://hanyu.baidu.com/s'
    param={'wd':s,'ptype':'zici'}
    tree=etree.HTML(requests.get(url=urls,headers=headers,params=param).text)
    try:
        pinyin_list=tree.xpath('//div[@id="pinyin"]//span/b/text()')
        if len(pinyin_list) > 1:
            dic_other={'zi':s,'yin':pinyin_list}
            list_other.append(dic_other)
        pinyin=pinyin_list[0]
        if pinyin[0] == '[':
            pinyin=pinyin[2:-2]
        if l1[-1] != s:
            print(pinyin+'、',end='')
            out=out+pinyin+'、'
        elif l1[-1] == s:
            print(pinyin,end='')
            out=out+pinyin
    except:
        if l1[-1]!=s:
            print('ERROR、',end='')
            out=out+'ERROR、'
        elif l1[-1] == s:
            print('ERROR',end='')
            out=out+'ERROR'
with open('./pinyin.txt','w',encoding='utf-8') as fp:
    fp.write(out)
    print('\n拼音已经写入到本地!')
if len(list_other)!=0:
    if input('发现其中有多音字(词),是否查看?(y/n)')== 'y':
        out,s1='',''
        for d in list_other:
            print()
            print(d['zi']+':',end='')
            out=out+'\n'+d['zi']+':'
            for s in d['yin']:
                if s[0] == '[':
                    s1=s[2:-2]
                elif s[0]!='[':
                    s1=s
                if s==d['yin'][-1]:
                    out=out+s1
                    print(s1,end='')
                elif s!=d['yin'][-1]:
                    out=out+s1+','
                    print(s1+',',end='')
        with open('./pinyin.txt','a',encoding='utf-8') as fp:
            fp.write(out)
        print('\n多音字已经写入到本地!')                
input('\n按Enter键结束')