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
- Click add button, choose "Google Galaxy Nexus - 4.2.2 - API 17 - 720x1280". Leave the default device name.
- Set its predefined to "320x480 - 160dpi".
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

