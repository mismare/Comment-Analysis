import os
import urllib
import datetime

from BeautifulSoup import BeautifulSoup

class hotnewsParser:
    """
    Hotnews Parser
    """

    def parse(self, link, source, kind, date):

        x = datetime.datetime.now()

        path1 = source + '/' + kind + '/' + date + '/' + link.rsplit('/')[-1]

        pFile = urllib.urlopen(link)
        fileToRead = pFile.read()
        pFile.close()
        soup = BeautifulSoup(fileToRead)

        if not os.path.exists(path1):
            os.makedirs(path1)
            """
            save article and comments
            """
            fd1 = open(path1+"/articol.html", "w")

            rawP = soup.findAll(attrs={"class":"title"})
            fd1.write(str(rawP[0].contents[0]))
            fd1.write('\n------------------------\n')

            rawP = soup.findAll(attrs={"id":"articleContent"})
            for i in rawP[0].contents:
                if i == ' ':
                    continue
                fd1.write(str(i))

            fd1 = open(path1 + "/comments" + str(x.hour) + ":" + str(x.minute) + ".html", "w")

            rawP = soup.findAll(attrs={"id":"comments"})
            if len(rawP) != 0:
                rawP1 = rawP[0].findAll("li")
                if len(rawP1) > 0:
                    for i in rawP1:
                        comment_body = i.findAll(attrs={"class":"cCon"})
                        comment_rate = i.findAll(attrs={"class":"ra"})
                        fd1.write(str(comment_rate[0].contents[1].contents[0]) + "#@$" + str(comment_body))
                        if len(comment_body) > 1:
                            for j in range(1, len(comment_body)):
                                    fd1.write("\n^&*" + str(comment_rate[j].contents[1].contents[0]) + "#@$" + str(comment_body[j].contents[0]))

                        fd1.write("\n-------------------------------\n")



            fd1.close()

        else:
            """
            save just comments
            """
            fd1 = open(path1 + "/comments" + str(x.hour) + ":" + str(x.minute) + ".html", "w")

            rawP = soup.findAll(attrs={"id":"comments"})
            if len(rawP) != 0:
                rawP1 = rawP[0].findAll("li")
                if len(rawP1) > 0:
                    for i in rawP1:
                        comment_body = i.findAll(attrs={"class":"cCon"})
                        comment_rate = i.findAll(attrs={"class":"ra"})
                        fd1.write(str(comment_rate[0].contents[1].contents[0]) + "#@$" + str(comment_body))
                        if len(comment_body) > 1:
                            for j in range(1, len(comment_body)):
                                    fd1.write("\n^&*" + str(comment_rate[j].contents[1].contents[0]) + "#@$" + str(comment_body[j].contents[0]))
                        
                        fd1.write("\n-------------------------------\n")

            fd1.close()
