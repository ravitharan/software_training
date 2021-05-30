#! /usr/bin/env python3

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.http import MediaFileUpload
import sys

# If modifying these scopes, delete the file token.pickle.
#SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def upload_file(file_name):
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': 'daraz_usb',
        'mimeType': 'application/vnd.google-apps.spreadsheet'
    }
    media = MediaFileUpload(file_name,
                            mimetype='text/csv',
                            resumable=True)
    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='webViewLink').execute()
    print('\nFile link: {}'.format(file.get('webViewLink')))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Argument error\nUsage: {} <file_name>".format(sys.argv[0]))
        exit(1)
    upload_file(sys.argv[1])
