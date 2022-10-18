#!/usr/bin/python3
'''
TODOS management application
'''

import requests
from sys import argv

if __name__ == '__main__':
    def print_todos_detail(id):
        '''
        fetch_todos function prints detail information
        about assigned tasks

        Args:
            id (int): Stores user id

        Return:
            return None
        '''

        #: str: Stores resource location
        domain = 'https://jsonplaceholder.typicode.com'

        #: obj of str: Stores services to consume
        endpoints = {'users': 'users', 'todos': 'todos'}

        #: str: url
        url = '{}/{}'.format(domain, endpoints['users'])

        #: obj of int: Stores query parameter
        user_id = {'userId': id}
        name = ''

        res = requests.get(url + '/' + user_id['userId'])
        if res.status_code == 200:
            name = res.json()['name']
        else:
            print(res.status_code)

        if not name:
            print('User\'s name not found')
        else:
            url = '{}/{}'.format(domain, endpoints['todos'])
            res = requests.get(url, params=user_id)

            if res.status_code == 200:
                todos = res.json()
                completed = [
                    todo for todo in todos if todo['completed']
                ]

                msg = 'Employee {} is done with tasks({}/{}):'\
                    .format(name, len(completed), len(todos))
                print(msg)

                for done in completed:
                    msg = '\t {}'.format(done['title'])
                    print(msg)

    try:
        id = argv[1]
    except IndexError:
        print('Require employee\'s ID but not found')
    else:
        print_todos_detail(id)
