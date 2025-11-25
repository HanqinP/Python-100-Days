import requests
from time import time
from threading import Thread

class DownloadHandler(Thread):

    def __init__(self, url):
        super.__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('/Users/Hank/'+ filename, 'wb') as f:
            f.write(resp.content)


def main():
    APIKey = '1e4cedc848c4290ea48291578f54a2d0'
    resp = requests.get('https://apis.tianapi.com/dgryl/index?key=APIKey')

    data_model = resp.json()
    for mm_dict in data_model