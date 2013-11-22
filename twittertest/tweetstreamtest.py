'''
Created on Nov 22, 2013

@author: usr
'''
import tweetstream

words = words = ["opera", "firefox", "safari", "ie", "chrome"]
people = None
locations = None


stream = tweetstream.FilterStream("alenrooni", "M0sht@ri", track=words, follow=people, locations=locations)
for tweet in stream:
    print tweet