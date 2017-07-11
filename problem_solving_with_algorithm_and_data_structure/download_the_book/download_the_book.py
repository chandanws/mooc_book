#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import PyPDF2
import pdfkit
from PyPDF2 import PdfFileMerger


def get_url_list():
    response = requests.get("http://interactivepython.org/courselib/static/pythonds/index.html")
    soup = BeautifulSoup(response.content, 'html.parser')
    div_list = soup.find('div', attrs={'class': 'toctree-wrapper compound'})
    # print(div_list)
    a_s = div_list.find_all('a', attrs={'class': 'reference internal'})
    urls = []
    names = []
    for a in a_s:
        #   url = a['href']
        url = "http://interactivepython.org/courselib/static/pythonds/" + a['href']
        name = a.get_text()
        urls.append(url)
        names.append(name)
    return urls, names


if __name__ == '__main__':
    urls, names = get_url_list()
    # path_wkthmltopdf = r'C:\wkhtmltopdf.exe'
    # config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    for ii in range(len(urls)):
        print(ii)
        pdfkit.from_url(urls[ii], names[ii] + '.pdf')
