import requests
import re


def input_code():
    code = input("please input code:")
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

if __name__ == "__main__":
    url = 'http://hq.sinajs.cn/list='+input_code()
    data_str = getHTMLText(url)

    p = '\"([^\"]*)\"'
    matchObj = re.match(p,data_str)
    print(matchObj.group())





