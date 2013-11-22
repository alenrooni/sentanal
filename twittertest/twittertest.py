'''
Created on Nov 21, 2013

@author: usr
'''
#!/usr/bin/env python

'''Post a message to twitter'''

__author__ = 'dewitt@google.com'

import ConfigParser
import getopt
import os
import sys
import twitter


USAGE = '''Usage: tweet [options] message

  This script posts a message to Twitter.

  Options:

    -h --help : print this help
    --consumer-key : the twitter consumer key
    --consumer-secret : the twitter consumer secret
    --access-key : the twitter access token key
    --access-secret : the twitter access token secret
    --encoding : the character set encoding used in input strings, e.g. "utf-8". [optional]

  Documentation:

  If either of the command line flags are not present, the environment
  variables TWEETUSERNAME and TWEETPASSWORD will then be checked for your
  consumer_key or consumer_secret, respectively.

  If neither the command line flags nor the enviroment variables are
  present, the .tweetrc file, if it exists, can be used to set the
  default consumer_key and consumer_secret.  The file should contain the
  following three lines, replacing *consumer_key* with your consumer key, and
  *consumer_secret* with your consumer secret:

  A skeletal .tweetrc file:

    [Tweet]
    consumer_key: *consumer_key*
    consumer_secret: *consumer_password*
    access_key: *access_key*
    access_secret: *access_password*

'''

class TweetRc(object):
  def __init__(self):
    self._config = None

  def GetConsumerKey(self):
    return self._GetOption('consumer_key')

  def GetConsumerSecret(self):
    return self._GetOption('consumer_secret')

  def GetAccessKey(self):
    return self._GetOption('access_key')

  def GetAccessSecret(self):
    return self._GetOption('access_secret')

  def _GetOption(self, option):
    try:
      return self._GetConfig().get('Tweet', option)
    except:
      return None

  def _GetConfig(self):
    if not self._config:
      self._config = ConfigParser.ConfigParser()
      print 'reading config file'
      self._config.read('.tweetrc')
    return self._config


rc = TweetRc()
consumer_key = rc.GetConsumerKey()
consumer_secret = rc.GetConsumerSecret()
access_key =  rc.GetAccessKey()
access_secret = rc.GetAccessSecret()
print access_key

api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,
                    access_token_key=access_key, access_token_secret=access_secret,
                    input_encoding='utf-8')


#status = api.PostUpdate('hhhhhhhhhhhhhhhhh')
tws = api.GetTrendsWoeid(12789690)
for tw in tws:
    print tw
 