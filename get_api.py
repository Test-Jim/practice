from flask import Flask
from bs4 import  BeautifulSoup
import urllib.request

app = Flask(__name__)

@app.route('/get_baidu')#接口url=get_baidu
def get_baidu_info():
    srcstrig=''
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    req = urllib.request.Request(url=r'https://www.baidu.com',headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read().decode('utf-8')
    soup= BeautifulSoup(html, "html.parser")#获取baidu网页源码
    contents=soup.find_all('div',id='lg')
    for index in contents[0].select('img'):
        srcstrig+=index.get('src')#如果多个src，则累加返回

    return srcstrig#返回src
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
