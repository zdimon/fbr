# -*- coding: utf-8 -*-
from fabric.api import *
import os
from contextlib import contextmanager as _contextmanager
        
def production_env():
    """Окружение для продакшена"""
#    env.hosts = ['chat.mirbu.com']
#    env.key_filename = [os.path.join(os.environ['HOME'], '.ssh', 'id_rsa.pub')]  # Локальный путь до файла с ключами
    env.user = 'zdimon'  # На сервере будем работать из под пользователя "webmaster"
    env.project_root = '/home/zdimon/fbr_ve/fbr'  # Путь до каталога проекта (на сервере)
    env.password = 'HEvfhbyrf76'
    env.activate = 'source /home/zdimon/fbr_ve/bin/activate'


env.hosts = ['mirbu.com']
env.port =  22

@_contextmanager
def virtualenv():
    with cd(env.project_root):
        with prefix(env.activate):
            yield




def deploy():
    production_env()  # Инициализация окружения
    with virtualenv():
        run('git pull') # Пуляемся из репозитория
        #run('pip install -r requirements.txt') # ставим пакеты
        #run('bower install')
        run('./manage.py schemamigration map --auto') # Собираем статику
        run('./manage.py migrate')
        run('git add --all')
        run('git commit -m "from server"')
        run('git push')
        #run('find . -name "*.mo" -print -delete')  # Чистим старые скомпиленные файлы gettext'а
        #run('./manage.py compilemessages')  # Собираем новые файлы gettext'а
        #run('sudo supervisorctl restart all')

