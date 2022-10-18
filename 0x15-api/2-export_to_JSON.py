#!/usr/bin/python3
'''
TODOS management application
'''

import json
import requests
from sys import argv


if __name__ == '__main__':
    def fetch(id):
        '''
        Fetch data by endpoint of resource for
        given id

        Args:
            id (str): Stores user id

        Return:
            return list of tasks
        '''

        #: str: Stores resource location
        domain = 'https://jsonplaceholder.typicode.com'

        #: obj of str: Stores services to consume
        endpoints = {'users': 'users', 'todos': 'todos'}

        #: str: url
        url = '{}/{}/'.format(domain, endpoints['users'])

        #: obj of str: Stores query parameter
        user_id = {'userId': id}
        name = ''

        res = requests.get(url + user_id['userId'])
        if res.status_code == 200:
            name = res.json()['username']
        else:
            print(res.status_code)

        if not name:
            print('User\'s name is not found!')
        else:
            url = url + '{}/{}'.format(id, endpoints['todos'])
            res = requests.get(url)

            if res.status_code == 200:
                todos = res.json()
                processed_list = []

                for todo in todos:
                    processed_list.append({
                        'task': todo['title'],
                        'completed': todo['completed'],
                        'username': name
                    })
        return processed_list

    def jsonify(data):

        with open(id + '.json', 'w', encoding='utf-8') as w_file:
            str_data = json.dumps({id: data})
            w_file.write(str_data)

    def app():
        data = fetch(id)
        jsonify(data)

    try:
        id = argv[1]
    except IndexError:
        print('Require employee\'s ID but not found')
    else:
        app()
