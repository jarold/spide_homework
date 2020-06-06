import requests
import re


def input_code():
    code = input("please input code (like input : sz000001):")
    if len(code) == 8:
        print("input code:",code)
        return code
    else:
        print("error code")

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "error"

def re_Text(code,text):
    '''对获取的html进行正则化筛选返回列表'''
    p = re.compile(r'\"([^\"].*)\"')
    ss = p.findall(text)[0]
    d_list = re.split(r',', ss)
    d_list.append(code)
    return d_list

if __name__ == "__main__":
    code = input_code()
    url = 'http://hq.sinajs.cn/list='+code
    data_str = getHTMLText(url)
    data_list = re_Text(code,data_str)
    print(data_list)







