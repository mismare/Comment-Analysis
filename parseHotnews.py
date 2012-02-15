#! /usr/bin/python

import os
import datetime
from linkparser import hotnewsParser

if __name__ == '__main__':

    x = datetime.datetime.now()
    today =  str(x.day) + "." + str(x.month) + "." + str(x.year)

    path = "hotnews.ro/economy/" + today
    if not os.path.exists(path):
        os.makedirs(path)

    """
    Economic News
    """
    fd = open("hotnews.ro/economy/LinksToParse.txt", "r")

    line = fd.readline()
    count = 0

    while line != '' :
        path1 = path + "/" + line.rsplit('/')[-1]
      #  print "count = " + str(count) + ", " + str(line)

        X = hotnewsParser()
        X.parse(line, 'hotnews.ro', 'economy', today)

        line = fd.readline()
        count = count + 1

    fd.close()

    """
    Political News
    """

    path = "hotnews.ro/politics/" + today
    if not os.path.exists(path):
        os.makedirs(path)

    fd = open("hotnews.ro/politics/LinksToParse.txt", "r")

    line = fd.readline()
    count = 0

    while line != '' :
        path1 = path + "/" + line.rsplit('/')[-1]
        print "count = " + str(count) + ", " + str(line)

        X = hotnewsParser()
        X.parse(line, 'hotnews.ro', 'politics', today)

        line = fd.readline()
        count = count + 1

    fd.close()
