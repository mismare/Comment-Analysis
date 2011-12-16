all:
	echo > hotnews.ro/economy/LinksToParse.txt
	echo > hotnews.ro/politics/LinksToParse.txt
	echo > adevarul.ro/economy/LinksToParse.txt
	echo > adevarul.ro/politics/LinksToParse.txt
clean:
	rm -rf adevarul.ro
	rm -rf hotnews.ro
