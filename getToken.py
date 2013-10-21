import os
import sys
import webbrowser
import urllib

CLIENT_ID = '446856592102595'
REDIRECT_URI = 'http://localhost'
CLIENT_SECRET = '03b98cd544170bff1672f4aea4971fc7'

def login():

    
    EXTENDED_PERMS = ['user_likes',
                      'user_friends',
                      ]
    args  = dict(client_id=CLIENT_ID, redirect_uri=REDIRECT_URI,
                 scope=','.join(EXTENDED_PERMS), type='user_agent',
                 display='popup')

    
    webbrowser.open('https://graph.facebook.com/oauth/authorize?'+urllib.urlencode(args))

def extend(token):
    args = dict(grant_type = 'fb_exchange_token',
                client_id = CLIENT_ID,
                client_secret = CLIENT_SECRET,
                fb_exchange_token = token)

    webbrowser.open('https://graph.facebook.com/oauth/access_token?'+urllib.urlencode(args))

if __name__ == '__main__':
    login()
    token = raw_input('Enter Your Access_token : ')
    extend(token)
             
