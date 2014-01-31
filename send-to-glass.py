#!/usr/bin/python

import httplib2
import pprint

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
import sys

message = str(sys.argv[1])

def insert_timeline_item(service, text, content_type=None, attachment=None,
                         notification_level=None):
  timeline_item = {'text': text}
  media_body = None
  if notification_level:
    timeline_item['notification'] = {'level': notification_level}
  if content_type and attachment:
    media_body = MediaIoBaseUpload(
        io.BytesIO(attachment), mimetype=content_type, resumable=True)
  try:
    return service.timeline().insert(
        body=timeline_item, media_body=media_body).execute()
  except errors.HttpError, error:
    print 'An error occurred: %s' % error

# load the credentials from the file
storage = Storage('credentials')
credentials = storage.get()

# Create an httplib2.Http object and authorize it with our credentials
http = httplib2.Http()
http = credentials.authorize(http)

# create a Mirror API service
mirror_service = build('mirror', 'v1', http=http)

# insert it into the timeline
insert_timeline_item(mirror_service, message, None, None, "DEFAULT")

