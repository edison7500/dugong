import os
from fabric.api import local
from fabric.contrib.project import rsync_project
from fabric.api import run, env

env.hosts = ['jiaxin.im', '47.91.130.68']
# env.hosts = ['67.207.85.65',]
# env.hosts = ['47.91.130.68',]
env.user = "jiaxin"


def test_blog():
    local("./manage.py test blog")

def deploy_python():
    local('find . -name "*.pyc" -exec rm {} \;')
    rsync_project(
        remote_dir='/data/www/dugong/',
        local_dir='{dir}/'.format(dir=os.getcwd()),
        exclude=('.git', 'db.sqlite3', '.idea/'),
        delete=True,
    )

def deploy():
    test_blog()
    deploy_python()
