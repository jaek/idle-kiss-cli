#!/usr/bin/python3

import cmd
import requests
import config
import pprint as p
import os.path
import json
import vent

class VentShell(cmd.Cmd):

    def __init__(self, url=config.url):
        super(VentShell, self).__init__()
        self.intro='Vent test shell.'
        self.url=config.url
        self.vent_url=config.vent_child
        self.prompt='('+self.url+')'
        self.headers= { 'content-type':'application/json' }

    def do_exit(self, arg):
        'exit the REPL'
        exit()

    def do_get_all(self, args):
        'retrieve all vents'
        v = requests.get(self.url)
        p.pprint(v.json())

    def do_get_vent(self, vent_id, filename=None):
        'retrieve a single vent by id'
        v = requests.get(self.url+vent_id)
        if filename==None:
            p.pprint(v.json())
        else:
            f = open(filename, 'a')
            f.write('test')

    def do_set_url(self, url):
        'set the url'
        self.url = url
        print('url is now set to:' + self.url)
        self.prompt='('+self.url+')'

    def do_post_vent(self, fname):
        'post a vent'
        v = vent.Vent()
        if os.path.isfile(fname):
            f = open(fname, 'r') 
            v.add_body(f.read())
        else:
            v.add_body(str(fname))

        json_vent = v.export_vent()
        v = requests.post(url=self.url, data=json_vent, headers=self.headers) 

    def do_heart_vent(self, vent_id):
        'heart vent{id}'
        h = requests.post(self.url+vent_id+'/heart')
        print(self.url+vent_id+'/heart')
        if h.status_code == requests.codes.ok:
            print("heart request succeeded")
        else:
            print("heart request failed")
    
    def do_test(self):
        do_post_vent(test)
if __name__ == '__main__':
    v=VentShell()
    v.cmdloop()
