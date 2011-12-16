#! /usr/bin/python

import urllib
import datetime

from BeautifulSoup import BeautifulSoup

economySource = 'http://www.adevarul.ro/financiar/'

if __name__ == '__main__':

    x = datetime.datetime.now()
    today = str(x.day) + "." + str(x.month) + "." + str(x.year)[2] + str(x.year)[3]

    """
    Economic news
    """
    pFile = urllib.urlopen(economySource)
    fileToRead = pFile.read()
    pFile.close()
    soup = BeautifulSoup(fileToRead)

    EconomyList = []

    rawP = soup.findAll(attrs={"class":"bb-md-news-l bb-md-news_base cover_story"})

    for i in rawP:
        date = i.findAll('span', attrs={"class":"time"})
        current_date = date[0].contents[0]
        if 'Acum' in current_date or today in current_date:
            ahref = i.findAll("a")
            link = 'http://www.adevarul.ro' + ahref[0].attrMap['href']
            EconomyList.append(link)

    rawP = soup.findAll(attrs={"class":"bb-md-news-l bb-md-news_base news_md_section_home"})

    for i in rawP:
        date = i.findAll('span', attrs={"class":"date"})
        current_date = date[0].contents[0]
        if ':' in current_date or today in current_date:
            ahref = i.findAll("a")
            link = 'http://www.adevarul.ro' + ahref[0].attrMap['href']
            EconomyList.append(link)

    fd = open('adevarul.ro/economy/LinksToParse.txt', 'w')
    fd.truncate()
    for i in EconomyList:
        fd.write('%s\n' %i)
    fd.close()
