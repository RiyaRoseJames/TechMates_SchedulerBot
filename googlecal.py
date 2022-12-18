from __future__ import print_function
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import datetime
import datefinder
import os.path
from google.oauth2.credentials import Credentials
import timedelta
import pytz
from pprint import pprint
import pickle
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
SCOPES = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=SCOPES)
credentials = flow.run_console()
pickle.dump(credentials, open("token.pkl", "wb")) 
credentials = pickle.load(open("token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)
result = service.calendarList().list().execute()
def create_event(start_time_str, summary, duration=1,attendees=None, description=None, location=None):
    matches = list(datefinder.find_dates(start_time_str))
    if len(matches):
        start_time = matches[0]
        end_time = start_time + datetime.timedelta(hours=duration)
        print(start_time, end_time)
        start_time = start_time.strftime("%Y-%m-%dT%H:%M:%S")
        end_time = end_time.strftime("%Y-%m-%dT%H:%M:%S")
        print("timezone", pytz.timezone)
    event = {
       'summary': 'Google I/O 2015',
      'location': '800 Howard St., San Francisco, CA 94103',
      'description': 'A chance to hear more about Google\'s developer products.',
        'start': {
            'dateTime': start_time,
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Asia/Kolkata',
        },
        'attendees': [
        {'email':'akhilshalil22@gmail.com' },
    ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    print('''*** %r event added: 
    With: %s
    Start: %s
    End:   %s''' % (summary.encode('utf-8'),
        attendees,start_time, end_time))
        
    event = service.events().insert(calendarId='primary', body=event,sendNotifications=True).execute()
    print(event.get('htmlLink'))
    
create_event('24 Jul 12.30pm', "Test Meeting using CreateFunction Method",0.5,"akhilshalil22@gmail.com","Test Description","Mentone, VIC,Australia")