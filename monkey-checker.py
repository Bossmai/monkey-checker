import ConfigParser
import os

__author__ = 'liashi'

configParser = ConfigParser.ConfigParser()
configParser.optionxform = str
configParser.read("monkey-checker.conf")

print "Read configuration..."
os.system("pullRepo.bat " + configParser.get("crazy_monkey", "apk_repo_path"))



