all:
	echo > hotnews.ro/economy/LinksToParse.txt
	echo > hotnews.ro/politics/LinksToParse.txt
	echo > adevarul.ro/economy/LinksToParse.txt
	echo > adevarul.ro/politics/LinksToParse.txt
prepare:
	mkdir hotnews.ro
	mkdir hotnews.ro/economy
	mkdir hotnews.ro/politics
	mkdir adevarul.ro
	mkdir adevarul.ro/economy
	mkdir adevarul.ro/politics

clean:
	rm -rf adevarul.ro
	rm -rf hotnews.ro
