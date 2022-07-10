# First_ML_project

# Software and Account Requirement
Start machine Learning Project
1. Github Account - 
2. Heroku Account
3. VC Code 
4. Git Cli  


Creating virtual enviroment


'''
conda create -p venv python==3.7 -y

conda activate venv/


https://github.com/avnyadav/machine_learning_project

'''

To set up CD/ CI

heroku api key - c34ecf4a-8f1f-4aa6-83a6-6d3eebb64c72

email id - abi.hermy@gmail.com

Applicztion name- myfirstmlproject

python setup.py install

pip install -r requirements.txt

-e . means # This will install all lib used in other packages too


#install ipynb kernel
"""
    pip install ipykernel

    
"""
===================

Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@abigit24 
avnyadav
/
machine_learning_project
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
machine_learning_project/README.md

Avnish327030 assignment added
Latest commit 477337e 8 days ago
 History
 1 contributor
115 lines (85 sloc)  1.67 KB

Start Machine Learning project.
Software and account Requirement.
Github Account
Heroku Account
VS Code IDE
GIT cli
GIT Documentation
Creating conda environment

conda create -p venv python==3.7 -y
conda activate venv/
OR

conda activate venv
pip install -r requirements.txt
To Add files to git

git add .
OR

git add <file_name>
Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status

git status
To check all version maintained by git

git log
To create version/commit all changes by git

git commit -m "message"
To send version/changes to github

git push origin main
To check remote url

git remote -v
To setup CI/CD pipeline in heroku we need 3 information

HEROKU_EMAIL = anishyadav7045075175@gmail.com
HEROKU_API_KEY = <>
HEROKU_APP_NAME = ml-regression-app
BUILD DOCKER IMAGE

docker build -t <image_name>:<tagname> .
Note: Image name for docker must be lowercase

To list docker image

docker images
Run docker image

docker run -p 5000:5000 -e PORT=5000 f8c749e73678
To check running container in docker

docker ps
Tos stop docker conatiner

docker stop <container_id>
python setup.py install
Install ipykernel

pip install ipykernel
Data Drift: When your datset stats gets change we call it as data drift

Write a function to get training file path from artifact dir
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
You have no unread notifications