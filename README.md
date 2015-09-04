# monkey-checker

Monkey checker is only work under Windows.

## Installation Guide
1. Install [Git] (http://www.git-scm.com/download/win)
Remember to tick "Use Git from the Windows Command Prompt"
2. Install [Genymotion] (https://www.genymotion.com/)
3. Click add button, choose "Google Galaxy Nexus - 4.2.2 - API 17 - 720x1280". Leave the default device name.
4. Set its predefined to "320x480 - 160dpi".
5. Start the device once and set superSU's automatic response to "Allow".
6. Open git bash and run
```Bash
vim ~/.git-credentials
https://{username}:{password}@{git repo host}
git config --global credential.helper store
```
