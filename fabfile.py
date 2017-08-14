import os
from fabric.api import local
from fabric.context_managers import cd
from fabric.contrib.project import rsync_project
from fabric.api import run, env

env.hosts = ['47.91.130.68', ]
# env.hosts = ['67.207.85.65',]
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

def deploy_static():
    with cd("/data/www/dugong/"):
        run("/home/jiaxin/.virtualenvs/dugong/bin/python manage.py "
            "collectstatic --noinput --settings=dugong.settings.production")
        run("/home/jiaxin/.virtualenvs/dugong/bin/python manage.py "
            "compress --settings=dugong.settings.production")

def reload_server():
    run("sudo supervisorctl reload dugong")



def deploy():
    test_blog()
    deploy_static()
    deploy_python()
