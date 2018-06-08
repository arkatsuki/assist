import requests
from lxml import html

USERNAME = "js"
PASSWORD = "999999"

LOGIN_URL = "http://192.168.200.248:8080/accounts/login/"
# URL = "http://192.168.200.248:8080/data/index/"
# URL = "http://192.168.200.248:8080/selfservice/login/"
URL = "http://192.168.200.248:8080/accounts/login/"


def main():
    session_requests = requests.session()
    payload = {
        "username": "js",
        "password": 999999,
        "login_type": "pwd",
        "client_language": "zh-cn",
        "template9": "",
        "template10": "",
        "finnger9": "",
        "finnger10": ""
    }

    # request_content = "username = js & password = & template9 = & finnger10 = & finnger9 = & template10 = & login_type = pwd & client_language = zh - cn"

    # headers = {'content-type': 'application/json',
    #            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

    # Perform login
    # result = session_requests.post(URL, data = payload, headers = dict(referer = LOGIN_URL))
    result = session_requests.post(URL, data=payload)
    # result = requests.post(URL, data=payload)

    # Scrape url
    # result = session_requests.get(LOGIN_URL, headers = dict(referer = LOGIN_URL))
    # tree = html.fromstring(result.content)
    # bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

    # print(type(result.content.decode()))
    # print(type(result.text))
    print(result.text)
    print('status code:',result.status_code )

    # print(type(tree))
    # print(type(''.join(result.content)))
    # print(result.content)
    f = open(r'F:\py\lib-svn\outputSvn.txt', 'w', encoding='utf-8')
    # f.write(result.text)  # write的参数需要是字符串，不能是List

    result = session_requests.get(r'http://192.168.200.248:8080/data/worktable/')
    f.write(result.text)

if __name__ == '__main__':
    main()