#!/usr/bin/python3
from fabric.api import *

env.hosts = ['web-01_ip_address']

def upload():
    put("./tyrell_corp.sql", "~/", use_sudo=True)
