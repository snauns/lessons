from bs4 import BeautifulSoup as bs
import requests as r
class ParserHTLM:
    def __init__(self, url:str):
        self.Counter : int = 0
        self.Url : str = url
        self.Result : dict = {}
    def ParseNBU(self, separator1:str, separator2:str, isUsd:bool):
        response =r.get(self.Url)
        response_content = response.content
        html = bs(response_content, features="html.parser")
        tags = html.find_all('div', attrs={'class' : separator1})
        usdTag = None
        if isUsd:
            usdTag = tags[1].find(separator2)
        else:
            usdTag = tags[0].find(separator2)
        value = float(usdTag.text.replace(' ', '').replace(',', '.'))
        self.Result[self.Counter] = value