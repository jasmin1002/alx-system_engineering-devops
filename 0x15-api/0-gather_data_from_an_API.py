#!/usr/bin/python3
'''
Documentation goes here
'''

import requests
from sys import argv

try:
    id = argv[1]
except IndexError:
    print('Require employee\'s ID but none')

domain = 'https://jsonplaceholder.typicode.com'
todos = 'todos'
users = 'users'
user_id = {'userId': id}
url_s = '{}/{}'.format(domain, users)
res = requests.get(url_s)

if res.status_code == 200:
    users = res.json()
    name = ''

    for user in users:
        if str(user.get('id')) == id:
            name = user['name']
            break

    if name:
        url_t = '{}/{}'.format(domain, todos)
        res = requests.get(url_t, params=user_id)

        if res.status_code == 200:
            todos = res.json()

            done = [data for data in todos if data['completed']]

            msg = 'Employee {} is done with tasks({}/{}):'\
                .format(name, len(done), len(todos))
            print(msg)

            for completed in done:
                msg = '\t {}'.format(completed['title'])
                print(msg)
        else:
            print(res.status_code)
else:
    print(res.status_code)
