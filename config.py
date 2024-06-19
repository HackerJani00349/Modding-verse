from os import getenv

class Config(object):
      API_HASH = getenv("d71ad4ec048ab41677a1a439b21ff0c9")
      API_ID = int(getenv("29426486", 0))      
      BOT_TOKEN = getenv("6965255627:AAGHAspJSX01m1vaKfp6faZdWRJg-hDQtKg", "")
      CHANNEL = list(x for x in getenv("-1002244796953", "").replace("-1002194819972", " ").split(' '))
