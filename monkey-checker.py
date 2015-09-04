import ConfigParser
import os
import requests
import time

__author__ = 'Alfred Shi'

configParser = ConfigParser.ConfigParser()
configParser.optionxform = str
configParser.read("monkey-checker.conf")

os.system("pullRepo.bat " + configParser.get("crazy_monkey", "apk_repo_path"))

os.system('start /b startGenymotion.bat')

time.sleep(60)

r = requests.get(configParser.get('master', 'running_job_query_api'))
i = 0

for apkId in r.json():
    i = i + 1

    print "[" + apkId + "]\t" + "Start running " + apkId + "..."
    print "Remain apk: " + str(len(r.json()) - i)
    package_name = ""
    script_name = ""
    f = open(configParser.get("crazy_monkey", "apk_repo_path") + "\\apk\\" + apkId + "_test.sh")
    lines = f.readlines()
    for line in lines:
        if line.startswith("package="):
            package_name = line[8:]
        elif line.startswith("$ANDROID_SDK_HOME/tools/monkeyrunner $CRAZY_MONKEY_HOME/apk/"):
            script_name = line[60:-3]

    print "[" + apkId + "]\t" + "Installing APK..."
    os.system("installAPK.bat " + configParser.get("crazy_monkey", "apk_repo_path") + "\\apk\\" + apkId + ".apk")

    print "[" + apkId + "]\t" + "Start to run script..."
    os.system("monkeyrunner " + configParser.get("crazy_monkey", "apk_repo_path") + "\\apk\\" + script_name + " 192.168.56.101:5555")

    print "[" + apkId + "]\t" + "Uninstall APK..."
    os.system("adb uninstall " + package_name)

    print "[" + apkId + "]\t" +  "test done."