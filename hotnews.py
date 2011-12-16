#! /usr/bin/python

import urllib
import datetime

from BeautifulSoup import BeautifulSoup

import xml.dom.minidom


economySource = 'http://www.hotnews.ro/rss/economie'
politicSource = 'http://www.hotnews.ro/rssCateg?categoryId=20002'

if __name__ == '__main__':

    x = datetime.datetime.now()
    today =  str(x.day) + "." + str(x.month) + "." + str(x.year)


    """
    Economic news
    """

    document = urllib.urlopen(economySource).read()

    dom = xml.dom.minidom.parseString(document)
    rawP = dom.getElementsByTagName("item")

    EconomyList = []

    for i in rawP:
        link = i.getElementsByTagName("link")[0]
        EconomyList.append(link.firstChild.nodeValue)

    fd = open('hotnews.ro/economy/LinksToParse.txt', 'w')
    fd.truncate()
    for i in EconomyList:
        fd.write('%s\n' %i)
    fd.close()


    """
    Political news
    """
    document = urllib.urlopen(politicSource).read()

    dom = xml.dom.minidom.parseString(document)
    rawP = dom.getElementsByTagName("item")

    PoliticList = []

    for i in rawP:
        link = i.getElementsByTagName("link")[0]
        PoliticList.append(link.firstChild.nodeValue)

    fd = open('hotnews.ro/politics/LinksToParse.txt', 'w')
    fd.truncate()
    for i in PoliticList:
        fd.write('%s\n' %i)
    fd.close()


    """
    pFile = urllib.urlopen(economySource)
    fileToRead = pFile.read()
    pFile.close()
    soup = BeautifulSoup(fileToRead)

    rawP = soup.findAll(attrs={"class":"articol_lead_full"})
    EconomyList = []

    for i in rawP:
        date = i.findAll('span', attrs={"class":"data"})
        current_date = date[0].contents[0]
        if ':' in current_date or today in current_date:
            ahref = i.findAll("a")
            link = ahref[0].attrMap['href']
            EconomyList.append(link)

    fd = open('hotnews.ro/economy/LinksToParse.txt', 'w')
    fd.truncate()
    for i in EconomyList:
        fd.write('%s\n' %i)
    fd.close()

    """

    """
    Political news
    """
    """
    pFile = urllib.urlopen(politicSource)
    fileToRead = pFile.read()
    pFile.close()
    soup = BeautifulSoup(fileToRead)

    rawP = soup.findAll(attrs={"class":"articol_lead_full"})
    PoliticList = []

    for i in rawP:
        ahref = i.findAll("a")
        link = ahref[0].attrMap['href']
        PoliticList.append(link)

    fd = open('hotnews.ro/politics/LinksToParse.txt', 'w')
    fd.truncate()
    for i in PoliticList:
        fd.write('%s\n' %i)
    ifd.close()
    """
