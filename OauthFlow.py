#!/usr/bin/env python3

import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect

# This code will generate a manual long-lasting token
APP_KEY = ""
APP_SECRET = ""

auth_flow = DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)

# Generates a link to creating authorization token
authorize_url = auth_flow.start()
print("1. Go to: " + authorize_url)
print("2. Click \"Allow\" (you might have to log in first).")
print("3. Copy the authorization code.")
auth_code = input("Enter the authorization code here: ").strip()

try:
    oauth_result = auth_flow.finish(auth_code)

# Printed token will be copied manually to use in future application
    print("Access token:", oauth_result)
except Exception as e:
    print('Error: %s' % (e,))
    exit(1)

with dropbox.Dropbox(oauth2_access_token=oauth_result.access_token) as dbx:
    dbx.users_get_current_account()
    print("Successfully set up client!")