#!/usr/bin/python3
from fabric.api import *

env.hosts = ['web-01_ip_address', 'web-02_ip_address']

def upload():
    put("./setup_mysql_holberton_user.sql", "~/", use_sudo=True, mode='0744')
