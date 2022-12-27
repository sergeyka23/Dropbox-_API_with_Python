#!/usr/bin/env python3

import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect


APP_KEY = ""
APP_SECRET = ""

auth_flow = DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)

authorize_url = auth_flow.start()
print("1. Go to: " + authorize_url)
print("2. Click \"Allow\" (you might have to log in first).")
print("3. Copy the authorization code.")
auth_code = input("Enter the authorization code here: ").strip()

try:
    access_token = auth_flow.finish(auth_code)
    #access_token, _ = web_auth.finish(code)

    print("Access token:", access_token)
except Exception as e:
    print('Error: %s' % (e,))
    exit(1)

with dropbox.Dropbox(oauth2_access_token=oauth_result.access_token) as dbx:
    dbx.users_get_current_account()
    print("Successfully set up client!")