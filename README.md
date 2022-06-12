# Machine_Learning_project

## This is my first Machine Learning project

### Software and account requirement for project.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)

Creating conda environment

```
conda create -p venv python==3.7 -y

conda activate venv/
```
OR

```
conda activate venv

pip install -r requirements.txt

```
To Add files to git

```git add .
```
OR

```
git add <file_name>
```
>Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status

```
git status
```

To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github

```
git push origin main
```

To check remote url

```
git remote -v
```

_To setup CI/CD pipeline in heroku we need 3 information_

1.HEROKU_EMAIL = anishyadav7045075175@gmail.com
2.HEROKU_API_KEY = < You get it from Heroku -> account_settings -> Scroll_to_bottom >
3.HEROKU_APP_NAME = < App_name in Heroku >

_TO BUILD DOCKER IMAGE_

docker build -t <image_name>:<tagname> .

>Note: Image name for docker must be lowercase

_To list docker image_

docker images

_To Run docker image_

docker run -p 5000:5000 -e PORT=5000 f8c749e73678


_To check running container in docker_

docker ps


_To stop docker conatiner_

docker stop <container_id>