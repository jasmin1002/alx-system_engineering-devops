#!/usr/bin/python3
from fabric.api import *

env.hosts = ['web-02_ip_address']
def download():
    get(remote_path='/etc/mysql/mysql.conf.d/mysqld.cnf', local_path="./4-mysql_configuration_replica", use_sudo=True)
