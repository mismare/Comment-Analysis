#! /usr/bin/python

import os

"""
    Create directory hierarchy
"""

os.makedirs("adevarul.ro")
os.makedirs("adevarul.ro/economy")
fd = open("adevarul.ro/economy/LinksToParse.txt", "w")
fd.closed
os.makedirs("adevarul.ro/politics")
fd = open("adevarul.ro/politics/LinksToParse.txt", "w")
fd.closed

os.makedirs("hotnews.ro")
os.makedirs("hotnews.ro/economy")
fd = open("hotnews.ro/economy/LinksToParse.txt", "w")
fd.closed

os.makedirs("hotnews.ro/politics")
fd = open("hotnews.ro/politics/LinksToParse.txt", "w")
fd.closed
