#!/usr/bin/python3
'''
Documentation goes here
'''

import csv
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
            name = user['username']
            break

    if name:
        url_t = '{}/{}'.format(domain, todos)
        res = requests.get(url_t, params=user_id)

        if res.status_code == 200:
            todos = res.json()

            new_l = []
            for data in todos:
                new_l.append(
                    [data['userId'], name, data['completed'], data['title']]
                )

            with open('USER_ID.csv', 'w', encoding='utf-8') as w_file:
                write = csv.writer(w_file, quoting=csv.QUOTE_ALL)
                write.writerows(new_l)

        else:
            print(res.status_code)
else:
    print(res.status_code)
