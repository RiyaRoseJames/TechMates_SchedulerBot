from __future__ import print_function

import datetime
import datefinder
import os.path
import timedelta
import pytz
from pprint import pprint
# import service



def create_event(start_time_str, summary, duration=1,attendees=None, description=None, location=None):
    matches = list(datefinder.find_dates(start_time_str))
    if len(matches):
        start_time = matches[0]
        end_time = start_time + datetime.timedelta(hours=duration)
                
    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': pytz.timezone,
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': pytz.timezone,
        },
        'attendees': [
        {'email':attendees },
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
        
    return service.events().insert(calendarId='primary', body=event,sendNotifications=True).execute()

create_event('18 december 12.30pm',"meeting",0.5,"yoosufsada@gmail.com","test description","discord")