#! /usr/bin/python

import os
import urllib
import datetime

from BeautifulSoup import BeautifulSoup

if __name__ == '__main__':

    x = datetime.datetime.now()
    today =  str(x.day) + "." + str(x.month) + "." + str(x.year)

    path = "adevarul.ro/economy/" + today
    if not os.path.exists(path):
        os.makedirs(path)

    """
    Economic News
    """
    fd = open("adevarul.ro/economy/LinksToParse.txt", "r")

    line = fd.readline()

    while line != '' :
#        print line
        path1 = path + "/" + line.rsplit('/')[-1]
 #       print path1
        if not os.path.exists(path1):
            os.makedirs(path1)
            """
            save article and comments
            """
            #to change here
            fd1 = open(path1+"/articol.html", "w")

            pFile = urllib.urlopen(line)
            fileToRead = pFile.read()
            pFile.close()
            soup = BeautifulSoup(fileToRead)

            rawP = soup.findAll(attrs={"class":"header"})
            fd1.write(str(rawP[0]))

            rawP = soup.findAll(attrs={"class":"bb-wg-text"})
            fd1.write(str(rawP[0]))
            fd1.close()

            fd1 = open(path1 + "/comments" + str(x.hour) + ":" + str(x.minute) + ".html", "w")
            rawP = soup.findAll(attrs={"class":"art-comment"})
            fd1.write(str(rawP))

            fd1.close()

        else:
            """
            save just comments
            """
            fd1 = open(path1 + "/comments" + str(x.hour) + ":" + str(x.minute) + ".html", "w")
            rawP = soup.findAll(attrs={"class":"art-comment"})
            fd1.write(str(rawP))

            fd1.close()


        line = fd.readline()


    fd.close()

"""
    pFile = urllib.urlopen(economySource)
    fileToRead = pFile.read()
    pFile.close()
    soup = BeautifulSoup(fileToRead)

    rawP = soup.findAll(attrs={"class":"articol_lead_full"})
    EconomyList = []

    or i in rawP:
        date = i.findAll('span', attrs={"class":"data"})
        current_date = date[0].contents[0]
        if ':' in current_date or today in current_date:
            ahref = i.findAll("a")
            link = ahref[0].attrMap['href']
            EconomyList.append(link)
"""
