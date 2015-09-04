# monkey-checker

Monkey checker is only work under Windows.

## Installation Guide
- Install [Python 2] (http://python.org)
- Install request library
```bat
cd %Python_Installation%/Scripts
pip install requests
```
- Install [Git] (http://www.git-scm.com/download/win)
Remember to tick "Use Git from the Windows Command Prompt"
- Install [Genymotion] (https://www.genymotion.com/)
- Install Android SDK & set sdk-tools (monkeyrunner & adb) to ENV.
- Click add button, choose "Google Galaxy Nexus - 4.2.2 - API 17 - 720x1280". Leave the default device name.
- Set its predefined to "320x480 - 160dpi".
- Install ARM translation zip.
- Start the device once and set superSU's automatic response to "Allow".
- Set no password for git command. Open git bash and run:
```Bash
vim ~/.git-credentials
https://{username}:{password}@{git repo host}
git config --global credential.helper store
```
Then go into crazymonkey repo and run
```Bash
git pull
```
input the username/password to auto save it.



## Usage
```bat
python monkey-checker.py #run all the jobs
python monkey-checker.py {jobName} #run specific job
```
