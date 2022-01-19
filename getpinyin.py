import requests
from time import sleep
a=0
s1=''
l1=[]
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}
while 1==1:
    p=input('汉字:\n')
    p=p+'、'
    for i in p:
        if i=='、':
            l1.append(s1)
            s1=''
        else:
            s1=s1+i
    for s in l1:
        urls='https://hanyu.baidu.com/hanyu/ajax/sugs?mainkey={}'.format(s)
        sleep(0.5)
        res=requests.get(url=urls,headers=headers).json()
        try:
            pinyin=res['data']['ret_array'][0]['pinyin'][0]
            print('、'+pinyin,end='')
        except:
            print('、ERROR',end='')
            #print()
            #print(res)
            #print(s)
    
